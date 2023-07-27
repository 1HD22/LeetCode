# Write your MySQL query statement below
SELECT Distinct author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY id