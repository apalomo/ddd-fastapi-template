import logging
from src.domain.user.entity import User
from src.domain.user.repo import RepoUsers

class CreateUser():
    def __init__(self, repo: RepoUsers, logger: logging.Logger = logging.getLogger()):
        self.repo: RepoUsers = repo
        self.logger = logger

    def execute(self, user: User) -> int:
        self.logger.info('[CreateUser] Starting to create user ')
        id = self.repo.save(user)
        self.logger.info(f'[CreateUser] User created with id {id}')
        return id