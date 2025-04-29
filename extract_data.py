from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import re
import os

def get_gas_download_links():
    base_url = 'https://dados.gov.br/dados/api/publico/conjuntos-dados/'
    headers = {
        'chave-api-dados-abertos': os.getenv("API_KEY")
    }
    r = requests.get(base_url + 'serie-historica-de-precos-de-combustiveis-e-de-glp', headers=headers)
    regex_txt = 'https:\/\/www\.gov\.br\/anp\/pt-br\/centrais-de-conteudo\/dados-abertos\/arquivos\/shpc\/dsas\/ca\/ca-20\d{2}-\d{2}\.csv'
    links = re.findall(regex_txt, str(r.json()))
    return links

with DAG(
    dag_id="Download_gas"

)
    
download_data()