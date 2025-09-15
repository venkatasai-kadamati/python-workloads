from airflow import DAG
from datetime import timedelta, datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    'author': 'venkat',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email': 'venkatasaikadamati+airflow@gmail.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'depends_on_past': False
}

dag = DAG(
    'basic_day_linear',
    description='dag to print through both bash and python operator',
    default_args=default_args,
    start_date=datetime(2025, 9, 10),
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['dev']
)

task1 = BashOperator(
    task_id="print_using_bash",
    bash_command="echo hello world using BashOperator",
    dag=dag
)

# python function defined: will be called using python_callable inside tasks
def print_content():
    print("hello world using PythonOperator")

task2 = PythonOperator(
        task_id="print_using_python",
        python_callable=print_content,
        dag=dag
)

task1 >> task2

