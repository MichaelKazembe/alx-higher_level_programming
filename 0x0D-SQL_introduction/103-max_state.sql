--  script that displays average temp by each state in descending order
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
