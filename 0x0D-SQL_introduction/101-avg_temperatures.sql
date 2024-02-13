--
SELECT city, AVG(temp_fahrenheit) AS avg_temp
  
FROM temperature
  
GROUP BY city
  
ORDER BY avg_temp DESC;
