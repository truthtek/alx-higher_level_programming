-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `avg_temp`   -- Selects the city column and calculates the average temperature from the value column, aliasing it as avg_temp
FROM `temperatures`                          -- Specifies the table from which to retrieve the data
GROUP BY `city`                              -- Groups the records by the city column
ORDER BY `avg_temp` DESC;                    -- Orders the result set by the avg_temp column in descending order
