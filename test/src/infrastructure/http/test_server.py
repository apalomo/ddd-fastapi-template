import pytest
from src.infrastructure.http.server import create_app


@pytest.fixture
def container(mocker):
    return mocker.patch('src.infrastructure.http.server.Container')


@pytest.fixture
def router(mocker):
    return mocker.patch('src.infrastructure.http.server.router')


@pytest.fixture
def fast_api(mocker):
    return mocker.patch('src.infrastructure.http.server.FastAPI')


def test_create_app(fast_api, container, router):
    res = create_app()

    fast_api.assert_called_once()
    fast_api.return_value.include_router.assert_called_with(router.router)
    assert res == fast_api.return_value
