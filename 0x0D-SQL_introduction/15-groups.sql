-- Counts the number of records with the same score in the table
SELECT score, COUNT(*) AS record
FROM second_table 
GROUP BY score
ORDER BY record DESC;
