db:
	docker compose up -d

ingest:
	cd text2sql && python ingest.py