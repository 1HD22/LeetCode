# Write your MySQL query statement below
SELECT name, bonus
FROM Employee as e
LEFT JOIN Bonus as b
ON e.empId = b.empId
WHERE bonus IS NULL OR bonus < 1000