# DDD FAST-API TEMPLATE

Template of a ddd project webserver.

It contains the user entity, two endpoints create and list, the use cases called by these endpoints and the tests of all these code.

Tecnologies:
* python
* fastapi
* postgresql
* sqlalchemy
* alembic
Devops to develop:
* pdm
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
