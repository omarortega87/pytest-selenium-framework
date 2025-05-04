from selenium import webdriver

class Config_browser:
    def __init__(self, browser):

        SUPPORTED_BROWSERS = ['chrome', 'firefox']

        if browser == None or browser.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f'{browser} please select a browser with the option --browser (supported browsers: {SUPPORTED_BROWSERS})')

        self.browser_type = {
                'chrome': 'chrome_browser',
                'firefox': 'firefox_browser'
        }[browser]

class Config_execution:
    def __init__(self, execution):

        SUPPORTED_EXECUTORS = ['local', 'grid']

        if execution == None or execution.lower() not in SUPPORTED_EXECUTORS:
            raise Exception(f'{execution} please select an option from the Supported Executors with the option --execution (supported executors: {SUPPORTED_EXECUTORS})')


        self.execution_type = {
                'grid': 'grid',
                'local': 'local'
        }[execution]

