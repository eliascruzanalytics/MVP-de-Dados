# MVP de Pipeline de Dados — Airflow com Docker

Este repositório contém um **MVP de pipeline de dados** utilizando a arquitetura  
**Bronze → Silver → Gold**, orquestrado com **Apache Airflow**, rodando localmente via **Docker**.

O objetivo é demonstrar:

- ingestão real de dados públicos (CSV)
- separação clara de responsabilidades
- falha explícita
- pipeline simples e evolutivo

---

## 📋 Pré-requisitos

Antes de tudo, você precisa ter instalado na sua máquina:

### ✅ 1. Usando Windows com WSL (recomendado)  
Este projeto foi testado utilizando WSL (Windows Subsystem for Linux), que é a forma mais estável de rodar Docker + Airflow no Windows.  

✅ Pré-requisitos adicionais no Windows

Você precisa ter:

WSL 2 instalado

Docker Desktop configurado para usar WSL

📌 Se você já instalou o Docker Desktop normalmente, provavelmente o WSL já está ativo.
Para confirmar, execute no PowerShell:   

```
wsl --list --verbose

```
Você deve ver algo como:   

```
NAME            STATE   VERSION
Ubuntu          Running 2

```

### ✅ 2. Docker Desktop

Windows / Mac:  
👉 https://www.docker.com/products/docker-desktop/

Após instalar:

- abra o Docker Desktop
- aguarde até aparecer **“Docker is running”**

💡 **No Windows**, o Docker usa WSL automaticamente  
(não é necessário configurar manualmente).

---

## 📥 Clonar ou baixar o projeto

### Opção B — Download ZIP

1. Clique em **Code → Download ZIP**
2. Extraia o arquivo
3. Abra a pasta extraída

---

## 📁 Estrutura do projeto

```text
MVP-de-Dados/
├── dags/            # DAGs do Airflow
├── docker/          # docker-compose.yml
├── data/            # Camadas Bronze e Silver (arquivos gerados)
├── docs/            # Documentação e posts da série
├── README.md
├── requirements.txt
└── .gitignore
```

## 🐳 Subindo o Airflow com Docker

1️⃣ Acesse a pasta correta  

No terminal (PowerShell ou Prompt de Comando):  
```
cd docker  
```

1️⃣ Acesse a pasta correta  

No terminal (PowerShell ou Prompt de Comando):  
```
cd docker  
```
2️⃣ Suba os containers

No terminal (PowerShell ou Prompt de Comando):  
```
docker-compose up -d
```

Na primeira vez, isso pode demorar alguns minutos  
(Docker irá baixar as imagens do Airflow e do Postgres).  

Se tudo der certo, você verá algo como:  
```
Creating airflow-webserver ... done
Creating airflow-scheduler ... done
Creating postgres ... done

```

3️⃣ Verifique se os containers estão rodando    

```
docker ps

```
Você deve ver os containers do Airflow e do Postgres ativos.   


🌐 Acessando o Airflow  
Abra o navegador e acesse:   

```
http://localhost:8080

```
Credenciais padrão  

Usuário: airflow  
Senha: airflow123  

 



