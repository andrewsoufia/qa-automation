



import pytest
from practice.cart import Cart


def test_cart_count(filled_cart):
    items_count = filled_cart.count()
    assert items_count == 3

def test_total_of_filled_cart(filled_cart):
    items_total = filled_cart.total()
    assert items_total == 49.97

def test_adding_same_item_twice(filled_cart):
    filled_cart.add("Backpack",29.99, 1)
    items_count = filled_cart.count()
    assert items_count == 4 #since now added new existing item


def test_removing_item(filled_cart):
    qty_removed = filled_cart.items["Backpack"]["qty"]
    filled_cart.remove("Backpack")
    assert filled_cart.count() == (3-qty_removed) #since 1 item was removed so must test if count qty is correct.


def test_adding_item_qty_0(filled_cart):
    
    pytest.raises(ValueError,filled_cart.add, "Pencil",2.99,0)


@pytest.mark.parametrize("percent,expected_total",[pytest.param(0,49.97,marks=pytest.mark.xfail(reason="Bug here: 0 is considered as invalid input due to condition error in cart.py::apply_discount")),
                                                   (10,44.97),
                                                   (50,24.98),
                                                   (100,0)],ids=["0%:","10%:","50%:","100%:"])
def test_discount_valid_percents(filled_cart,percent,expected_total):
    total_price = filled_cart.apply_discount(percent)
    assert total_price == expected_total



@pytest.mark.parametrize("percent",[-1,101],ids=["-1%:","101%:"])
def test_discount_invalid_percents(filled_cart,percent):
    pytest.raises(ValueError,filled_cart.apply_discount,percent)



def test_receipt(filled_cart,receipt_path):
    filled_cart.save_receipt(receipt_path)

    with open(receipt_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
        assert "TOTAL: 49.97" == content