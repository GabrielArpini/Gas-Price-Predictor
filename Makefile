.PHONY: envsetup docker rm

envsetup:
	echo "AIRFLOW_UID=50000" > .env
	python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt

docker:
	docker compose up -d
	@echo "Waiting for Airflow webserver to be ready to start db connection..."
	sleep 120
	docker compose exec airflow-webserver airflow connections add "timescaledb" \
		--conn-type "postgres" \
		--conn-host "host.docker.local" \
		--conn-login "airflow" \
		--conn-password "airflow" \
		--conn-schema "airflow" \
		--conn-port 5432
rm:
	docker compose down 