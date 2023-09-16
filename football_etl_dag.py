from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.opreators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import FootballMatchExtractor
import os

def get_date():
    day = datetime.today() - timedelta(days=1)
    return day.strftime("%Y-%m-%d")

def get_football_match_data():
    extractor = FootballMatchExtractor.Extractor(link="https://www.theguardian.com/football/results", days_ago=1)
    return extractor.get_data()

def branching_data():
    file_name = f"match-data-{get_date()}.json"
    if os.path.exists(file_name):
        return "upload-file-to-s3"
    else:
        return "do-nothing"

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
    python_callable=get_football_match_data,
    dag=dag
)

branching = BranchPythonOperator(
    task_id="branching",
    python_callable=branching_data,
    dag=dag
)

upload_file = BashOperator(
    task_id="upload-file-to-s3",
    bash_command=f"aws s3 ./match-data-{get_date()}.json s3:/// ",
    dag=dag
)

remove_local_file = BashOperator(
    task="remove_local_file",
    bash_command=f"rm ./match-data-{get_date()}.json ",
    dag=dag
)

do_nothing = DummyOperator(
    task_id="do-nothing",
    dag=dag
)

get_match_data >> branching >> [upload_file, do_nothing]
upload_file >> remove_local_file