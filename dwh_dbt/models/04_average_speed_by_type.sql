-- models/04_average_speed_by_type.sql

WITH avg_speed AS (
  SELECT
    type,
    AVG(avg_speed) AS average_speed
  FROM
    TrafficData
  WHERE
    avg_speed IS NOT NULL
  GROUP BY
    type
)

SELECT
  type,
  average_speed
FROM
  avg_speed