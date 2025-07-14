import pandas as pd
import sys


print(sys.argv)

day=sys.argv[1]

print(f'first pipeline on {day}')




services:
  postgres:
    image: postgres:13
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: airflow
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
    healthcheck:
      test: ["CMD", "pg_isready","-U","airflow"]
      interval: 5s
      retries: 5
    restart: always


docker run -it \
-e POSTGRES_DB=root \
-e POSTGRES_USER=root \
-e POSTGRES_PASSWORD=ny_taxi \
-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:13
