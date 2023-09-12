import pytest
from src.application.user.create_user import CreateUser
from src.domain.user.repo import RepoUsers
from src.domain.user.entity import User

@pytest.fixture
def repo(mocker):
    repo = mocker.MagicMock(spec=RepoUsers)
    repo.save.return_value = 12
    return repo

def test_create_user(repo):
    user = User(name='name1', fullname='full', nickname='nick')
    res = CreateUser(repo).execute(user)
    assert res == 12
