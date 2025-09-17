from datetime import timedelta, datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    "author": "venkat",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "email": "venkatasaikadamati@gmail.com",
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": False,
}

dag = DAG(
    "basic_dag_parallel",
    description="dags to test parallel execution of 3 dags",
    default_args=default_args,
    start_date=datetime(2025, 9, 1),
    schedule_interval=timedelta(days=1),
    catchup=False,
)


def hello():
    print("printing hello using PythonOperator")


task1 = PythonOperator(task_id="print_using_python1", python_callable=hello, dag=dag)

task2 = BashOperator(
    task_id="print_using_bash1",
    bash_command="echo printing hello using BashOperator: 1",
    dag=dag,
)

task3 = BashOperator(
    task_id="print_using_bash2",
    bash_command="echo printing hello using BashOperator: 2",
    dag=dag,
)

task1 >> [task2, task3]
