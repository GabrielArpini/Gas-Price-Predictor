# Gas-Price-Predictor

Set-up airflow id inside a .env
AIRFLOW_UID=50000


Set up env with makefile
envfile:
	echo "AIRFLOW_UID=50000" > .env

up: envfile
	docker compose up