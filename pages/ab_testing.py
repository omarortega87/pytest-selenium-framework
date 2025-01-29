from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class AB_TESTING(BasePage):

    @property
    def ab_testing_link(self):
        locator = Locator(by=By.CSS_SELECTOR, value="a[href='/abtest']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def ab_testing_header(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".example > h3")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )