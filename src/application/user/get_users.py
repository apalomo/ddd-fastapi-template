import typing
import logging
from src.domain.user.entity import User
from src.domain.user.repo import RepoUsers

class GetUsers():
    def __init__(self, repo: RepoUsers, logger: logging.Logger = logging.getLogger()):
        self.repo: RepoUsers = repo
        self.logger = logger

    def execute(self) -> typing.List[User]:
        self.logger.info('[GetUsers] Starting to get users ')
        users = self.repo.list()
        self.logger.info(f'[GetUsers] Return {len(users)} users')
        return users