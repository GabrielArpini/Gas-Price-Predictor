from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import re

def download_data():
    base_url = 'https://dados.gov.br/dados/api/publico/conjuntos-dados/'
    headers = {
        'chave-api-dados-abertos': '' # API KEY
    }
    r = requests.get(base_url + 'serie-historica-de-precos-de-combustiveis-e-de-glp', headers=headers)
    regex_txt = 'https:\/\/www\.gov\.br\/anp\/pt-br\/centrais-de-conteudo\/dados-abertos\/arquivos\/shpc\/dsan\/20\d{2}\/precos-gasolina-etanol-\d{2}\.csv'
    links = re.findall(regex_txt, str(r.json()))
    print(links)
    
download_data()