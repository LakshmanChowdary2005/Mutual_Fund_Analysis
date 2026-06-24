-- 1
SELECT AVG(nav) FROM fact_nav;

-- 2
SELECT MAX(nav) FROM fact_nav;

-- 3
SELECT MIN(nav) FROM fact_nav;

-- 4
SELECT COUNT(*) FROM fact_nav;

-- 5
SELECT * FROM fact_nav ORDER BY nav DESC LIMIT 5;

-- 6
SELECT * FROM fact_nav ORDER BY nav ASC LIMIT 5;

-- 7
SELECT strftime('%Y', full_date) AS year,
AVG(nav)
FROM fact_nav
JOIN dim_date
ON fact_nav.date_id = dim_date.date_id
GROUP BY year;

-- 8
SELECT strftime('%m', full_date) AS month,
AVG(nav)
FROM fact_nav
JOIN dim_date
ON fact_nav.date_id = dim_date.date_id
GROUP BY month;

-- 9
SELECT COUNT(DISTINCT fund_id)
FROM fact_nav;

-- 10
SELECT fund_id,
AVG(nav)
FROM fact_nav
GROUP BY fund_id;