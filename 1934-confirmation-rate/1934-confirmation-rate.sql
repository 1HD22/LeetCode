#  Write your MySQL query statement below

SELECT s.user_id,
(CASE
    WHEN c.user_id IS NULL
        THEN 0
    ELSE ROUND(SUM(CASE WHEN c.action = "confirmed" THEN 1 ELSE 0 END) / COUNT(c.action),2)
END) AS confirmation_rate
FROM Signups as s
LEFT JOIN Confirmations as c
ON c.user_id = s.user_id
GROUP BY s.user_id