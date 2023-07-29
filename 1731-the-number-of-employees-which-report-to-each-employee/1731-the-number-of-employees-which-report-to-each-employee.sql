# Write your MySQL query statement below
SELECT Managers.employee_id, Managers.name, count(Employees.employee_id) AS reports_count, 
round(avg(Employees.age),0) AS average_age
FROM Employees as Managers
INNER JOIN Employees as Employees
ON Managers.employee_id = Employees.reports_to
GROUP BY Managers.employee_id
ORDER BY Managers.employee_id