from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
# from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

# Define your dbt model name and project directory
dbt_model_name = '03_average_distance_by_type'
dbt_project_dir = '/dbt'

# Default_args specify the default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),  # Start immediately
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG with its parameters
dag = DAG(
    'dbt_run_dag',
    default_args=default_args,
    description='DAG to run dbt models',
    schedule_interval=None,  # Set to None for manual triggering or use the @once decorator
)

# Use the BashOperator to run dbt commands
run_dbt_model = BashOperator(
    task_id=f'run_dbt_{dbt_model_name}',
    bash_command=f'dbt run --models {dbt_model_name} --project-dir {dbt_project_dir}',
    dag=dag,
)

# Set the task dependencies, if any
# Example: run_dbt_model.set_upstream(other_task)

if __name__ == "__main__":
    dag.cli()



# from datetime import timedelta, datetime
# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from airflow.operators.bash_operator import BashOperator
# import pandas as pd
# import os
# from sqlalchemy import create_engine

# # Set the database credentials
# username = 'postgres'
# password = 'nati@postgres'
# database = 'TrafficData'
# schema = 'Public'


# csv_file_path = os.path.abspath('../data/expanded_data.csv')

# # Create the SQLAlchemy engine
# engine = create_engine(f'postgresql://{username}:{password}@localhost/{database}')

# def load_csv_to_database():
#     # Read the CSV file into a pandas DataFrame
#     df = pd.read_csv(csv_file_path)

#     # Write the DataFrame to the database table
#     df.to_sql(name='traffic_data', con=engine, schema=schema, if_exists='replace', index=False)

#     # Close the database connection
#     engine.dispose()

# default_args = {
#     'owner': 'nathybkl',
#     'start_date': datetime(2023, 12, 20),
#     'retries': 5,
#     'retry_delay': timedelta(minutes=2),
# }

# dag = DAG(
#     dag_id='traffic_data_dag',
#     description='DAG for processing traffic data with dbt',
#     default_args=default_args,
#     schedule_interval='@daily',
# )

# task_load_data = PythonOperator(
#     task_id='load_data',
#     python_callable=load_csv_to_database,
#     dag=dag,
# )

# task_insert_data = BashOperator(
#     task_id='insert_data',
#     bash_command='dbt run --models=insert_data',
#     dag=dag,
# )

# task_average_distance = BashOperator(
#     task_id='average_distance',
#     bash_command='dbt run --models=average_distance',
#     dag=dag,
# )

# task_average_speed = BashOperator(
#     task_id='average_speed',
#     bash_command='dbt run --models=average_speed',
#     dag=dag,
# )

# task_load_data >> task_insert_data
# task_insert_data >> task_average_distance
# task_insert_data >> task_average_speed