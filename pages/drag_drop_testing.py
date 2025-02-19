from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage

class DragDropTesting(BasePage):

    @property
    def drag_drop_link(self):
        locator = (By.CSS_SELECTOR, "a[href='/drag_and_drop']")
        return BaseElement(driver=self.driver, locator=locator) 
    
    @property
    def drag_drop_header(self):
        locator = (By.CSS_SELECTOR, ".example > h3")
        return BaseElement(driver=self.driver, locator=locator)
    
    @property
    def drag_and_drop_first_item(self):
        locator = (By.CSS_SELECTOR, "#column-a")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def drag_and_drop_second_item(self):
        locator = (By.CSS_SELECTOR, "#column-b")
        return BaseElement(driver=self.driver, locator=locator)
    