-- models/02_insert_data.sql

{{ config(materialized='incremental') }}

INSERT INTO TrafficData
SELECT * FROM {{ ref('load_data') }}