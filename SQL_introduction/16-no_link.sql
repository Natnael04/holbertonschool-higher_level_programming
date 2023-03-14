-- lists all record of the table by their group
SELECT ANY_VALUE(score) AS score, ANY_VALUE(name) AS name
FROM second_table
WHERE name
GROUP BY name
ORDER BY score DESC;