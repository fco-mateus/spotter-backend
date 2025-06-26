## API do projeto Spotter.

Para executar a API localmente, instale as dependências e execute: uvicorn app.main:app --reload

Veja o Swagger da API em /docs.

Para testar localmente, rode o banco e popule um banco localmente com os seguintes comandos:

Rodar o container do banco:
docker run --name postgres-spotter \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=spotter \
  -p 5432:5432 \
  -d postgres

Script de criação de tabelas do banco:
docker exec -i postgres-spotter psql -U postgres -d spotter < database.sql

Para popular o banco com os mocks, utilize os endpoints de inserção em massa de funcionários, veículos e ocorrências **nessa ordem**, por conta das relações entre as entidades. Caso insira uma ocorrência que não tenha veículo, dará erro.

Acessar container do banco e entrar no postgres:
docker exec -it postgres-spotter psql -U postgres -d spotter
