-- lists all record of the table by their group
SELECT score, name
FROM second_table
GROUP BY score
ORDER BY name DESC;