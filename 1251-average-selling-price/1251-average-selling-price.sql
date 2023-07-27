# Write your MySQL query statement below
SELECT p.product_id, round(sum(u.units * p.price) / sum(u.units), 2) AS average_price
FROM Prices as p
INNER JOIN UnitsSold as u
ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id, u.product_id