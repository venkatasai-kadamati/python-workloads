# practicing dag creation
from datetime import timedelta, datetime

from airflow import DAG
from airflow.example_dags.example_latest_only_with_trigger import task1

# defaults (how airflow should behave) - dags - task & dependency
default_args = {
    'author': 'venkat',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email': 'x@gmail.com',
    'email_on_retry': False,
    'email_on_failure': False,
}

# dag
dag = DAG(
        'testdag',
        description='....',
        default_args=default_args,
        start_date=datetime(...)
        schedule=timedelta(days=1)
)

start_task = DummyOperator(task_id='start', dag=dag)
end_task = DummyOperator(task_id='end', dag=dag)

