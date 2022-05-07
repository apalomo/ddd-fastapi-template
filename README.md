# DDD TEMPLATE FAST-API

Simple template of a ddd project with api rest (fast-api) and database (postgres) in the infrastructure layer.

Basic tecnologies:
* python
* fastapi
* postgresql
* sqlalchemy
Devops to develoo:
* pytest
* pre-commit
* docker & docker-compose

## TO DEVELOP

- run database and server:

    `docker-compose up -d`

- Apply migrations

    `pdm run alembic_upgrade head`

- run test

    `pdm run test`

- for more details see the scripts section of `pyproject.toml`
