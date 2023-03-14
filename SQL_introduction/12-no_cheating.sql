-- update the score
UPDATE second_table
SELECT score, name
SET name = "Bob", score = 10;