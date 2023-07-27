# Write your MySQL query statement below
SELECT contest_id, round(count(user_id) * 100 / (SELECT count(*) FROM Users), 2) as percentage
FROM Register as r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC