import logging
import typing
from domain.user.entity import User
from src.domain.user.repo import RepoUsers as RepoUsersAbc
from sqlalchemy.orm import Session
from src.infrastructure.database.models import User as UserDb


class RepoUsers(RepoUsersAbc):

    def __init__(self, session_orm: Session, logger: logging.Logger = logging.getLogger(__name__)):
        self.session_orm = session_orm

    def save(self, user: User) -> int:
        user_to_save: UserDb = UserDb(**user.model_dump())
        self.session_orm.add(user_to_save)
        self.session_orm.commit()
        self.session_orm.refresh(user_to_save)
        return user_to_save.id

    def list(self) -> typing.List[User]:
        users = self.session_orm.query(UserDb).all()
        users_domain: typing.List[User] = list(map(
            lambda user_db: User(
                name=user_db.name,
                fullname=user_db.fullname,
                nickname=user_db.nickname
            ),
            users
        ))
        return users_domain