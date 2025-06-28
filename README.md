## API do projeto Spotter.

Esse projeto é o back-end do projeto Spotter. Serve para comunicação entre front-end, OCR, S3 e banco de dados.

### Modos de execução:
- Para executar a API localmente, instale as dependências e execute: `uvicorn app.main:app --reload`
Dessa forma, garanta que no arquivo app/config/database.py, a string de conexão esteja configurada corretamente para o banco de dados em container:
`DATABASE_URL = DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/spotter"`

Altere também a comunicação com o container de OCR, caso rode essa API sem estar em container.

- Para executar a API em container localmente, faça o build da imagem com: `docker build -t spotter-backend .` ou baixe a imagem do Dockerhub `fcomateus1/spotter-backend`.
Dessa forma, a string de conexão com o banco é passada via variável de ambiente para o container, no comando:
`DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres-spotter:5432/spotter")`.
Lembre-se de colocar o nome do container de banco exatamente como está na string, para que a conexão seja possível.

OBS: Para rodar a API, banco de dados e container de OCR todos se enxergando pelo __nome do container__, é **necessário** criar uma rede personalizada no Docker com `docker network create <nome_da_rede>` e lançar os containers todos nessa rede, com o parâmetro `--network <nome_da_rede>` no comando `docker run`.

### Iniciando container da aplicação

Para executar a aplicação:
`docker run --name spotter-backend -p 8000:8000 --env DATABASE_URL=postgresql://postgres:postgres@postgres-spotter:5432/spotter --network rede-spotter spotter-backend`

Veja o Swagger da API em /docs.

Para testar localmente, rode o banco e popule um banco localmente com os seguintes comandos:

### Iniciando container do banco de dados local para teste
Rodar o container do banco:
docker run --name postgres-spotter --network rede-spotter \
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

### Rodando o ambiente integrado
Execute a aplicação de OCR na mesma rede, fazendo o bind da porta 5000 do container para a porta 5000 do host e dê o nome do container de __ocr__, pois essa aplicação está configurada para interagir com o container de OCR. Algo como:

`docker run --name ocr -p 5000:5000 --network rede-spotter endmrf/ocr-license-plates`
