


from selenium.webdriver.common.by import By


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