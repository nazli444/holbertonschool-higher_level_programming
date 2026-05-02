-- List records with score >= 10 ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE scor >= 10
ORDER BY score DESC;
