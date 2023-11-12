"""Containers module."""
import os
from dependency_injector import containers, providers
from src.infrastructure.database.repos.user import RepoUsers

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[".http.user"])
    postgres_host = os.environ.get("POSTGRES_HOST", "")
    postgres_port = os.environ.get("POSTGRES_PORT", "")
    postgres_user = os.environ.get("POSTGRES_USER", "")
    postgres_password = os.environ.get("POSTGRES_PASSWORD", "")
    postgres_db = os.environ.get("POSTGRES_DB", "")
    if not all(
        [postgres_host, postgres_port, postgres_user, postgres_password, postgres_db]
    ):
        raise Exception("Bad config")

    postgres_uri = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    engine_orm = providers.Factory(create_engine, postgres_uri)
    session_orm = providers.Factory(Session, engine_orm)
    repo_users = providers.Singleton(RepoUsers, session_orm)
