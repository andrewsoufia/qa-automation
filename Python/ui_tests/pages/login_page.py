

import pytest
from selenium.webdriver.common.by import By

class LoginPage:

    Username = (By.ID,"user-name")
    Password = (By.ID, "password")
    LoginButton = (By.ID, "login-button")
    Error = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(*self.Username).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.LoginButton).click()


    def error_text(self):
        return self.driver.find_element(*self.Error).text

