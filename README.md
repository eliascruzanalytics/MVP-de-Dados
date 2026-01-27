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

No próximo post, entro no primeiro cenário de ingestão: arquivos CSV — e por que eles continuam sendo onipresentes em pipelines de dados.
