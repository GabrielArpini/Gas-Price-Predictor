from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from utils.db_conn import test_db_con
from extract_data import get_gas_y_sem


with DAG (
    dag_id = "extract_gas",
    start_date=datetime(2004,1,1),
    schedule= "0 0 5 3 * ",
    catchup= False,
    tags=["gdp","bcb"]
    
) as dag:
    test_connection_task = PythonOperator (
        task_id = "connection_test",
        python_callable = test_db_con
    )
    extract_gas_task = PythonOperator(
        task_id = "extract_gas",
        python_callable = get_gas_y_sem
    )


    test_connection_task >> extract_gas_task