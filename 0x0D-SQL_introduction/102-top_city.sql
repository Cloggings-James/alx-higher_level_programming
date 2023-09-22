USE hbtn_0c_0;

SELECT city, ROUND(AVG((value - 32) / 1.8), 4) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

