# TEMPLATE DDD FAST-API 

Simple template of a ddd project with api rest (fast-api) and database (postgres) in the infrastructure layer.

## TO DEVELOP

- run database and server:

    `docker-compose up -d`

- run migrations

    `pdm run alembic_upgrade head`

- run test

    `pdm run test`

- for more details see the scripts section of `pyproject.toml`

