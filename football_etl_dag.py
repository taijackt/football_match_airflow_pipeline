from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

def get_football_match_data():
    import FootballMatchExtractor
    extractor = FootballMatchExtractor.Extractor(link="https://www.theguardian.com/football/results", days_ago=1)
    return extractor.get_data()

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
    dag=dag,
    do_xcom_push=True
)

# branching = BranchPythonOperator(
#     task_id="branching",
#     python_callable=lambda x: 
# )

# upload_match_data = BashOperator(
#     task_id="upload-football-data",
#     bash_command=""
# )

get_match_data