from selenium import webdriver

class Config:
    def __init__(self, browser):

        SUPPORTED_BROWSERS = ['chrome', 'firefox']

        if browser == None or browser.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f'{browser} please select a browser with the option --browser (supported browsers: {SUPPORTED_BROWSERS})')

        self.browser_type = {
                'chrome': 'chrome_browser',
                'firefox': 'firefox_browser'
        }[browser]

