# ~/data-pipeline-mvp/dags/mvp_etl.py

# Importações do Airflow e operadores
from airflow import DAG  # Classe para criar uma DAG (workflow)
from airflow.operators.python import PythonOperator  # Operador para executar funções Python
from datetime import datetime  # Para definir datas de início da DAG
import pandas as pd  # Para manipulação de dados (DataFrame)
import psycopg2  # Para conexão com PostgreSQL
import os  # Para acessar variáveis de ambiente

# ===============================
# Configurações de conexão com Postgres
# ===============================
# Define host, banco, usuário e senha via variáveis de ambiente ou valores padrão
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "airflow")
POSTGRES_USER = os.getenv("POSTGRES_USER", "airflow")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "airflow123")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

# Caminho do arquivo CSV de entrada
DATA_FILE = "/opt/airflow/data/clientes.csv"

# ===============================
# Função extract: lê CSV e salva em pickle
# ===============================
def extract():
    df = pd.read_csv(DATA_FILE)  # Lê CSV com pandas
    df.to_pickle("/opt/airflow/data/extracted.pkl")  # Salva DataFrame em pickle (arquivo binário)
    print("Extraído com sucesso!")

# ===============================
# Função transform: lê pickle, aplica transformação e salva novamente
# ===============================
def transform():
    df = pd.read_pickle("/opt/airflow/data/extracted.pkl")  # Lê pickle criado na etapa extract
    # Filtra apenas emails que contêm "@example.com"
    df = df[df['email'].str.contains("@example.com")]
    df.to_pickle("/opt/airflow/data/transformed.pkl")  # Salva pickle transformado
    print("Transformado com sucesso!")

# ===============================
# Função load: carrega dados transformados no Postgres
# ===============================
def load():
    df = pd.read_pickle("/opt/airflow/data/transformed.pkl")  # Lê pickle transformado
    # Conecta ao Postgres usando psycopg2
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT
    )
    cur = conn.cursor()
    # Cria a tabela 'clientes' se ainda não existir
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT PRIMARY KEY,
            nome TEXT,
            email TEXT
        )
    """)
    conn.commit()

    # Insere dados linha a linha
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO clientes (id, nome, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO UPDATE  -- Se o id já existir, atualiza nome e email
            SET nome = EXCLUDED.nome,
                email = EXCLUDED.email
        """, (row['id'], row['nome'], row['email']))
    conn.commit()  # Confirma alterações no banco
    cur.close()
    conn.close()
    print("Carregado no Postgres com sucesso!")

# ===============================
# Definição da DAG
# ===============================
with DAG(
    'mvp_etl',                 # Nome da DAG
    start_date=datetime(2026, 1, 19),  # Data de início da DAG
    schedule_interval=None,     # Sem agendamento automático (manual)
    catchup=False               # Não processar datas passadas
) as dag:

    # ===============================
    # Definição das tasks
    # ===============================
    t1 = PythonOperator(task_id='extract', python_callable=extract)  # Task extract
    t2 = PythonOperator(task_id='transform', python_callable=transform)  # Task transform
    t3 = PythonOperator(task_id='load', python_callable=load)  # Task load

    # Define a ordem de execução: extract → transform → load
    t1 >> t2 >> t3


