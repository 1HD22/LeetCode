#  Write your MySQL query statement below
SELECT query_name, round(avg(rating/position),2) AS quality, 
    round(sum(CASE WHEN rating<3 THEN 1 ELSE 0 END) * 100 / count(rating), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name