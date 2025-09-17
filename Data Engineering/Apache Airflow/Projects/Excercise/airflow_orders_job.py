from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.models.param import Param
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocSubmitJobOperator,
)
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "batch_spark_job_new",
    default_args=default_args,
    description="A DAG to run Spark job on Dataproc",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 7, 25),
    catchup=False,
    tags=["dev"],
    params={
        "execution_date": Param(
            default="NA", type="string", description="Execution date in yyyymmdd format"
        ),
    },
)

# Fetch configuration with fallback values
try:
    config = Variable.get("cluster_details", deserialize_json=True)
except KeyError:
    # Fallback configuration if variable doesn't exist
    config = {
        "CLUSTER_NAME": "dynamicparam-backfilling-cluster-airflow",
        "PROJECT_ID": "ninth-quarter-471814-i3",
        "REGION": "us-central1",
    }

CLUSTER_NAME = config["CLUSTER_NAME"]
PROJECT_ID = config["PROJECT_ID"]
REGION = config["REGION"]

pyspark_job_file_path = "gs://airflow-projects-gdsk/airflow-project-excercise/spark_code/orders_data_process.py"


def get_execution_date(ds_nodash, **kwargs):
    execution_date = kwargs["params"].get("execution_date", "NA")
    if execution_date == "NA":
        execution_date = ds_nodash
    return execution_date


get_execution_date_task = PythonOperator(
    task_id="get_execution_date",
    python_callable=get_execution_date,
    provide_context=True,
    op_kwargs={"ds_nodash": "{{ ds_nodash }}"},
    dag=dag,
)

PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {
        "main_python_file_uri": pyspark_job_file_path,
        "args": ["--date={{ ti.xcom_pull(task_ids='get_execution_date') }}"],
    },
}

submit_pyspark_job = DataprocSubmitJobOperator(
    task_id="submit_pyspark_job",
    job=PYSPARK_JOB,
    region=REGION,
    project_id=PROJECT_ID,
    dag=dag,
)

get_execution_date_task >> submit_pyspark_job
