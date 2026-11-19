

import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.summary_page import SummaryPage


def test_valid_checkout(logged_in_as_standard): #Full purchase: add 2 items, go all the way through, and check the confirmation says “Thank you for your order!”. Also check the cart is empty afterwards.
    

    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inv_page.add_to_cart("add-to-cart-test.allthethings()-t-shirt-(red)")
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_page.go_to_checkout()

    #now use checkout page to continue
    checkout_page = CheckoutPage(logged_in_as_standard)
    checkout_page.go_to_summary_checkout("test","user",1234)

    summary_page = SummaryPage(logged_in_as_standard)
    summary_page.finish_checkout()
    orderStatus = summary_page.get_order_status()
    assert ( orderStatus == "Thank you for your order!" )
    assert ( inv_page.is_cart_empty() )




@pytest.mark.parametrize("firstname,lastname,postal,expected",[("","User","1234","Error: First Name is required"),
                                                      ("Test","","1234","Error: Last Name is required"),
                                                      ("Test","User","","Error: Postal Code is required")],
                                                      ids=["empty firstname","empty lastname","empty postal code"])
def test_invalid_checkout_info(logged_in_as_standard,firstname,lastname,postal,expected):    # Required fields: one parametrized test, 3 cases. Leave first name, last name or postal code empty in turn, and check the exact error for each. Find the real messages manually first.
    
    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inv_page.add_to_cart("add-to-cart-test.allthethings()-t-shirt-(red)")
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_page.go_to_checkout()

    #now use checkout page to continue
    checkout_page = CheckoutPage(logged_in_as_standard)
    checkout_page.go_to_summary_checkout(firstname,lastname,postal)
    error_text = checkout_page.get_error_text()
    
    assert expected == error_text



def test_remove_item_in_cart_page(logged_in_as_standard): #Remove from cart: add 2 items, remove 1 on the cart page, check only the other is left and the badge updated.
    
    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inv_page.add_to_cart("add-to-cart-test.allthethings()-t-shirt-(red)")
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_page.remove_item("remove-test.allthethings()-t-shirt-(red)")
    cart_items = cart_page.get_items()
    #print(cart_items)
    assert inv_page.cart_count() == "1"
    assert ( cart_items == ["Sauce Labs Bolt T-Shirt"])


def test_total_price_with_tax(logged_in_as_standard): #Totals: with Backpack + Bike Light, check item total, tax and total on the overview against the spec, calculated in your test.
    
    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inv_page.add_to_cart("add-to-cart-sauce-labs-bike-light")
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_page.go_to_checkout()

    #now use checkout page to continue
    checkout_page = CheckoutPage(logged_in_as_standard)
    checkout_page.go_to_summary_checkout("test","user",1234)

    summary_page = SummaryPage(logged_in_as_standard)
    tax,itemsPrice, totalPrice = summary_page.get_checkout_information()

    backpack = 29.99
    bike_light = 9.99
    expected_items_price = float(round(backpack+bike_light,2))
    expected_tax = float(round((8*expected_items_price)/100,2))
    expected_total_price = float(round(expected_items_price + expected_tax,2))

    formatted_tax = float(tax.replace("Tax: $",""))
    formatted_items_price = float(itemsPrice.replace("Item total: $",""))
    formatted_total_price = float(totalPrice.replace("Total: $",""))
    assert formatted_tax == expected_tax
    assert formatted_items_price == expected_items_price
    assert formatted_total_price == expected_total_price


def test_saved_items_when_continue_shopping(logged_in_as_standard): #Continue shopping: from the cart, go back to Products and check the cart still holds your item.
    
    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inv_page.add_to_cart("add-to-cart-test.allthethings()-t-shirt-(red)")
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_items = cart_page.get_items()
    cart_page.continue_shopping()

    text = inv_page.title()

    assert ( len(cart_items) == int(inv_page.cart_count()) ) 
    assert ( text == "Products" ) # and also check the cart contents in local storage matches the cart items


#automated test for one of the bugs i found on saucedemo.com
@pytest.mark.xfail(reason="BUG-015 from the bug report: Checkout with an empty cart isnt being blocked")
def test_checkout_with_empty_cart(logged_in_as_standard):
    
    inv_page = InventoryPage(logged_in_as_standard)
    inv_page.go_to_cart()

    #now use cart page to continue from here
    cart_page = CartPage(logged_in_as_standard)
    cart_items = cart_page.get_items()
    
    assert len(cart_items) == 0
    cart_page.go_to_checkout()
    
    assert "cart.html" in logged_in_as_standard.current_url
    