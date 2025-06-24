docker run --name postgres-spotter \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=spotter \
  -p 5432:5432 \
  -d postgres

docker exec -i postgres-spotter psql -U postgres -d spotter < database.sql

docker exec -it postgres-spotter psql -U postgres -d spotter
