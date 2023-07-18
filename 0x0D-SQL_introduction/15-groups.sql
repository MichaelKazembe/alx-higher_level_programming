-- Counts the number of records with the same score in the table
SELECT score, COUNT(*) AS count
FROM second_table 
GROUP BY score
ORDER BY count DESC;
