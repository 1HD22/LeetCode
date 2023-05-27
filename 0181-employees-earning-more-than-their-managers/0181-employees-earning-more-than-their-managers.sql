# Write your MySQL query statement below
SELECT
 e.name AS Employee
FROM
 EMPLOYEE e
INNER JOIN
 EMPLOYEE m
ON
 m.id = e.managerId
WHERE
 e.salary > m.salary