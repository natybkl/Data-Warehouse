from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd
import os
from sqlalchemy import create_engine

# Set the database credentials
username = 'postgres'
password = 'nati@postgres'
database = 'TrafficData'
schema = 'Public'


csv_file_path = os.path.abspath('../data/expanded_data.csv')

# Create the SQLAlchemy engine
engine = create_engine(f'postgresql://{username}:{password}@localhost/{database}')

def load_csv_to_database():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Write the DataFrame to the database table
    df.to_sql(name='traffic_data', con=engine, schema=schema, if_exists='replace', index=False)

    # Close the database connection
    engine.dispose()

default_args = {
    'owner': 'nathybkl',
    'start_date': datetime(2023, 12, 20),
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    dag_id='traffic_data_dag',
    description='DAG for processing traffic data with dbt',
    default_args=default_args,
    schedule_interval='@daily',
)

task_load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_csv_to_database,
    dag=dag,
)

task_insert_data = BashOperator(
    task_id='insert_data',
    bash_command='dbt run --models=insert_data',
    dag=dag,
)

task_average_distance = BashOperator(
    task_id='average_distance',
    bash_command='dbt run --models=average_distance',
    dag=dag,
)

task_average_speed = BashOperator(
    task_id='average_speed',
    bash_command='dbt run --models=average_speed',
    dag=dag,
)

task_load_data >> task_insert_data
task_insert_data >> task_average_distance
task_insert_data >> task_average_speed