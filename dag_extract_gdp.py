from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from utils.db_conn import test_db_con
from extract_data import get_gdp_y


with DAG (
    dag_id = "extract_gdp",
    start_date=datetime(datetime.today()),
    schedule= "0 0 5 3 * ",
    catchup= False,
    tags=["gdp","bcb"]
    
) as dag:
    test_connection_task = PythonOperator (
        task_id = "connection_test",
        python_callable = test_db_con
    )
    extract_gdp_task = PythonOperator(
        task_id = "extract_gdp",
        python_callable = get_gdp_y
    )


    test_connection_task >> extract_gdp_task