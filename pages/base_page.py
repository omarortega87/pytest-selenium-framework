class BasePage(object):
    url = 'https://the-internet.herokuapp.com/'
    
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
