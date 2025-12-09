from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract():
    print("Extrayendo data desde la fuente…")
    # Aquí iría la lógica de lectura (S3, Mongo, API, etc.)

def transform():
    print("Transformando data con PySpark…")
    # Aquí se ejecutará el script PySpark (lo agregamos luego)

def validate():
    from validation.schema import validate_data  # Pandera schema
    validate_data()
    print("Validación completada.")

def load():
    print("Cargando data validada al destino…")

default_args = {
    "owner": "sebastian",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="etl_diario",
    default_args=default_args,
    description="Pipeline ETL diario",
    schedule_interval="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="validate", python_callable=validate)
    t4 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3 >> t4
