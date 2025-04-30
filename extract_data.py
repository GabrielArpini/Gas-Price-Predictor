import requests
import re
import os
from datetime import datetime

# This script will download all the csv and must be imported inside the dag workflow
# It is possible to add more scripts here and then to the dag task by just importing
# And a few implementation

def get_gas_y_sem(year: int, semester: int):
    base_url = 'https://dados.gov.br/dados/api/publico/conjuntos-dados/'
    headers = {
        'chave-api-dados-abertos': os.getenv("API_KEY")
    }
    
    r = requests.get(base_url + 'serie-historica-de-precos-de-combustiveis-e-de-glp', headers=headers)
    
    regex_txt = f'https:\/\/www\.gov\.br\/anp\/pt-br\/centrais-de-conteudo\/dados-abertos\/arquivos\/shpc\/dsas\/ca\/ca-{year}-0{semester}\.csv'
    link = re.search(regex_txt, str(r.json()))
    
    if link:
        print(f"Found link: {link.group()}")
        file_url = link.group()

        with requests.get(file_url, stream=True) as csv_data:
            if csv_data.status_code == 200:
                os.makedirs("data/bronze/gas", exist_ok=True)
                
                file_path = f"data/bronze/gas/gas_{year}_S0{semester}_raw.csv"
                with open(file_path, "wb") as f:
                    for chunk in csv_data.iter_content(chunk_size=1024):  
                        f.write(chunk)
                
                print(f"File saved as: {file_path}")
            else:
                print(f"Failed to fetch the file. Status code: {csv_data.status_code}")
    else:
        print("Error: No regex match for year/semester parameters")


# Run every march for safety, will only concatenate new year after updated.
def get_gdp_y():
    url_for_update = "https://dadosabertos.bcb.gov.br/api/3/action/package_search?q=1207"
    response = requests.get(url_for_update)
    data = response.json()
    first_result = data["result"]["results"][0]
    update_date = first_result["metadata_modified"]
    year = datetime.fromisoformat(update_date).year
    link = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1207/dados?formato=csv"
    with requests.get(link,stream=True) as csv_data:
        if csv_data.status_code == 200:
            os.makedirs("data/gdp/bronze", exist_ok=True)
            file_path = f"data/bronze/gdp/gdp_{year}_raw.csv"
            with open(file_path, "wb") as f:

                for chunk in csv_data.iter_content(chunk_size=1024):  
                    f.write(chunk)
                print(f"File saved as: {file_path}")
        else:
            print(f"Failed to fetch the file. Status code: {csv_data.status_code}")

