import unittest
import os
from datetime import datetime, timedelta
from airflow.models import DagBag
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from dags.load_csv_files import load_csv  

class TestTrafficDataDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag(dag_folder = os.path.abspath('../dags'))  

    def test_traffic_data_dag(self):
        dag_id = 'traffic_data_dag'
        dag = self.dagbag.get_dag(dag_id)
        
        self.assertIsNotNone(dag)

        # Check the number of tasks and their types
        expected_task_ids = ['load_data', 'insert_data', 'average_distance', 'average_speed']
        for task_id in expected_task_ids:
            task = dag.get_task(task_id)
            self.assertIsNotNone(task)
            self.assertTrue(isinstance(task, (PythonOperator, BashOperator)))

        # Check the task dependencies
        load_data_task = dag.get_task('load_data')
        insert_data_task = dag.get_task('insert_data')
        average_distance_task = dag.get_task('average_distance')
        average_speed_task = dag.get_task('average_speed')

        self.assertListEqual(load_data_task.downstream_task_ids, ['insert_data'])
        self.assertListEqual(insert_data_task.upstream_task_ids, ['load_data'])
        self.assertListEqual(insert_data_task.downstream_task_ids, ['average_distance', 'average_speed'])

if __name__ == '__main__':
    unittest.main()
