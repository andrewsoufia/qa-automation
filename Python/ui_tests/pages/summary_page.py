


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SummaryPage:


    CancelBtn = (By.ID, "cancel")
    FinishBtn = (By.ID, "finish")
    Tax = (By.CLASS_NAME, "summary_tax_label")
    TotalItems = (By.CLASS_NAME, "summary_subtotal_label")
    TotalPrice = (By.CLASS_NAME, "summary_total_label")
    OrderStatus = (By.CLASS_NAME, "complete-header")

    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.FinishBtn))


    def finish_checkout(self):
        self.driver.find_element(*self.FinishBtn).click()

    def cancel_summary_checkout(self):
        self.driver.find_element(*self.CancelBtn).click()

    def get_order_status(self):
        text = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.OrderStatus)).text
        #print(f"summ: {text}")
        return text

    def get_checkout_information(self):
        tax = self.driver.find_element(*self.Tax).text
        subtotal = self.driver.find_element(*self.TotalItems).text
        totalPrice = self.driver.find_element(*self.TotalPrice).text
        return tax,subtotal,totalPrice