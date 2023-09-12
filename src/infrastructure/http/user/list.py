"""Endpoints module."""

import typing

from src.domain.user.entity import User as UserD

from fastapi import Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide

from .router import router
from src.infrastructure.injections import Container
from src.application.user.get_users import GetUsers


class User(BaseModel):
    name: str


class Response(BaseModel):
    results: typing.List[User]


@router.get("/", response_model=Response)
@inject
def get_list(
        repo_users = Depends(Provide[Container.repo_users]),
):
    users: typing.List[UserD] = GetUsers(repo_users).execute()
    users_response = list(map(lambda user_d: User(name=user_d.name), users))
    return Response(results=users_response)