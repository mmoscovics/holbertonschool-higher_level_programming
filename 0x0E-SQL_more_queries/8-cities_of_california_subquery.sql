-- lists all cities of California that are found in a database
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;