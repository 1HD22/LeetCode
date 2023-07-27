# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales AS s
INNER JOIN Product AS P
ON p.product_id = s.product_id