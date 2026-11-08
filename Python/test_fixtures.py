


def test_change_price(booking):
    booking["totalprice"] = 0
    assert booking["totalprice"] == 0


def test_price_unchanged(booking):
    assert booking["totalprice"] == 911



def test_append_table(cart):
    cart.append("table")
    assert len(cart) == 1


def test_append_pencil(cart):
    cart.append("pencil")
    assert len(cart) == 1