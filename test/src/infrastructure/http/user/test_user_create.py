import pytest
from src.infrastructure.http.user.create import create, Response, Body
from src.domain.user.entity import User

@pytest.fixture
def create_user(mocker):
    return mocker.patch('src.infrastructure.http.user.create.CreateUser')


def test_create_user(create_user):
    create_user.return_value.execute.return_value = 1
    body = Body(name='name1', fullName='full1', nickName='nick1')
    res = create(body)

    create_user.return_value.execute.assert_called_with(
        User(name='name1', fullname='full1', nickname='nick1')
    )
    assert res == Response(id=1)
