from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


dag = DAG(
    'test_dag',
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval="0 1 * * *"
)

t1 = BashOperator(
    task_id='list_current_directory',
    bash_command='ls',
    dag=dag
)
