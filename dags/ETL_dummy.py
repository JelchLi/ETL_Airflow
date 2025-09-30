# Primer DAG en airflow para chequear la estructura
from airflow import DAG
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner' : 'Jose',
    'depends_on_past' : False, 
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1 
}

with DAG(
    'DAG_ETL_Dummy',
    default_args = default_args,
    description='Creacion de DAG ETL Dummy',
    schedule = None,
    tags = ['ETL', 'Ingenieria'] #Son como las key words
) as dag:
    
    #Definir tareas
    get_api_bash = EmptyOperator(
        task_id='get_api_bash'
        )
    get_api_python = EmptyOperator(task_id='get_api_python')
    
    join_trans = EmptyOperator(task_id = 'join_trans')
    
    load_postgreSQL = EmptyOperator(task_id = 'load_postgreSQL')
    
    [get_api_bash, get_api_python] >> join_trans >> load_postgreSQL
    
dag=dag