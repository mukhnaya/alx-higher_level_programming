-- do not list those with missing names
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
