# Write your MySQL query statement below

SELECT round(count(*)/ (SELECT count(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date) IN
(SELECT player_id, date_add(min(event_date), INTERVAL 1 DAY)
FROM Activity
GROUP BY player_id)
