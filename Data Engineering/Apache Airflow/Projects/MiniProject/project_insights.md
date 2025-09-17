1. The use of airflow to orchestrate data pipelines is really smooth but needs high level of maintenance if we try to manage the infrastructure too.
   - Better option is to leave infra and opt serverless option with primary focus on job management only.
   - Important note: one major downside we notice is cold-start of resource and for continuous jobs it is not a good option, instead opt dedicated resource
2. the dag name and task name we see come from task_id not from the python variable names.
3. **Ideal way to work with airflow dag implementation:** 
   - First draft a rough sketch of dag with tasks and dependencies
   - Then implement the tasks as functions in python
   - Then create the dag and tasks using python operators
   - Finally test the dag in airflow UI
4. When working with cloud, it is super crucial to ensure that adhoc creations are also removed. For instance, when setting up the dataproc cluster, metastore buckets are created in cloud storage and other resources as needed.