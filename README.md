# <p align="center">MVP-de-Dados </p>
# <p align="left">📌 #1 Contexto (problema real) </p>
<img width="876" height="528" alt="image" src="https://github.com/user-attachments/assets/c130863a-f77c-47c7-b8c3-a0b94cdd9a39" />

Tenho visto muita discussão sobre stacks completas de dados, arquiteturas complexas e soluções “enterprise”.

Mas pouca conversa honesta sobre MVPs reais de dados.

MVP no sentido literal:   
👉 o mínimo viável para gerar valor   
👉 simples de operar   
👉 fácil de evoluir   

Resolvi então construir um MVP de dados do zero, com foco em problemas comuns do dia a dia:   

• ingestão de arquivos (CSV)   
• ingestão via API   
• uma transformação essencial   
• e orquestração simples, sem overengineering

Não é um projeto de portfólio.   
É um exercício prático para responder uma pergunta que aparece em quase toda empresa:   

“Qual é o menor caminho entre dados brutos e valor?”   

Vou compartilhar esse MVP em partes por aqui, explicando as decisões, os trade-offs e, principalmente, o que ficou de fora de propósito.

O código vai sendo versionado publicamente no GitHub conforme a série evolui.

Se você trabalha com engenharia de dados, arquitetura ou está começando um time do zero, talvez isso te ajude.

✍️ Nos próximos posts, começo pela arquitetura do MVP.

# <p align="left">📌 #2 Arquitetura do MVP </p>

<img width="898" height="619" alt="image" src="https://github.com/user-attachments/assets/5e901bd5-085f-4d35-a4c3-3137d802bf23" />


Dando sequência ao MVP de dados que comentei no post anterior, comecei pela arquitetura.

Antes de pensar em ferramenta, pensei nos objetivos.

Esse MVP tem 3 objetivos claros:

1️⃣ Ingestão simples   
Porque, na prática, a maioria dos problemas começa aqui.   
CSV e API ainda são o padrão no mundo real.

2️⃣ Observabilidade básica   
Não faz sentido ingerir dados sem saber:   

• quando rodou   
• se falhou   
• qual volume foi processado   

Não é observabilidade enterprise — é o mínimo funcional.

3️⃣ Facilidade de evolução   
Esse ponto é crítico.   
O MVP precisa permitir crescer sem reescrever tudo:   

• novas fontes   
• novas transformações   
• novas regras   

A imagem acima mostra a arquitetura em alto nível, propositalmente simples.   

Não é sobre usar todas as ferramentas possíveis.   
É sobre reduzir o caminho entre dados brutos e valor.   

Este repositório está público e vai evoluir junto com essa série.   

✍️ Nos próximos posts, entro no primeiro cenário de ingestão: arquivos CSV — e por que eles continuam sendo onipresentes em pipelines de dados.

# <p align="left">📌 #3 — Ingestão CSV (o cenário mais comum) </p>

<img width="938" height="532" alt="image" src="https://github.com/user-attachments/assets/8730ebee-e691-46c7-9e4d-e951ab631f32" />

👉 Antes de iniciar, ajuste seu ambiente...leia o arquivo https://github.com/eliascruzanalytics/MVP-de-Dados/blob/main/install_airflow_%2B_docker.md   
   
Comecei o MVP pelo cenário mais comum no mundo real: arquivos CSV.

CSV não é moderno.  
CSV não é bonito.  
Mas CSV continua dominando pipelines de dados.  

E por alguns motivos bem práticos:  

• é simples de gerar  
• é fácil de compartilhar
• funciona em qualquer stack
• normalmente é o primeiro formato quando um processo nasce  

Justamente por isso, a ingestão de CSV costuma ser onde os problemas aparecem primeiro.  

Nesse MVP, tratei CSV com algumas premissas claras:  

1️⃣ Validação mínima de schema  
Antes de qualquer transformação, valido:  

• existência de colunas esperadas  
• tipos básicos (quando aplicável)
• volume de registros

Não é validação pesada.  
É o suficiente para não propagar erro silencioso.  
 
2️⃣ Separação clara entre ingestão e transformação  
O CSV entra “como veio”.  
Regras de negócio ficam fora da ingestão.  

Isso facilita debug, reprocessamento e evolução.  

3️⃣ Falha explícita  
Se o arquivo não atende ao mínimo esperado, o pipeline falha.  

Prefiro falhar cedo do que corrigir dados errados depois.  

<img width="995" height="886" alt="image" src="https://github.com/user-attachments/assets/de59ef17-9add-44af-b5a7-335850366306" />


   
✍️ Nos próximos posts, entro no segundo cenário: ingestão via API e ajuste do DBEAVER para facilitar o acesso ao dado...até lá! 😄


