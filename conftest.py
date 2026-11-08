

import pytest


@pytest.fixture
def booking():
    return {"firstname": "Test",
            "lastname": "User",
            "totalprice": 911}


@pytest.fixture
def cart():
    items = []
    print("cart ready for items")
    yield items
    print("cart now empty")
    items.clear()