# import required libraries
from datetime import datetime, timedelta

from airflow import DAG

"""
Operators = Tasks, so dependencies can be created using '>>'
Flow
    - First, we configure our default_args which tells how airflow should behave
    - Second, we define DAG with name, description, start_date, schedule_interval
    - Third, we list down our Tasks using Operators and uniquely attached to DAG's
    - Fourth, we mention the order using >> for linear or '[]' for parallel execution 
"""
# Define the default args dictionary
# - help us configure how airflow should behave
"""
    owner name
    retry: number and delay
    email on failure
"""
default_args = {
    "owner": "venkat",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "venkatasai@gmail.com",
}

# Define a dags
"""
    dags name,
    description,
    default args <- pass the above configuration
    dags runs
        - start_date
        - schedule_interval
"""
dag = DAG(
    "example_dag",
    default_args=default_args,
    description="An example Dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval=timedelta(days=1),
)

# Define tasks and their dependency
# Operator + task id (unique identifier) + dags (to what dags this task belongs)
start_task = DummyOperator(task_id="start", dag=dag)
end_task = DummyOperator(task_id="end", dag=dag)

start_task >> end_task
