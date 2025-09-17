from datetime import timedelta, datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocDeleteClusterOperator,
    DataprocSubmitJobOperator,  # correct import
)

default_args = {
    "author": "venkat",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "email": "venkat@gmail.com",
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": True,
}

dag = DAG(
    "clustersetup_process_destroy_dag",
    description="This dags will help us with the management of single run processing of data daily",
    default_args=default_args,
    start_date=datetime(2025, 9, 10),
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=["mini-project"],
)

"""
Task list
    1. create dataproc cluster 
    2. run spark job on dataproc
    3. delete dataproc cluster
"""


# task 1
# define cluster configuration
CLUSTER_NAME = "spark-airflow-cluster"
PROJECT_ID = "ninth-quarter-471814-i3"
REGION = "us-central1"
CLUSTER_CONFIG = {
    "master_config": {
        "num_instances": 1,  # master node
        "machine_type_uri": "n1-standard-2",  # machine type
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 30},
    },
    "worker_config": {
        "num_instances": 2,  # worker node
        "machine_type_uri": "n1-standard-4",  # machine type
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 30},
    },
}

create_dataproc_cluster = DataprocCreateClusterOperator(
    task_id="dataproc_cluster_creation",
    project_id=PROJECT_ID,
    cluster_name=CLUSTER_NAME,
    cluster_config=CLUSTER_CONFIG,
    region=REGION,
    dag=dag,
)

# task 2
GCS_JOB_FILE = (
    "gs://airflow-projects-gdsk/airflow-project-mini/spark-code/emp_batch_job.py"
)
PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": GCS_JOB_FILE},
}

# ? we have the option to pass spark session properties in the below job submission
"""
spark_job_resources_param={
    'spark.executor.instances': "4",
    'spark.executor.memory': "4g",
    'spark.executor.cores': "2",
    'spark.driver.memory': "2g",
    'spark.driver.cores': "2",
}
"""
submit_pyspark_job = DataprocSubmitJobOperator(
    task_id="pyspark_job_submission",
    job=PYSPARK_JOB,
    region=REGION,
    project_id=PROJECT_ID,
    dag=dag,
)

# task 3
delete_cluster = DataprocDeleteClusterOperator(
    task_id="cluster_deletion",
    project_id=PROJECT_ID,
    cluster_name=CLUSTER_NAME,
    region=REGION,  # fixed typo
    trigger_rule="all_done",
    dag=dag,
)

create_dataproc_cluster >> submit_pyspark_job >> delete_cluster
