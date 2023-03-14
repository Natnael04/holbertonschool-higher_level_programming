-- lists number with same score
SELECT score, number
FROM second_table
GROUP BY score
HAVING number >= 1
ORDER BY score DESC;