-- models/03_average_distance_by_type.sql

WITH avg_distance AS (
  SELECT
    type,
    AVG(traveled_distance) AS average_distance
  FROM
    TrafficData
  WHERE
    traveled_distance IS NOT NULL
  GROUP BY
    type
)

SELECT
  type,
  average_distance
FROM
  avg_distance