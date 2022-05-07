# DDD SKELETON FAST-API

Simple skeleton of a ddd project with api rest (fast-api) and database (postgres) in the infrastructure layer.

Basic tecnologies:
* python
* pdm
* fastapi
* postgresql
* sqlalchemy
Devops to develop:
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
