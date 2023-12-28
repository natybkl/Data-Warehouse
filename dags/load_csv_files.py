import pandas as pd
import os, sys
import csv

def load_csv():
    rpath = os.path.abspath('../data/20181024_d1_0830_0900 (5).csv')

    csv.field_size_limit(10000000) 
    # Create a new list to store the expanded rows
    expanded_rows = []

    with open(rpath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            values = row[0].split(';')  # Split the row values by ';'
            num_values = len(values)

            for i in range(1, num_values // 6 + 1):
                expanded_row = {
                    'track_id': values[0],
                    'type': values[1],
                    'traveled_d': values[2],
                    'avg_speed': values[3],
                    'lat': values[6 * (i - 1) + 4],
                    'lon': values[6 * (i - 1) + 5],
                    'speed': values[6 * (i - 1) + 6],
                    'lon_acc': values[6 * (i - 1) + 7],
                    'lat_acc': values[6 * (i - 1) + 8],
                    'time': values[6 * (i - 1) + 9]
                }

                expanded_rows.append(expanded_row)

    return expanded_rows


load_csv()