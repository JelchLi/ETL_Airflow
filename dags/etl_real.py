# Primer DAG en airflow para chequear la estructura
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

default_args = {
    'owner' : 'Jose',
    'depends_on_past' : False, 
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1 
}

with DAG(
    'DAG_ETL_Real',
    default_args = default_args,
    description='Creacion de DAG para la prueba prototipo del entrenamiento orquestado para el Modelo',
    schedule = None,
    tags = ['ETL', 'Ingenieria'] #Son como las key words
) as dag:
    
    #Definir tareas
    get_api_bronze = DockerOperator(
        task_id='get_api_bronze',
        image='etl',
        api_version='auto',
        auto_remove='success',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[
            Mount(
                source='/home/jelch/ETL/data/bronze',
                target='/capa_bronze/data/bronze',
                type='bind',
            )
        ],
    )
    get_api_python = EmptyOperator(task_id='get_api_python')
    
    join_trans = EmptyOperator(task_id = 'join_trans')
    
    load_postgreSQL = EmptyOperator(task_id = 'load_postgreSQL')
    
    [get_api_bronze, get_api_python] >> join_trans >> load_postgreSQL
    
dag=dag