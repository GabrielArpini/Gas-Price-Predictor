envsetup:
	echo "AIRFLOW_UID=50000" > .env	
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt
docker:
	docker compose up -d