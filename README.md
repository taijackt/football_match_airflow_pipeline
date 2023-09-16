# Football match data ETL

<table>
<tr>
  <td><img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" align="left"  width="400" /></td>
  <td><img src="https://miro.medium.com/v2/resize:fit:750/1*q6F0j8HFHd8jeYXyQBqrCQ.jpeg" align="left"  width="400" /></td>
</tr>
</table>

### Background:
1. This project is going to scrap football match data from [online](https://www.theguardian.com/football/results) using Python (beautifulSoup and pandas).
2. Transform the data using pandas and save it into json file format.
3. Upload it AWS S3 bucket.
4. Automate the processes above with airflow by deploying everything on an EC2 instance.

### Project Diagram
![diagram](https://github.com/taijackt/football_match_airflow_pipeline/blob/main/screenshots/diagram.jpg)

### Tools
- Python>=3.7
  - Pandas
  - BeautifulSoup
  - Requests
  - Airflow
- AWS CLI

### Data Preview:
<table>
<tr>
  <td>Football match data on website</td>
  <td><img src="https://github.com/taijackt/football_match_airflow_pipeline/blob/main/screenshots/raw_data.jpg" align="left"  width="400" /></td>
</tr>
<tr>
  <td>Data after transformation</td>
  <td><img src="https://github.com/taijackt/football_match_airflow_pipeline/blob/main/screenshots/transformed_data.jpg" align="left"  width="400" /></td>
</tr>
</table>

### Steps:
1. Create an EC2 instance (Ubuntu) on AWS.
2. Install all the dependencies in `dependencies.sh`.
3. Copy the dag file `football_etl_dag.py` and directory `FootballMatchExtractor` to `~/airflow/dags`.
4. Initialize airflow database and create an admin account.
5. Start airflow webserver and scheduler.

### Result
<table>
<tr>
  <td>Dag in airflow</td>
  <td><img src="https://github.com/taijackt/football_match_airflow_pipeline/blob/main/screenshots/dags.jpg" align="left"  width="500" /></td>
</tr>
<tr>
  <td>Json in s3</td>
  <td><img src="https://github.com/taijackt/football_match_airflow_pipeline/blob/main/screenshots/s3.jpg" align="left"  width="500" /></td>
</tr>
</table>



