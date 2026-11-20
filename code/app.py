"""
Carbon Atlas - Part 2 API
===========================
A small Flask server that reads the Part 1 MySQL table and returns JSON.

Data flow (the story we tell in the presentation):
    Carbon Monitor CSV  ->  MySQL carbon_emission  ->  this API (JSON)  ->  index.html

Run it (from this folder):
    python3 app.py
Then open:
    http://127.0.0.1:5001/                -> the dashboard (index.html)
    http://127.0.0.1:5001/api/sectors     -> JSON (tutorial endpoint)
    http://127.0.0.1:5001/api/health      -> JSON (is the database reachable?)

How the code is organised:
    1. CONFIG       - database credentials + app settings
    2. run_sql()    - one helper that opens a connection, runs ONE query, returns rows
    3. TUTORIAL ENDPOINTS  /api/sectors and /api/monthly  (the two required by Part 2)
    4. DASHBOARD ENDPOINTS more aggregated views used by our own front end
    5. ERROR HANDLING      - friendly JSON instead of an HTML stack trace
    6. MAIN
"""

import os

import pymysql
from flask import Flask, jsonify, request, send_file
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------
# 1. CONFIG
# ---------------------------------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Credentials come from environment variables, with sensible defaults so the
# project still runs on the marker's own machine after `pip install -r`.
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    # Put YOUR MySQL password here, or set the DB_PASSWORD environment variable.
    # The placeholder is intentional: never commit a real password to a submission.
    "password": os.environ.get("DB_PASSWORD", "your_password"),
    "database": os.environ.get("DB_NAME", "carbon_lab"),
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
}

UNIT = "MtCO2 per day"       # the unit of every `value` in carbon_emission
SOURCE = "Carbon Monitor"    # https://carbonmonitor.org/

app = Flask(__name__, static_folder="static", static_url_path="/static")


# ---------------------------------------------------------------------------
# 2. THE ONE HELPER
# ---------------------------------------------------------------------------
def run_sql(sql, params=()):
    """Open a connection, run one parameterised query, return a list of dicts.

    Always closing the connection in `finally` keeps the demo stable: if a
    query fails we do not leak a MySQL connection and the next request works.
    """
    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        conn.close()


def scalar(sql, params=(), key=None):
    """Return the first column of the first row (or 0 when there is no row)."""
    rows = run_sql(sql, params)
    if not rows:
        return 0
    row = rows[0]
    return row[key] if key else list(row.values())[0]


def latest_complete_year():
    """Last year that has ~365 daily rows. 2026 is partial, so we prefer 2025.

    Why this matters: summing a half-finished year makes 2026 look like a huge
    drop. That would be a misleading chart - an ethical issue we discuss in the
    'Method & responsibility' section of the dashboard.
    """
    rows = run_sql(
        """
        SELECT YEAR(date) AS year, COUNT(DISTINCT date) AS days
        FROM carbon_emission
        WHERE country = 'WORLD'
        GROUP BY YEAR(date)
        ORDER BY year
        """
    )
    complete = [int(r["year"]) for r in rows if r["days"] >= 365]
    return complete[-1] if complete else int(rows[-1]["year"])


# ---------------------------------------------------------------------------
# 3. TUTORIAL ENDPOINTS  (these are the two required by Part 2 / Part 3)
# ---------------------------------------------------------------------------
# The aggregate behind /api/sectors. Naming the SQL keeps the route short and
# makes the query easy to show on a slide (see the Part 2 explanation).
SECTOR_SQL = """
    SELECT sector, ROUND(SUM(value), 2) AS total
    FROM carbon_emission
    WHERE country = %s AND YEAR(date) = %s
    GROUP BY sector
    ORDER BY total DESC
"""


@app.route("/api/sectors")
def sectors():
    """Total CO2 per sector. Defaults to the whole world, latest full year.

    Tutorial version: WHERE country = 'WORLD' GROUP BY sector.
    Our version adds two optional query-string filters so the same endpoint
    can power the country focus panel:
        /api/sectors?country=China&year=2025
    """
    country = request.args.get("country", "WORLD")
    year = request.args.get("year", type=int) or latest_complete_year()
    rows = run_sql(SECTOR_SQL, (country, year))
    return jsonify(rows)


@app.route("/api/monthly")
def monthly():
    """Total CO2 per calendar month for one country (the line chart source).

    Tutorial version: country = 'WORLD', month = DATE_FORMAT(date, '%Y-%m').
    We keep exactly that shape but let the caller choose the country.
    """
    country = request.args.get("country", "WORLD")
    rows = run_sql(
        """
        SELECT DATE_FORMAT(date, '%%Y-%%m') AS month,
               ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country = %s
        GROUP BY month
        ORDER BY month
        """,
        (country,),
    )
    return jsonify(rows)


# ---------------------------------------------------------------------------
# 4. DASHBOARD ENDPOINTS
# ---------------------------------------------------------------------------
@app.route("/api/health")
def health():
    """Cheap check used by the status pill in the page header."""
    try:
        rows = run_sql(
            "SELECT COUNT(*) AS rows_count, MIN(date) AS first_day, "
            "MAX(date) AS last_day FROM carbon_emission"
        )
        r = rows[0]
        return jsonify(
            ok=True,
            rows=r["rows_count"],
            first_day=str(r["first_day"]),
            last_day=str(r["last_day"]),
            database=DB_CONFIG["database"],
        )
    except Exception as exc:  # noqa: BLE001 - we want any failure to become JSON
        return jsonify(ok=False, error=str(exc)), 503


@app.route("/api/meta")
def meta():
    """Dimensions and coverage: the page uses this to build its controls."""
    totals = run_sql(
        "SELECT COUNT(*) AS row_count, MIN(date) AS first_day, "
        "MAX(date) AS last_day FROM carbon_emission"
    )[0]
    countries = [r["country"] for r in run_sql(
        "SELECT DISTINCT country FROM carbon_emission ORDER BY country")]
    sectors = [r["sector"] for r in run_sql(
        "SELECT DISTINCT sector FROM carbon_emission ORDER BY sector")]
    years = run_sql(
        """
        SELECT YEAR(date) AS year, COUNT(DISTINCT date) AS days
        FROM carbon_emission
        WHERE country = 'WORLD'
        GROUP BY YEAR(date)
        ORDER BY year
        """
    )
    complete = [int(r["year"]) for r in years if r["days"] >= 365]
    return jsonify(
        row_count=totals["row_count"],
        first_day=str(totals["first_day"]),
        last_day=str(totals["last_day"]),
        latest_complete_year=latest_complete_year(),
        complete_years=complete,
        years=[int(r["year"]) for r in years],
        countries=countries,
        sectors=sectors,
        unit=UNIT,
        source=SOURCE,
    )


@app.route("/api/country_year")
def country_year():
    """Every country x year total - feeds the map, the table and sparklines."""
    rows = run_sql(
        """
        SELECT country,
               YEAR(date) AS year,
               ROUND(SUM(value), 2) AS total,
               COUNT(DISTINCT date) AS days
        FROM carbon_emission
        GROUP BY country, year
        ORDER BY country, year
        """
    )
    return jsonify(rows)


@app.route("/api/country_ytd")
def country_ytd():
    """Country totals for one year, compared like-for-like with 2019.

    The last year in the database (2026) is incomplete. Comparing its raw
    annual sum with 2019 would show a fake 31% 'fall'. So we compare the SAME
    months of both years. This single endpoint therefore powers the KPI strip,
    the ranking table and the 'vs 2019' column, and stays correct for every year.

    Example: /api/country_ytd?year=2026
    """
    year = request.args.get("year", type=int) or latest_complete_year()
    through_month = int(scalar(
        "SELECT MAX(MONTH(date)) FROM carbon_emission WHERE YEAR(date) = %s",
        (year,)))

    rows = run_sql(
        """
        SELECT country, ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE YEAR(date) = %s AND MONTH(date) <= %s
        GROUP BY country
        ORDER BY total DESC
        """,
        (year, through_month),
    )
    base = run_sql(
        """
        SELECT country, ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE YEAR(date) = 2019 AND MONTH(date) <= %s
        GROUP BY country
        """,
        (through_month,),
    )
    base_by_country = {r["country"]: float(r["total"]) for r in base}
    world_total = next((float(r["total"]) for r in rows if r["country"] == "WORLD"), 0.0)

    result = []
    for r in rows:
        country = r["country"]
        total = float(r["total"])
        before = base_by_country.get(country)
        change = round(100 * (total / before - 1), 1) if before else None
        result.append({"country": country, "total": total,
                       "change_vs_2019_pct": change})

    return jsonify(
        year=year,
        through_month=through_month,
        partial=through_month < 12,
        world_total=world_total,
        rows=result,
    )


@app.route("/api/daily")
def daily():
    """Daily total for one country - used by the weekly-rhythm chart.

    Example: /api/daily?country=China
    """
    country = request.args.get("country", "WORLD")
    rows = run_sql(
        """
        SELECT DATE_FORMAT(date, '%%Y-%%m-%%d') AS day,
               ROUND(SUM(value), 4) AS total
        FROM carbon_emission
        WHERE country = %s
        GROUP BY day
        ORDER BY day
        """,
        (country,),
    )
    return jsonify(rows)


@app.route("/api/compare")
def compare():
    """Monthly series for several countries at once - overlay on the line chart.

    Example: /api/compare?countries=China,United States
    One SQL query with an IN (...) list is much faster than calling
    /api/monthly once per country.
    """
    raw = request.args.get("countries", "WORLD")
    countries = [c.strip() for c in raw.split(",") if c.strip()][:5]
    if not countries:
        return jsonify(error="No countries given"), 400

    placeholders = ", ".join(["%s"] * len(countries))
    rows = run_sql(
        f"""
        SELECT country,
               DATE_FORMAT(date, '%%Y-%%m') AS month,
               ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country IN ({placeholders})
        GROUP BY country, month
        ORDER BY country, month
        """,
        tuple(countries),
    )
    # Group by country in Python so the browser can draw one line per country.
    series = {name: [] for name in countries}
    for row in rows:
        series[row["country"]].append({"month": row["month"], "total": row["total"]})
    return jsonify({"countries": countries, "series": series})


@app.route("/api/insights")
def insights():
    """The numbers behind the 'Findings' cards.

    The API returns facts only; the page writes the sentences. Keeping text out
    of SQL means the wording can change without touching the database layer.
    """
    year = latest_complete_year()

    annual = run_sql(
        """
        SELECT YEAR(date) AS year,
               ROUND(SUM(value), 2) AS total,
               COUNT(DISTINCT date) AS days
        FROM carbon_emission
        WHERE country = 'WORLD'
        GROUP BY YEAR(date)
        ORDER BY year
        """
    )

    # --- sector leader in the latest complete year -------------------------
    sector_rows = run_sql(
        """
        SELECT sector, ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country = 'WORLD' AND YEAR(date) = %s
        GROUP BY sector
        ORDER BY total DESC
        """,
        (year,),
    )
    sector_sum = sum(float(r["total"]) for r in sector_rows) or 1.0
    top_sector = {
        "sector": sector_rows[0]["sector"],
        "share_pct": round(100 * float(sector_rows[0]["total"]) / sector_sum, 1),
        "total": float(sector_rows[0]["total"]),
    }

    # --- biggest country and its share of the world ------------------------
    country_rows = run_sql(
        """
        SELECT country, ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE YEAR(date) = %s AND country NOT IN ('WORLD', 'EU27', 'ROW')
        GROUP BY country
        ORDER BY total DESC
        """,
        (year,),
    )
    world_total = float(scalar(
        "SELECT ROUND(SUM(value), 2) FROM carbon_emission "
        "WHERE country = 'WORLD' AND YEAR(date) = %s", (year,)))
    top_country = {
        "country": country_rows[0]["country"],
        "total": float(country_rows[0]["total"]),
        "share_pct": round(100 * float(country_rows[0]["total"]) / world_total, 1)
        if world_total else 0,
    }

    # --- fastest riser / biggest faller (meaningful emitters only) ---------
    # Self-join of two one-year aggregates: latest year vs the year before.
    movers = run_sql(
        """
        SELECT a.country,
               ROUND(a.v, 2) AS latest,
               ROUND(b.v, 2) AS previous,
               ROUND(100 * (a.v - b.v) / b.v, 1) AS pct
        FROM (SELECT country, SUM(value) AS v
              FROM carbon_emission
              WHERE YEAR(date) = %s AND country NOT IN ('WORLD','EU27','ROW')
              GROUP BY country) a
        JOIN (SELECT country, SUM(value) AS v
              FROM carbon_emission
              WHERE YEAR(date) = %s AND country NOT IN ('WORLD','EU27','ROW')
              GROUP BY country) b
          ON a.country = b.country
        WHERE b.v > 100 AND a.v > 0
        ORDER BY pct DESC
        """,
        (year, year - 1),
    )

    # --- monthly extremes --------------------------------------------------
    peak_month = run_sql(
        """
        SELECT DATE_FORMAT(date, '%%Y-%%m') AS month,
               ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country = 'WORLD'
        GROUP BY month
        ORDER BY total DESC
        LIMIT 1
        """
    )[0]

    covid_low = run_sql(
        """
        SELECT DATE_FORMAT(date, '%%Y-%%m') AS month,
               ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country = 'WORLD'
          AND date BETWEEN '2020-01-01' AND '2020-12-31'
        GROUP BY month
        ORDER BY total ASC
        LIMIT 1
        """
    )[0]

    # --- year-to-date comparison (fair like-for-like for the partial year) -
    partial_year = int(annual[-1]["year"])
    partial_days = int(annual[-1]["days"])
    partial_month = int(run_sql(
        "SELECT MAX(MONTH(date)) AS m FROM carbon_emission "
        "WHERE country = 'WORLD' AND YEAR(date) = %s", (partial_year,))[0]["m"])
    ytd = run_sql(
        """
        SELECT YEAR(date) AS year, ROUND(SUM(value), 2) AS total
        FROM carbon_emission
        WHERE country = 'WORLD'
          AND MONTH(date) <= %s
          AND YEAR(date) IN (%s, %s)
        GROUP BY YEAR(date)
        """,
        (partial_month, partial_year, 2019),
    )
    ytd_by_year = {int(r["year"]): float(r["total"]) for r in ytd}
    ytd_now = ytd_by_year.get(partial_year, 0.0)
    ytd_2019 = ytd_by_year.get(2019, 0.0)

    return jsonify(
        latest_complete_year=year,
        annual=[{"year": int(r["year"]), "total": float(r["total"]),
                 "days": int(r["days"])} for r in annual],
        sectors=[{"sector": r["sector"], "total": float(r["total"]),
                  "share_pct": round(100 * float(r["total"]) / sector_sum, 1)}
                 for r in sector_rows],
        top_sector=top_sector,
        top_country=top_country,
        riser={"country": movers[0]["country"], "pct": float(movers[0]["pct"]),
               "total": float(movers[0]["latest"])} if movers else None,
        faller={"country": movers[-1]["country"], "pct": float(movers[-1]["pct"]),
                "total": float(movers[-1]["latest"])} if movers else None,
        peak_month={"month": peak_month["month"], "total": float(peak_month["total"])},
        covid_low={"month": covid_low["month"], "total": float(covid_low["total"])},
        ytd={
            "year": partial_year,
            "months": partial_month,
            "days": partial_days,
            "total": ytd_now,
            "baseline_year": 2019,
            "change_pct": round(100 * (ytd_now / ytd_2019 - 1), 1) if ytd_2019 else None,
        },
    )


# ---------------------------------------------------------------------------
# 5. ERROR HANDLING  (JSON everywhere, so the front end can show a clear message)
# ---------------------------------------------------------------------------
@app.errorhandler(pymysql.err.OperationalError)
def mysql_down(exc):
    return jsonify(
        error="Cannot reach MySQL. Is the server running, and is the password "
              "in app.py correct?",
        detail=str(exc),
    ), 503


@app.errorhandler(500)
def server_error(exc):
    return jsonify(error="Server error", detail=str(exc)), 500


# ---------------------------------------------------------------------------
# 6. MAIN
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    # absolute path: works no matter which folder the terminal is in
    return send_file(os.path.join(APP_DIR, "index.html"))


# Convenience aliases: a saved bookmark or an editor preview may ask for these
# instead of "/". Without them Flask answers 404 even though the app is running.
@app.route("/index.html")
@app.route("/dashboard")
@app.route("/home")
def home_alias():
    return send_file(os.path.join(APP_DIR, "index.html"))


@app.route("/favicon.ico")
def favicon():
    # The page supplies an inline SVG favicon; answer the automatic browser
    # request quietly so the console does not show a spurious 404.
    return ("", 204)


if __name__ == "__main__":
    # Default stays local (127.0.0.1). For a classroom LAN demo run:
    #   HOST=0.0.0.0 DB_PASSWORD=... python3 app.py
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5001"))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host=host, port=port, debug=debug)
