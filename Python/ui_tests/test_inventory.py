


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC



def test_login_by_name(driver):
    driver.find_element(By.NAME,"user-name").send_keys("standard_user")
    driver.find_element(By.NAME,"password").send_keys("secret_sauce")
    driver.find_element(By.NAME,"login-button").click()
    text = driver.find_element(By.CLASS_NAME,"title").text
    assert text == "Products"


def test_add_backpack_to_cart(logged_in_as_standard):
    logged_in_as_standard.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    WebDriverWait(logged_in_as_standard,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
    
    badge_icon = logged_in_as_standard.find_element(By.CLASS_NAME,"shopping_cart_badge").text
    assert badge_icon == '1'


def test_open_item_by_name(logged_in_as_standard):
    logged_in_as_standard.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']").click()
    text = logged_in_as_standard.find_element(By.CLASS_NAME,"inventory_details_name").text
    assert text == "Sauce Labs Backpack"


def test_sort_low_to_high(logged_in_as_standard):
    Select(logged_in_as_standard.find_element(By.CLASS_NAME,"product_sort_container")).select_by_visible_text("Price (low to high)")
    prices = logged_in_as_standard.find_elements(By.CLASS_NAME,"inventory_item_price")
    prices_reworked = []
    for x in prices: # loops on every price string in prices and converts them to float numbers
        prices_reworked.append(float(x.text.replace('$',"")))
    print(prices_reworked) #checking if list is now replaced correctly
    assert  prices_reworked == sorted(prices_reworked) and len(prices_reworked) == 6 #should be equal if the sorting works
