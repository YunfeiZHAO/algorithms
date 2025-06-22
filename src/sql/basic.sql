-- STATION
-- id: number, city: varchar(21), lat_n: number, long_w: number

-- 1, String operations in SQL

-- Search with case insensitive
-- get name from stations table with name starting with 'a', 'b', or 'c' and ending with 'x', 'y', or 'z'
-- and city has os at the third position (sql is 1-indexed)
-- order by first 3 characters of name in descending order and id in ascending order
-- limit to 10 results
SELECT name FROM stations
WHERE 
    LOWER(LEFT(city, 1)) in ('a', 'b', 'c') AND
    LOWER(RIGHT(city, 1)) NOT IN ('a', 'b', 'c') AND
    CHARINDEX(LOWER(city), 'os') = 3 --LOWER(city) LIKE '%os%'
ORDER BY 
    SUBSTR(name, 1,3) DESC,
    id ASC
LIMIT 10;


-- 2, Some calculations in SQL

-- Round can finish with 0.123499999, need cast to get 0.1235
SELECT CAST(
    ROUND(
        SQRT(
            POWER(MAX(LAT_N) - MIN(LAT_N), 2) +
            POWER(MAX(LONG_W) - MIN(LONG_W), 2)
        ), 4
    ) AS DECIMAL(10,4) --10 digits in total, with 4 digits after the decimal point 
) as englob_square_distance
FROM STATION;

-- Median calculation
WITH Ordered AS (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
           COUNT(*) OVER () AS total_rows
    FROM STATION
)
SELECT ROUND(AVG(LAT_N), 4) AS median
FROM Ordered
WHERE row_num IN (FLOOR((total_rows + 1) / 2), CEIL((total_rows + 1) / 2));

-- 3, Pivot table in SQL with CTE and window functions
WITH Ranked AS (
    SELECT 
        name,
        occupation,
        ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rn
    FROM occupations
),
All_ranks AS (
    SELECT DISTINCT rn FROM Ranked
),
Doctors AS (
    SELECT rn, name AS Doctor FROM Ranked WHERE occupation = 'Doctor'
),
Professors AS (
    SELECT rn, name AS Professor FROM Ranked WHERE occupation = 'Professor'
),
Singers AS (
    SELECT rn, name AS Singer FROM Ranked WHERE occupation = 'Singer'
),
Actors AS (
    SELECT rn, name AS Actor FROM Ranked WHERE occupation = 'Actor'
)
SELECT 
    d.Doctor,
    p.Professor,
    s.Singer,
    a.Actor
FROM All_ranks r
LEFT JOIN Doctors d ON r.rn = d.rn
LEFT JOIN Professors p ON r.rn = p.rn
LEFT JOIN Singers s ON r.rn = s.rn
LEFT JOIN Actors a ON r.rn = a.rn
ORDER BY r.rn;