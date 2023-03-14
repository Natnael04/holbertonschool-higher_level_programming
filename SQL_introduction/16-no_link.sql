-- lists all record of the table by their group
SELECT score, name
FROM second_table
GROUP BY 'name'
ORDER BY score DESC;