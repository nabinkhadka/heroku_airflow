from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os

dag = DAG(
    os.path.basename(__file__).split('.')[0],
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval="0 1 * * *"
)

t1 = BashOperator(
    task_id='print_path',
    bash_command='pwd',
    dag=dag
)
