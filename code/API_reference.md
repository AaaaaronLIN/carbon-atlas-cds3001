# Carbon Atlas API reference (Part 2)

Base URL: `http://127.0.0.1:5001`

All responses are JSON. All SQL is **parameterised** (`%s` placeholders) so a country name from the
query string can never change the query itself. Errors are returned as JSON too, so the page can show a
readable message instead of an HTML stack trace.

The two endpoints required by the course are marked ✅.

---

## ✅ `GET /api/sectors`

Sector totals for one country and one year. Defaults: `country=WORLD`, `year=` latest complete year.

**Query:** `?country=China&year=2025`

```json
[
  { "sector": "Industry", "total": 5384.58 },
  { "sector": "Power", "total": 4880.39 },
  { "sector": "Ground Transport", "total": 1091.54 },
  { "sector": "Residential", "total": 598.63 },
  { "sector": "Domestic Aviation", "total": 91.95 },
  { "sector": "International Aviation", "total": 42.05 }
]
```

```sql
SELECT sector, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = %s AND YEAR(date) = %s
GROUP BY sector
ORDER BY total DESC;
```

---

## ✅ `GET /api/monthly`

Monthly totals for one country — the series behind the line chart.

**Query:** `?country=WORLD`

```json
[
  { "month": "2019-01", "total": 3418.85 },
  { "month": "2019-02", "total": 2965.57 }
]
```

```sql
SELECT DATE_FORMAT(date, '%Y-%m') AS month, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = %s
GROUP BY month
ORDER BY month;
```

(The same query as the Part 2 tutorial, with the country moved into a parameter.)

---

## `GET /api/health`

Cheap proof that the API can reach MySQL. The page header pill uses it.

```json
{ "ok": true, "rows": 655200, "first_day": "2019-01-01", "last_day": "2026-08-31", "database": "carbon_lab" }
```

Returns HTTP 503 with `ok: false` when MySQL is unreachable.

---

## `GET /api/meta`

Dimensions and coverage, used to build the controls.

```json
{
  "row_count": 655200,
  "first_day": "2019-01-01",
  "last_day": "2026-08-31",
  "latest_complete_year": 2025,
  "complete_years": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
  "years": [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
  "countries": ["Austria", "Belgium", "..."],
  "sectors": ["Domestic Aviation", "..."],
  "unit": "MtCO2 per day",
  "source": "Carbon Monitor"
}
```

---

## `GET /api/country_year`

Annual totals for every country — feeds the map, the ranking table and the sparklines.

```json
[ { "country": "China", "year": 2025, "total": 12089.14, "days": 365 } ]
```

```sql
SELECT country, YEAR(date) AS year, ROUND(SUM(value), 2) AS total,
       COUNT(DISTINCT date) AS days
FROM carbon_emission
GROUP BY country, year
ORDER BY country, year;
```

`days` matters: it lets the page detect that 2026 has only 243 days and treat it as partial.

---

## `GET /api/country_ytd`

One year's country totals, compared **like-for-like** with the same months of 2019.

**Query:** `?year=2026`

```json
{
  "year": 2026,
  "through_month": 8,
  "partial": true,
  "world_total": 25013.66,
  "rows": [ { "country": "China", "total": 7841.53, "change_vs_2019_pct": 9.1 } ]
}
```

```sql
SELECT country, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE YEAR(date) = %s AND MONTH(date) <= %s
GROUP BY country;

SELECT country, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE YEAR(date) = 2019 AND MONTH(date) <= %s
GROUP BY country;
```

Why: summing a half-finished 2026 and comparing it with a full 2019 would show a fake 31% collapse.
This endpoint is the single place that prevents that ethical/analytical error.

---

## `GET /api/daily`

Daily totals for one country — the weekly-rhythm chart averages them by weekday.

**Query:** `?country=China`

```json
[ { "day": "2019-01-01", "total": 10.4231 } ]
```

---

## `GET /api/compare`

Monthly series for several countries in **one** query (an `IN (...)` list), so overlaying a second
country does not cost a second round trip per request.

**Query:** `?countries=China,United States`

```json
{
  "countries": ["China", "United States"],
  "series": {
    "China": [ { "month": "2019-01", "total": 1046.67 } ],
    "United States": [ { "month": "2019-01", "total": 470.11 } ]
  }
}
```

```sql
SELECT country, DATE_FORMAT(date, '%Y-%m') AS month, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country IN (%s, %s)
GROUP BY country, month
ORDER BY country, month;
```

---

## `GET /api/insights`

The facts behind the six Findings cards. The API returns **numbers only**; the page writes the sentences,
so wording can change without touching the database layer.

```json
{
  "latest_complete_year": 2025,
  "annual": [ { "year": 2019, "total": 36396.8, "days": 365 } ],
  "sectors": [ { "sector": "Power", "total": 13491.8, "share_pct": 35.6 } ],
  "top_sector": { "sector": "Power", "share_pct": 35.6, "total": 13491.8 },
  "top_country": { "country": "China", "total": 12089.14, "share_pct": 31.9 },
  "riser":  { "country": "Netherlands", "pct": 5.3,  "total": 156.4 },
  "faller": { "country": "France",      "pct": -6.0, "total": 259.92 },
  "peak_month": { "month": "2026-01", "total": 3590.16 },
  "covid_low":  { "month": "2020-04", "total": 2476.95 },
  "ytd": { "year": 2026, "months": 8, "days": 243, "total": 25013.66,
           "baseline_year": 2019, "change_pct": 3.9 }
}
```

The riser/faller query joins two one-year aggregates to itself and filters out emitters below
100 MtCO₂, so a tiny country cannot "win" the ranking with a one-off swing:

```sql
SELECT a.country, ROUND(a.v, 2) AS latest, ROUND(b.v, 2) AS previous,
       ROUND(100 * (a.v - b.v) / b.v, 1) AS pct
FROM (SELECT country, SUM(value) AS v FROM carbon_emission
      WHERE YEAR(date) = %s AND country NOT IN ('WORLD','EU27','ROW')
      GROUP BY country) a
JOIN (SELECT country, SUM(value) AS v FROM carbon_emission
      WHERE YEAR(date) = %s AND country NOT IN ('WORLD','EU27','ROW')
      GROUP BY country) b ON a.country = b.country
WHERE b.v > 100 AND a.v > 0
ORDER BY pct DESC;
```

---

## Error behaviour

| Situation | Response |
|---|---|
| MySQL not running / wrong password | `503` `{"error": "Cannot reach MySQL. Is the server running, and is the password in app.py correct?", "detail": "..."}` |
| Unknown country (no rows) | `200` with `[]` — the page keeps its layout and shows zeros |
| `/api/compare` with no names | `400` `{"error": "No countries given"}` |
| Unhandled error | `500` `{"error": "Server error", "detail": "..."}` |

## Security notes (asks in the Safety/Responsibility section)

* SQL injection is prevented by parameterised queries; the only string interpolation is the generated
  `?, ?, ?` placeholder list, whose length comes from a validated list of up to five names.
* Inputs are clamped (`countries` limited to 5, `year` parsed as int) so a query cannot be used to
  dump the whole table in one request.
* The app binds to `127.0.0.1`, not `0.0.0.0`, so it is not exposed on the campus network.
* Credentials live in one config block and can be overridden with environment variables.
