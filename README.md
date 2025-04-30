# Gas-Price-Predictor

RUN 
make envsetup
then
source env/bin/activate

Do:
export API_KEY= <API>

banco api call = curl https://dadosabertos.bcb.gov.br/api/3/action/package_search?q=1207 > gdp_resp_show.txt


extrac_data_py contains all the python scripts to extract .csv files from API's, import it inside dag script python file to run it in DAG tasks, need to create connection via script from timescaledb to airflow

need to implement bronze, silver, gold file structure

create staging schema for silver inside DB
gold for analysis, think trough it further on.
