"""Containers module."""

from dependency_injector import containers, providers
from src.infrastructure.database.repos.user import RepoUsers

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=[".http.user"])

    engine_orm = providers.Factory(
        create_engine,
        "postgresql://user:password@localhost:5434/blog"
    )
    session_orm = providers.Factory(
        Session,
        engine_orm
    )
    repo_users = providers.Singleton(
        RepoUsers,
        session_orm
    )
