--
SELECT city, AVG(temp_fahrenheit) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
