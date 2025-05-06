from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from etl_functions import run_pyspark_etl

dag = DAG("api_elt_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@hourly")

task = PythonOperator(
    task_id="run_etl",
    python_callable=run_pyspark_etl,
    dag=dag
)
