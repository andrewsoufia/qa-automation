

import pytest
import os
from practice.cart import Cart

@pytest.fixture
def empty_cart(): 
    cart = Cart()
    return cart


@pytest.fixture 
def filled_cart(empty_cart):
    empty_cart.add("Backpack",29.99, 1)
    empty_cart.add("Bike Light",9.99, 2)
    return empty_cart


@pytest.fixture
def receipt_path():
    path = "./fileReceipt.txt"
    yield path

    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")