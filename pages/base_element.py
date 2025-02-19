from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        text = self.web_element.text
        return text

    def scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)
        return None
    
    def drag_and_drop(self, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.web_element, target.web_element).perform()
        return None
    
    def hover(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.web_element).perform()
        return None
    
    def is_displayed(self):
        return self.web_element.is_displayed()

    def is_enabled(self):
        return self.web_element.is_enabled()
    
    def is_selected(self):
        return self.web_element.is_selected()
    
    def clear(self):
        self.web_element.clear()
        return None
    
    def submit(self):
        self.web_element.submit()
        return None
    
    def get_css_value(self, prop):
        value = self.web_element.value_of_css_property(prop)
        return value
    
    def get_size(self):
        size = self.web_element.size
        return size

    def get_location(self):
        location = self.web_element.location
        return location 
    
    def get_tag_name(self):
        tag_name = self.web_element.tag_name
        return tag_name
    
    # Get the rectangle of the element
    def get_rect(self):
        rect = self.web_element.rect
        return rect
    
    def get_attribute(self, name):
        attribute = self.web_element.get_attribute(name)
        return attribute  # Return the attribute value
    
    def get_property(self, name):
        prop = self.web_element.get_property(name)
        return prop # Return the property value
    
    def get_text(self):
        text = self.web_element.text
        return text # Return the text of the element
   
    
   
