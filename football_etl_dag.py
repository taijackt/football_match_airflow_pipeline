from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

def get_match_data():
    import FootballMatchExtractor
    extractor = FootballMatchExtractor.Extractor(link="https://www.theguardian.com/football/results", days_ago=1)
    extractor.get_data()

default_args = {
    "owner":"admin",
    "start_date":days_ago(1),
    "email":["admin@admin.com"],
    "email_on_failure":False,
    "email_on_retry":False,
    "retries":0,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "football-match-ETL",
    default_args=default_args,
    description="get match data from webpage",
    schedule_interval=timedelta(days=1)
)

get_match_data = PythonOperator(
    task_id="extract-football-data",
    python_callable="get_match_data"m
    dag=dag
)

get_match_data