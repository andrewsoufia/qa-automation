


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    firstname = (By.ID,"first-name")
    lastname = (By.ID,"last-name")
    postal = (By.ID,"postal-code")
    CancelBtn = (By.ID, "cancel")
    ContinueBtn = (By.ID, "continue")
    ErrorText = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.firstname))


    def go_to_summary_checkout(self,firstname, lastname, postal):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.postal).send_keys(postal)
        self.driver.find_element(*self.ContinueBtn).click()

    def cancel_checkout(self):
        self.driver.find_element(*self.CancelBtn).click()

    def get_error_text(self):
        #return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.ErrorText)).text
        return self.driver.find_element(*self.ErrorText).text