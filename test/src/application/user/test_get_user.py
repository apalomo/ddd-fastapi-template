import pytest
from src.application.user.get_users import GetUsers
from src.domain.user.repo import RepoUsers
from src.domain.user.entity import User

@pytest.fixture
def repo(mocker):
    repo = mocker.MagicMock(spec=RepoUsers)
    repo.list.return_value = []
    return repo

def test_get_user__empty(repo):
    user = User(name='name1', fullname='full', nickname='nick')
    res = GetUsers(repo).execute()
    assert res == []


def test_get_user__with_data(repo):
    user = User(name='name1', fullname='full', nickname='nick')
    repo.list.return_value = [user]
    res = GetUsers(repo).execute()
    assert res == repo.list.return_value
