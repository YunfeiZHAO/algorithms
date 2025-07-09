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
-- CAST and ROUND functions
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
-- https://www.hackerrank.com/challenges/occupations
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

-- 4, Case statement in SQL
-- https://www.hackerrank.com/challenges/what-type-of-triangle
SELECT
CASE
    WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
    WHEN A = B AND B = C THEN 'Equilateral'
    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
    ELSE 'Scalene'
END AS type
FROM TRIANGLES;
-- https://www.hackerrank.com/challenges/the-pads
SELECT 
CASE
    WHEN occupation='Doctor' THEN  CONCAT(name, '(D)')
    WHEN occupation='Professor' THEN  CONCAT(name, '(P)')
    WHEN occupation='Singer' THEN  CONCAT(name, '(S)')
    WHEN occupation='Actor' THEN  CONCAT(name, '(A)')
END AS name_p
FROM occupations
ORDER BY name;
-- string manipulation with CONCAT and goup by operation
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(occupation), 's.') AS stat
FROM occupations
GROUP BY occupation
ORDER BY COUNT(*) ASC, LOWER(occupation) ASC;

-- Sub query in SQL with CASE
-- https://www.hackerrank.com/challenges/binary-search-tree-1
SELECT 
    n,
    CASE
        WHEN p IS NULL THEN 'Root'
        WHEN n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS node_type
FROM bst
ORDER BY n;

-- 5, Sub query
-- https://www.hackerrank.com/challenges/the-company
SELECT
    company_code,
    founder,
    COUNT(DISTINCT lead_manager_code) AS lead_manager_count,
    COUNT(DISTINCT senior_manager_code) AS senior_manager_count,
    COUNT(DISTINCT manager_code) AS manager_count,
    COUNT(DISTINCT employee_code) AS employee_count
FROM (
    SELECT DISTINCT e.*, c.founder
    FROM employee e 
    JOIN company c ON e.company_code = c.company_code
) AS CE
GROUP BY company_code, founder
ORDER BY company_code;

-- Several sub queries in SQL
-- https://www.hackerrank.com/challenges/earnings-of-employees
SELECT MAX(earnings), COUNT(*) AS count
FROM (
    SELECT employee_id, months * salary AS earnings
    FROM employee
) AS e
WHERE e.earnings = (
    SELECT MAX(months * salary)
    FROM employee
)

-- # AGGREGATE FUNCTIONS
-- 1, max, cast
-- https://www.hackerrank.com/challenges/weather-observation-station-15
SELECT CAST(long_w AS DECIMAL(10,4))
FROM station
WHERE lat_n = (
    SELECT max(lat_n) FROM station
    WHERE lat_n < 137.2345)


-- 2, COUNT, SUM, AVG
-- https://www.hackerrank.com/challenges/revising-aggregations-sum
SELECT COUNT(*) FROM city WHERE district = 'california' -- count number of cities
SELECT SUM(population) FROM city WHERE district = 'california' -- sum population of cities in california
SELECT AVG(population) FROM city WHERE district = 'california' -- average population of cities in california

-- Rounded down the average population to the nearest integer
SELECT FLOOR(AVG(population)) FROM city
-- Operation between agg
SELECT MAX(population) - MIN(population) FROM city
-- CAST between int and str and round up
-- avg of salaries - avg of salaries excluding zeros
-- IN CAST: signed, unsigned, decimal is validated
SELECT
    CEIL(AVG(salary) - AVG(CAST(REPLACE(salary, '0', '') AS UNSIGNED))) AS salary_difference
FROM employees;


-- # JOIN
-- 1, Join with between
-- https://www.hackerrank.com/challenges/the-report
SELECT 
    CASE 
        WHEN g.Grade >= 8 THEN s.Name 
        ELSE 'NULL' 
    END AS Name,
    g.Grade,
    s.Marks
FROM Students s
JOIN Grades g
  ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY 
    g.Grade DESC,
    CASE 
        WHEN g.Grade >= 8 THEN s.Name
        ELSE NULL
    END ASC,
    CASE 
        WHEN g.Grade < 8 THEN s.Marks
        ELSE NULL
    END ASC;

-- 2, Join with sub query
-- https://www.hackerrank.com/challenges/the-pads
SELECT h.*
FROM
    hackers h
JOIN (
    SELECT s.hacker_id, COUNT(*) AS full_score_count
    FROM
        submissions AS s
    JOIN 
        challenges AS c ON s.challenge_id = c.challenge_id
    JOIN
        difficulty AS d ON c.difficulty_level = d.difficulty_level
    WHERE
        s.score = d.score
    GROUP BY s.hacker_id
) hc ON h.hacker_id = hc.hacker_id
WHERE
    hc.full_score_count > 1
ORDER BY
    hc.full_score_count DESC, hc.hacker_id ASC;


-- 3, Join with sub query 
-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
SELECT w.id, p.age, w.coins_needed, w.power
FROM wands w
JOIN wands_property p ON w.code = p.code
WHERE p.is_evil = 0
  AND w.coins_needed = (
      SELECT MIN(w2.coins_needed)
      FROM wands w2
      JOIN wands_property p2 ON w2.code = p2.code
      WHERE p2.is_evil = 0
        AND w2.power = w.power
        AND p2.age = p.age
  )
ORDER BY w.power DESC, p.age DESC;

-- 4, Alternative queries
-- https://www.hackerrank.com/challenges/draw-the-triangle-1
WITH RECURSIVE cte AS (
    SELECT 20 AS n
    UNION ALL
    SELECT n - 1 FROM cte WHERE n > 0
)
SELECT REPEAT('* ', n) FROM cte;