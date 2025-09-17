### Idea
We are trying to build a workflow automation that helps us with data processing and loading once a day.

### Why?
Usually for processing we need clusters that are way too costly and having them up and running throughout the day is not cost-efficient. We can use Airflow to schedule our jobs and only use the clusters when we need them.

### What are we planning to do?
Use Airflow to schedule a job that will:
1. Spin up a cluster on Google Cloud Dataproc
2. Run a PySpark job on the cluster that will process some data and save the results to Google Cloud Storage
3. Shut down the cluster

### Requirements 
1. Google Cloud Account with Dataproc and Cloud Storage enabled
2. Google Composer (Airflow Env) set up
3. A PySpark script that processes data and csv (raw files)
4. Airflow DAG to orchestrate the workflow
5. In GCP UI - cloud storage we need to create a new bucket
   - nested bucket named 
     - data
     - spark-code
   - In existing service account bucket: in DAG folder add our dag python code
### Noticeable Benefits
1. Cost Efficiency: By spinning up the cluster only when needed, we save on costs associated
2. Automation: The entire process is automated, reducing the need for manual intervention

### Note
Modern systems have discarded orchestration of clusters in favor of serverless solutions. Instead, now the focus is on just jobs. 

This project is more of a learning exercise to understand how orchestration works and how to use Airflow with Google Cloud Dataproc.**