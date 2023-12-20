-- models/01_load_data.sql

{{ config(materialized='source') }}

SELECT
  track_id,
  type,
  traveled_distance,
  avg_speed,
  lat,
  lon,
  speed,
  lon_acc,
  lat_acc,
  time
FROM
  {{ source('my_data_source', 'expanded_data') }}