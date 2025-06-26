## API do projeto Spotter.

Modos de execução:
- Para executar a API localmente, instale as dependências e execute: `uvicorn app.main:app --reload`
Dessa forma, garanta que no arquivo app/config/database.py, a string de conexão esteja configurada corretamente para o banco de dados em container:
`DATABASE_URL = DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/spotter"`

- Para executar a API em container localmente, faça o build da imagem com: `docker build -t spotter-backend .`
Dessa forma, a string de conexão com o banco é passada via variável de ambiente para o container, no comando:
`DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@host.docker.internal:5432/spotter_db")`

Para executar a aplicação (WSL):
`docker run --name spotter-api -p 8000:8000 --env DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/spotter spotter-backend`

Para executar a aplicação (Linux nativo):
`docker run --name spotter-api -p 8000:8000 --env DATABASE_URL=postgresql://postgres:postgres@172.17.0.1:5432/spotter_db spotter-backend`

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
`docker exec -i postgres-spotter psql -U postgres -d spotter < database.sql`

Para popular o banco com os mocks, utilize os endpoints de inserção em massa de funcionários, veículos e ocorrências **nessa ordem**, por conta das relações entre as entidades. Caso insira uma ocorrência que não tenha veículo, dará erro.

Acessar container do banco e entrar no postgres:
`docker exec -it postgres-spotter psql -U postgres -d spotter`
