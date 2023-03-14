-- lists all record with a score greater than or equal to ten
SELECT score, name 
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;