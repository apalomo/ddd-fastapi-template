from src.infrastructure.server import read_root, read_item


def test_read_root():
    res = read_root()
    assert res == {"Hello": "World"}


def test_read_item():
    res = read_item(1)
    assert res == {"item_id": 1, "q": None}


def test_read_item_with_q():
    res = read_item(1, 'two')
    assert res == {"item_id": 1, "q": 'two'}
