from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sqlalchemy import create_engine

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 11)
}

dag = DAG('delete_record_from_db', default_args=default_args, schedule_interval='@hourly')

def check_data_exists(primary_id):
    engine = create_engine('postgresql://user:password@localhost:5432/my_database')
    connection = engine.connect()
    tables = ['table_1', 'table_2', 'table_3', 'table_4', 'table_5']
    for table in tables:
        query = f'SELECT COUNT(*) FROM {table} WHERE id={primary_id}'
        result = connection.execute(query)
        count = result.fetchone()[0]
        if count > 0:
            connection.close()
            return True
    connection.close()
    return False

def updateSelectedTaskStatus():
    return;

def delete_record(primary_id):
    engine = create_engine('postgresql://user:password@localhost:5432/my_database')
    connection = engine.connect()
    query = f'DELETE FROM my_table WHERE id={primary_id}'
    connection.execute(query)
    connection.close()

check_data = PythonOperator(
    task_id='selectTaskToDelete',
    python_callable=check_data_exists,
    op_kwargs={'primary_id': 123},
    dag=dag
)

delete_record = PythonOperator(
    task_id='deleteDataRecord',
    python_callable=delete_record,    
    dag=dag
)

updateSelectedTaskStatusTask = PythonOperator(
    task_id='updateSelectedTaskStatus',
    python_callable=updateSelectedTaskStatus,
    op_kwargs={'primary_id': 123},
    dag=dag
)

check_data >> delete_record >> updateSelectedTaskStatus 