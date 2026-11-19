
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CartLink = (By.CLASS_NAME, "shopping_cart_link")
    CartBadge = (By.CLASS_NAME, "shopping_cart_badge")
    Prices = (By.CLASS_NAME,"inventory_item_price")
    Filters = (By.CLASS_NAME, "product_sort_container")
    Item_Name = (By.CLASS_NAME, "inventory_details_name")
    Title = (By.CLASS_NAME, "title")

    InventoryList = (By.CLASS_NAME, "inventory_list")

    def __init__(self,driver):
        self.driver = driver
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.InventoryList))

    def itemName(self):
        return self.driver.find_element(*self.Item_Name).text

    def title(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.Title)).text
    
    
    def add_to_cart(self,item_id):
        self.driver.find_element(By.ID,item_id).click() #if id was the id of the button of that item needed

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CartBadge)) == 0
    
    def cart_count(self): #(with your explicit wait)
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.CartBadge)).text
    
    
    def open_item(self,name): # (XPath)
        self.driver.find_element(By.XPATH,"//div[text()='"+name+"']").click()

    
    def sort_by(self,option_text):
        Select(self.driver.find_element(*self.Filters)).select_by_visible_text(option_text)

    
    def prices(self): #(returns the list of floats).
        prices = self.driver.find_elements(*self.Prices)
        prices_reworked = []
        for x in prices: # loops on every price string in prices and converts them to float numbers
            prices_reworked.append(float(x.text.replace('$',"")))
        #print(prices_reworked) #checking if list is now replaced correctly
        return prices_reworked


    def go_to_cart(self):
        self.driver.find_element(*self.CartLink).click()