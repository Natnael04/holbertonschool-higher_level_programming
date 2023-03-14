-- lists all record of the table by their group
SELECT 'score', 'name'
FROM second_table
WHERE 'name' != ""
ORDER BY 'score' DESC