from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Funções Python simulando atividades
def task_1_func():
    print("Executando Task 1")


def task_2_func():
    print("Executando Task 2")


def task_3_func():
    print("Executando Task 3")


def parallel_task_func():
    print("Executando Task Paralela")


# Definição da DAG
with DAG(
    dag_id="pipeline_sequencial_paralelo",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Executa somente manualmente
    catchup=False,
    tags=["exemplo", "teste", "pipeline"],
) as dag:

    # Tarefas sequenciais
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=task_1_func,
    )

    task_2 = PythonOperator(
        task_id="task_2",
        python_callable=task_2_func,
    )

    task_3 = PythonOperator(
        task_id="task_3",
        python_callable=task_3_func,
    )

    # Tarefa paralela com task_1
    parallel_task = PythonOperator(
        task_id="parallel_task",
        python_callable=parallel_task_func,
    )

    # Definindo dependências
    task_1 >> task_2 >> task_3
    task_1 >> parallel_task
