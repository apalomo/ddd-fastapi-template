import pytest
import logging
from sqlalchemy.orm import Session
from src.infrastructure.database.repos.user import RepoUsers
from src.infrastructure.database.models import User as UserDb
from domain.user.entity import User


@pytest.fixture
def session_orm(mocker):
    return mocker.MagicMock(spec=Session)


@pytest.fixture
def logger(mocker):
    return mocker.MagicMock(spec=logging.Logger)


@pytest.fixture
def repo(session_orm, logger):
    return RepoUsers(session_orm, logger)

@pytest.fixture
def user():
    return User(name='name', fullname='full', nickname='nicky')


@pytest.fixture
def user_db(mocker):
    return mocker.patch('src.infrastructure.database.repos.user.UserDb', spec=UserDb)


def test_save(repo, user, user_db):
    
    res = repo.save(user)

    user_db.assert_called_with(**user.model_dump())
    repo.session_orm.add.assert_called_with(user_db.return_value)
    repo.session_orm.commit.assert_called_once()
    repo.session_orm.refresh.assert_called_with(user_db.return_value)
    
    assert res == user_db.return_value.id


def test_list(repo, user, user_db):
    repo.session_orm.query.return_value.all.return_value = [user]

    res = repo.list()

    repo.session_orm.query.return_value.all.assert_called_once()

    assert res == [user]
