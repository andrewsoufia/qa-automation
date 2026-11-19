



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    
    CheckoutBtn = (By.ID,"checkout")
    ShoppingBtn = (By.ID,"continue-shopping")
    Items = (By.CLASS_NAME, "inventory_item_name")


    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.CheckoutBtn))


    def get_items(self):
        self.items = [element.text for element in self.driver.find_elements(*self.Items)]
        return self.items


    def go_to_checkout(self):
        self.driver.find_element(*self.CheckoutBtn).click()


    def continue_shopping(self):
            self.driver.find_element(*self.ShoppingBtn).click()


    def remove_item(self, button_id):
        
        btn = self.driver.find_element(By.ID, button_id)        
        btn.click() #clicks the remove button of the item.