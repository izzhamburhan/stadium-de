
from datetime import datetime
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.wikipedia_pipeline import get_wikipedia_page




dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        "owner": "Izzham",
        "start_date": datetime(2024,4,2),
    },
    schedule_interval=None,
    catchup=False
)



# Extraction
extract_data_from_wikipedia = PythonOperator(
    task_id = "extract_data_from_wikipedia",
    python_callable=get_wikipedia_page,
    provide_context=True,
    op_kwargs={ "url":"https://en.wikipedia.org/wiki/List_of_Asian_stadiums_by_capacity"},
    dag=dag
)


# Preprocessing



# Write