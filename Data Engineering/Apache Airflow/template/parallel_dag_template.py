from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'venkat',  # use 'owner' instead of 'author'
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email': ['x@gmail.com'],  # email should be a list
    'email_on_failure': False,  # optional, prevents sending emails unless configured
    'email_on_retry': False
}

dag = DAG(
    'parallel_dag',
    description='template for parallel execution',
    default_args=default_args,
    start_date=datetime(2002, 11, 2),
    schedule_interval=timedelta(days=1),
)

task1 = DummyOperator(task_id='task1', dag=dag)
task2 = DummyOperator(task_id='task2', dag=dag)
task3 = DummyOperator(task_id='task3', dag=dag)
task4 = DummyOperator(task_id='task4', dag=dag)
task5 = DummyOperator(task_id='task5', dag=dag)

task1 >> [task2, task3, task4] >> task5
