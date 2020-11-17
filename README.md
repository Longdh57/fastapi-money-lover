# Money Lover
A building frame for make app service use FastAPI
## Start app
`uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload`
## Migrations
#### Create migration versions
`alembic revision --autogenerate`
#### Upgrade head migration
`alembic upgrade head`

