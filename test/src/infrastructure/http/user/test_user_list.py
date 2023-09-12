import pytest
from src.infrastructure.http.user.list import get_list, Response, User as UserResponse
from src.domain.user.entity import User

@pytest.fixture
def get_users(mocker):
    return mocker.patch('src.infrastructure.http.user.list.GetUsers')


def test_get_list(get_users):
    get_users.return_value.execute.return_value = [
        User(name='name1', fullname='full1', nickname='nick1'),
        User(name='name2', fullname='full2', nickname='nick2'),
        User(name='name3', fullname='full3', nickname='nick3')
    ]
    res = get_list()
    assert res == Response(results=[
        UserResponse(name='name1'),
        UserResponse(name='name2'),
        UserResponse(name='name3'),
        ]
    )
