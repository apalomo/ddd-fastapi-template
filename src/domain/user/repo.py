import typing
from abc import ABC, abstractmethod
from src.domain.user.entity import User

class RepoUsers(ABC):
    
    @abstractmethod
    def save(self, user: User) -> int:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> typing.List[User]:
        raise NotImplementedError