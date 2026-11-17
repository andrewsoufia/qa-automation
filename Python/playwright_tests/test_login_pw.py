

from playwright.sync_api import Page, expect
import pytest


def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator(".title")).to_have_text("Products")




def test_add_backpack_to_cart(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator("#add-to-cart-sauce-labs-backpack").click()
    
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_sort_low_to_high(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator("select.product_sort_container").select_option("lohi") #selected low to high option.

    prices = page.locator(".inventory_item_price").all_inner_texts()

    prices_reworked = []

    for pr in prices:
        prices_reworked.append(float(pr.replace("$","")))
        #print(pr , " || reworked: " , prices_reworked)

    assert prices_reworked == sorted(prices_reworked) and len(prices_reworked) == 6 #should be equal if the sorting works



# function written as POM below.
#code below combines all 3 functions above in 1 test with 1 more addition: Empty Password.
@pytest.mark.parametrize("username, password, expected",[("locked_out_user","secret_sauce","locked out"),
                                                          ("","secret_sauce", "Username is required"),
                                                          ("standard_user","secret_sauce1", "Username and password do not match"),
                                                          ("standard_user","", "Password is required")],
                                                          ids=["lockedOutUser","Empty Username","Wrong Password","Empty Password"])
def test_login_errors(page: Page,username,password,expected):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_contain_text(expected)



# @pytest.mark.parametrize("username,password,expected",[("standard_user","secret_sauce", "Products"),
#                                                        ("problem_user","secret_sauce", "Products"),
#                                                        ("performance_glitch_user","secret_sauce", "Products"),
#                                                        ("visual_user","secret_sauce", "Products"),
#                                                        ("error_user","secret_sauce", "Products")],
#                                                        ids=["StandardUser","ProblemUser",
#                                                             "GlitchUser","VisualUser","ErrorUser"])
# def test_valid_login_all_users(driver,username,password,expected):
#     page = LoginPage(driver)
#     page.login(username,password)
#     inv_page = InventoryPage(driver)
#     text = inv_page.title()
#     assert expected == text