

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    text = driver.find_element(By.CLASS_NAME,"title").text
    assert text == "Products"


def test_locked_out_user_login(driver):
    driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    text = driver.find_element(By.CSS_SELECTOR,"[data-test = 'error']").text
    assert text == "Epic sadface: Sorry, this user has been locked out." # exact wording
    


def test_empty_username(driver):
    driver.find_element(By.ID,"user-name").clear() # clears the input field
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    text = driver.find_element(By.CSS_SELECTOR,"[data-test = 'error']").text
    assert "Username is required" in text # flexible wording


def test_wrong_password(driver):
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce1")
    driver.find_element(By.ID,"login-button").click()
    text = driver.find_element(By.CSS_SELECTOR,"[data-test = 'error']").text
    assert "Username and password do not match" in text


#code below combines all 3 functions above in 1 test with 1 more addition: Empty Password.
@pytest.mark.parametrize("username, password, expected",[("locked_out_user","secret_sauce","locked out"),
                                                          ("","secret_sauce", "Username is required"),
                                                          ("standard_user","secret_sauce1", "Username and password do not match"),
                                                          ("standard_user","", "Password is required")],
                                                          ids=["lockedOutUser","Empty Username","Wrong Password","Empty Password"])
def test_login_errors(driver,username,password,expected):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert expected in text



@pytest.mark.parametrize("username,password,expected",[("standard_user","secret_sauce", "Products"),
                                                       ("problem_user","secret_sauce", "Products"),
                                                       ("performance_glitch_user","secret_sauce", "Products"),
                                                       ("visual_user","secret_sauce", "Products"),
                                                       ("error_user","secret_sauce", "Products")],
                                                       ids=["StandardUser","ProblemUser",
                                                            "GlitchUser","VisualUser","ErrorUser"])
def test_valid_login_all_users(driver,username,password,expected):
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()

    text = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"title"))).text
    assert expected == text