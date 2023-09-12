"""Endpoints module."""
from fastapi import Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide

from .router import router
from src.infrastructure.injections import Container
from src.application.user.create_user import CreateUser
from src.domain.user.entity import User

class Response(BaseModel):
    id: int

class Body(BaseModel):
    name: str
    fullName: str
    nickName: str

    def to_domain(self) -> User:
        return User(
            name=self.name,
            fullname=self.fullName,
            nickname=self.nickName
        )

@router.post("/", response_model=Response)
@inject
def create(
    body: Body,
    repo_users = Depends(Provide[Container.repo_users]),
):
    user_id: int = CreateUser(repo_users).execute(body.to_domain())
    return Response(id=user_id)