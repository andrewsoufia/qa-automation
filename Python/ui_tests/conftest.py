
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


# Rewrote the fixture below using POM
@pytest.fixture
def logged_in_as_standard(driver):
    page = LoginPage(driver)
    page.login("standard_user","secret_sauce")
    return driver

# @pytest.fixture
# def logged_in_as_standard(driver):
#     driver.find_element(By.ID,"user-name").send_keys("standard_user")
#     driver.find_element(By.ID,"password").send_keys("secret_sauce")
#     driver.find_element(By.ID,"login-button").click()
#     return driver