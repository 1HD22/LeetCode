#  Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, count(e.subject_name) AS attended_exams
FROM Students as st
JOIN Subjects as su
LEFT JOIN Examinations as e
ON e.student_id = st.student_id AND e.subject_name = su.subject_name
GROUP BY st.student_id, su.subject_name
ORDER BY st.student_id, su.subject_name
