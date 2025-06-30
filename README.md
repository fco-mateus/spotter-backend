
# API do projeto Spotter

Esse projeto é o back-end do projeto Spotter. Serve para comunicação entre front-end, OCR, S3 e banco de dados.

## Setup do ambiente (RDS e S3 em nuvem e API e OCR local)

- Baixe a [image da API](https://hub.docker.com/r/fcomateus1/spotter-backend) na versão 1.3.0, que está configurada para falar com RDS e S3.
- Baixe a [imagem do OCR](https://hub.docker.com/r/endmrf/ocr-license-plates).
- Crie uma rede virtual do Docker, por exemplo, `rede-spotter`, com o comando `docker network`. Tanto o container da API quando do OCR rodarão nessa rede. Esse passo é necessário para que os containers possam se enxergar pelo `nome do container` e, dessa forma, possam se falar.
- Baixe o [projeto Terraform](https://github.com/fco-mateus/spotter-infra) para provisionamento do RDS e S3 e **leia seu README**. Podem haver ajustes que devem ser feitos para configuração correta do ambiente.
- Acesse sua conta da AWS e crie um usuário com permissão para que o projeto Terraform possa provisionar a infraestrutura. Pode-se colocar a política _AdministratorAccess_ para configuração mais rápida. Crie as chaves de acesso desse usuário e configure no terminal que irá utilizar para criar a infraestrutura.
- Crie também um usuário para a **API**. Para configuração mais rápida, esse usuário pode ter as políticas _AmazonRDSFullAccess_ e _AmazonS3FullAccess_. Crie as chaves de acesso desse usuário e salve-as, pois você terá que configurá-la no **.env** desse projeto, para que o container possa interagir com a AWS.
- Provisione a infraestrutura com `terraform apply`
- Preencha as informações faltantes no **.env** com as informações da infraestrutura provisionada
- Execute a API com:
```
docker run --name spotter-backend-cloud -p 8000:8000 --env-file .env --network rede-spotter fcomateus1/spotter-backend:v1.3.0
```
- Execute o OCR com:
```
docker run --name ocr -p 5000:5000 --network rede-spotter endmrf/ocr-license-plates
```
OBS: O nome do container **deve** ser `ocr`, pois é como a **imagem da API** está configurada para chamar o container de OCR.
- Acesse `http://localhost:8000/docs` para ver o Swagger da API e testar os endpoints
OBS: Caso vá testar a detecção do OCR, use o endpoint `/easyocr`, pois tem mais chances de detecção.
- Acesse o banco de dados via algum cliente (CLI, DBeaver, PGAdmin...) e rode o script `database.sql` para inserir dados para teste.

Dessa forma, é possível configurar o ambiente para testar o OCR e a API com banco de dados e armazenamento de objetos na nuvem.
