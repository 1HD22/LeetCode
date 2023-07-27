#  Write your MySQL query statement below
SELECT manager.name
FROM Employee as manager
INNER JOIN Employee as employee
ON manager.id = employee.managerId
GROUP BY manager.id
HAVING COUNT(manager.id) >= 5