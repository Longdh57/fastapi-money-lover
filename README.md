# Money Couple
A building frame for make app service use FastAPI
## Start app
`uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload`
## Migrations
#### Create migration versions
`alembic revision --autogenerate`
#### Upgrade head migration
`alembic upgrade head`
## Docker
#### Build image
`docker build -t money-lover .`
#### Run docker with uvicorn
`docker run -it --name money-lover -p 8080:8080 --network="host" money-lover:latest`
or `docker run -d --name money-lover -p 8080:8080 money-lover:latest`

