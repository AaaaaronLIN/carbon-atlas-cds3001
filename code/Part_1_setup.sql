-- =====================================================================
--  CDS3001 Group Project · Part 1 — Database setup and CSV import
--  Data Fanatics
--
--  What this file does (run it top to bottom in the MySQL client):
--    1. Turns on local file import (MySQL 8 blocks it by default)
--    2. Creates the database carbon_lab and the table carbon_emission
--    3. Imports the Carbon Monitor CSV with LOAD DATA
--    4. Verifies the import (row count, date range, sample rows)
--    5. Runs the analytical queries that the Part 2 API calls
--
--  How to run (macOS):
--    /usr/local/mysql/bin/mysql --local-infile=1 -u root -p
--    source Part_1_setup.sql
--
--  How to run (Windows, Command Prompt):
--    cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
--    mysql --local-infile=1 -u root -p
--    source C:/path/to/Part_1_setup.sql
--
--  BEFORE RUNNING: replace
--    /path/to/carbonmonitor-global_datas_YYYY-MM-DD.csv
--  with the real path of your download.
--  On Windows use forward slashes: D:/downloads/carbonmonitor-global_datas_2026-08-31.csv
-- =====================================================================

-- ---------------------------------------------------------------------
-- 0. Allow the MySQL server to read local files.
--    Both sides must allow it: this line (server) + --local-infile=1 (client).
--    It resets when MySQL restarts, so it is part of this script.
-- ---------------------------------------------------------------------
SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';   -- Value must be ON

-- ---------------------------------------------------------------------
-- 1. Database
-- ---------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS carbon_lab
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE carbon_lab;

-- ---------------------------------------------------------------------
-- 2. Table
--    647,946 rows in the lecturer's example; our download has 655,200
--    (2019-01-01 → 2026-08-31). Larger downloads are fine: run
--    SHOW TABLE STATUS / SELECT COUNT(*) to confirm.
--    Column list matches the CSV: country, date, sector, value.
-- ---------------------------------------------------------------------
-- If carbon_emission already exists from an earlier attempt, uncomment the
-- next line to start clean (it deletes the imported rows, not the CSV):
-- DROP TABLE IF EXISTS carbon_emission;

CREATE TABLE IF NOT EXISTS carbon_emission (
  id      INT AUTO_INCREMENT PRIMARY KEY,
  country VARCHAR(50)  NOT NULL,
  date    DATE         NOT NULL,
  sector  VARCHAR(50)  NOT NULL,
  value   DOUBLE       NOT NULL,
  -- a country/sector/day should appear only once; this also speeds up
  -- the WHERE country = ... AND YEAR(date) = ... pattern used by the API
  UNIQUE KEY uq_country_date_sector (country, date, sector),
  KEY idx_country_date (country, date),
  KEY idx_date (date)
);

DESCRIBE carbon_emission;

-- ---------------------------------------------------------------------
-- 3. Import the CSV
--    The file has 4 columns plus a trailing comma, so MySQL sees an empty
--    5th column -> we catch it in @dummy.
--    The date is DD/MM/YYYY -> STR_TO_DATE converts it to a real DATE.
--    IGNORE 1 LINES skips the header row.
-- ---------------------------------------------------------------------
LOAD DATA LOCAL INFILE '/path/to/carbonmonitor-global_datas_2026-08-31.csv'
INTO TABLE carbon_emission
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(country, @date, sector, value, @dummy)
SET date = STR_TO_DATE(@date, '%d/%m/%Y');

-- Expected result: "Query OK, 6xxxxx rows affected ... Records: ... Deleted: 0 Skipped: 0 Warnings: 0"
-- If you see Warnings > 0, run: SHOW WARNINGS;

-- ---------------------------------------------------------------------
-- 4. Verification — the evidence we show in the presentation
-- ---------------------------------------------------------------------
SELECT COUNT(*)                    AS total_rows    FROM carbon_emission;
SELECT MIN(date) AS first_day, MAX(date) AS last_day FROM carbon_emission;
SELECT COUNT(DISTINCT country)     AS countries     FROM carbon_emission;
SELECT COUNT(DISTINCT sector)      AS sectors       FROM carbon_emission;
SELECT * FROM carbon_emission LIMIT 10;

-- Integrity checks: should return 0 rows each
SELECT COUNT(*) AS bad_values FROM carbon_emission WHERE value < 0;
SELECT COUNT(*) AS bad_dates  FROM carbon_emission WHERE date IS NULL;

-- ---------------------------------------------------------------------
-- 5. Analytical queries used by the Part 2 API
-- ---------------------------------------------------------------------

-- 5.1 /api/sectors — sector totals for one country and year
SELECT sector, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = 'WORLD' AND YEAR(date) = 2025
GROUP BY sector
ORDER BY total DESC;

-- 5.2 /api/monthly — monthly series for one country
SELECT DATE_FORMAT(date, '%Y-%m') AS month,
       ROUND(SUM(value), 2)       AS total
FROM carbon_emission
WHERE country = 'WORLD'
GROUP BY month
ORDER BY month;

-- 5.3 /api/country_year — annual totals for the map and the ranking table
SELECT country,
       YEAR(date)          AS year,
       ROUND(SUM(value), 2) AS total,
       COUNT(DISTINCT date) AS days
FROM carbon_emission
GROUP BY country, year
ORDER BY country, year;

-- 5.4 /api/country_ytd — like-for-like comparison with 2019
--     (2026 is incomplete, so we compare the same months only)
SELECT country, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE YEAR(date) = 2026 AND MONTH(date) <= 8
GROUP BY country
ORDER BY total DESC;

-- 5.5 /api/daily — daily series for the weekly-rhythm chart
SELECT DATE_FORMAT(date, '%Y-%m-%d') AS day,
       ROUND(SUM(value), 4)          AS total
FROM carbon_emission
WHERE country = 'China'
GROUP BY day
ORDER BY day;

-- 5.6 /api/compare — several countries in one query
SELECT country,
       DATE_FORMAT(date, '%Y-%m') AS month,
       ROUND(SUM(value), 2)       AS total
FROM carbon_emission
WHERE country IN ('China', 'United States')
GROUP BY country, month
ORDER BY country, month;

-- 5.7 /api/insights — fastest riser and biggest faller (self-join of
--     two one-year aggregates; small emitters filtered out)
SELECT a.country,
       ROUND(a.v, 2) AS latest,
       ROUND(b.v, 2) AS previous,
       ROUND(100 * (a.v - b.v) / b.v, 1) AS pct
FROM (SELECT country, SUM(value) AS v FROM carbon_emission
      WHERE YEAR(date) = 2025 AND country NOT IN ('WORLD','EU27','ROW')
      GROUP BY country) a
JOIN (SELECT country, SUM(value) AS v FROM carbon_emission
      WHERE YEAR(date) = 2024 AND country NOT IN ('WORLD','EU27','ROW')
      GROUP BY country) b ON a.country = b.country
WHERE b.v > 100 AND a.v > 0
ORDER BY pct DESC;

-- 5.8 Peak month and 2020 trough (used by the findings cards)
SELECT DATE_FORMAT(date, '%Y-%m') AS month, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = 'WORLD'
GROUP BY month
ORDER BY total DESC
LIMIT 1;

SELECT DATE_FORMAT(date, '%Y-%m') AS month, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = 'WORLD' AND date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY month
ORDER BY total ASC
LIMIT 1;

-- ---------------------------------------------------------------------
-- 6. Index performance check (optional evidence for the report)
-- ---------------------------------------------------------------------
EXPLAIN SELECT sector, ROUND(SUM(value), 2)
FROM carbon_emission
WHERE country = 'WORLD' AND YEAR(date) = 2025
GROUP BY sector;
