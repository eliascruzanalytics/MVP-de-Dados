## Por que utilizar o DBeaver neste projeto?
<img width="669" height="367" alt="image" src="https://github.com/user-attachments/assets/34482fc0-003f-47ea-9932-5c1ac7e7d332" />

Embora seja possível consultar o PostgreSQL diretamente pelo terminal via **WSL** usando comandos como `psql`, neste projeto a utilização do **DBeaver** oferece uma experiência muito mais prática, visual e produtiva para análise e validação dos dados.

O **DBeaver** é uma ferramenta gráfica de administração e consulta a bancos de dados que facilita o trabalho durante o desenvolvimento do pipeline, especialmente em cenários locais com **Docker + Airflow + PostgreSQL**.

### Benefícios de utilizar o DBeaver em vez de consultas apenas via WSL/terminal


- **Interface visual amigável**  
  Permite navegar por schemas, tabelas, colunas e dados sem depender exclusivamente de comandos no terminal.

- **Validação mais rápida das cargas do pipeline**  
  Após a execução das DAGs, é possível conferir imediatamente se as tabelas foram criadas, se os registros foram inseridos e se os dados estão consistentes.

- **Facilidade para explorar dados**
  Visualizar resultados em formato tabular torna a análise muito mais intuitiva do que trabalhar apenas com retorno textual no `psql`.

- **Produtividade no desenvolvimento**
  Durante a construção de DAGs ETL, o DBeaver agiliza testes, inspeção de tabelas e execução de queries, reduzindo o tempo gasto com comandos repetitivos.

- **Melhor experiência para debugging**
  Quando ocorre algum erro de carga, fica mais simples verificar:
  - se a tabela foi criada
  - se o schema está correto
  - se houve inserção parcial
  - se os dados foram persistidos como esperado

- **Apoio à documentação e demonstração do projeto**
  Para projetos de portfólio e estudos, uma ferramenta visual como o DBeaver facilita a evidência dos resultados e torna a validação do pipeline mais acessível.

### Quando o terminal via WSL ainda é útil?

O uso do **WSL + `psql`** continua sendo importante para:

- validar conectividade rapidamente
- executar comandos administrativos simples
- automatizar verificações em ambiente local
- depurar containers e serviços

No entanto, para o dia a dia de desenvolvimento e análise do pipeline, o **DBeaver complementa o ambiente de forma mais eficiente**, oferecendo maior visibilidade e agilidade no acompanhamento das etapas de carga e transformação.

> Em resumo: o terminal via WSL é excelente para administração e troubleshooting, mas o DBeaver entrega uma camada visual que melhora significativamente a experiência de desenvolvimento, inspeção e validação dos dados no PostgreSQL.
