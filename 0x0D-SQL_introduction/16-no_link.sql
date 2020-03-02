-- lists all records of a table with restrictions
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;