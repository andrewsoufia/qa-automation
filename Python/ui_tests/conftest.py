
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")



@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if (browser == "edge"):
        driver = webdriver.Edge()
    elif (browser == "firefox"):
        driver = webdriver.Firefox()
    elif (browser == "chrome"):
        driver = webdriver.Chrome()
    else:
        raise ValueError("ERROR invalid browser name..")
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