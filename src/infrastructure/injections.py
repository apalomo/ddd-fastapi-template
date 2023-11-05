"""Containers module."""
import os
from dependency_injector import containers, providers
from src.infrastructure.database.repos.user import RepoUsers

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=[".http.user"])
    postgres_db = os.environ.get('POSTGRES_DB', '')
    engine_orm = providers.Factory(
        create_engine,
        postgres_db
    )
    session_orm = providers.Factory(
        Session,
        engine_orm
    )
    repo_users = providers.Singleton(
        RepoUsers,
        session_orm
    )
