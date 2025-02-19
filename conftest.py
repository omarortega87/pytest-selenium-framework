from pytest import fixture
from selenium import webdriver
from config import Config_browser
from config import Config_execution

def pytest_addoption(parser):
    parser.addoption(
            "--browser",
            action="store",
            help="browser to run the test against"
    ),
    parser.addoption(
            "--execution",
            action="store",
            help="execution type: local or grid"
    )

@fixture(scope="function")
def browser_type(request):
    return request.config.getoption("--browser")

@fixture(scope="function")
def execution_type(request):
    return request.config.getoption("--execution")

@fixture(scope='function')
def execution(execution_type, browser_type):
    cfg = Config_browser(browser_type).browser_type
    efg = Config_execution(execution_type).execution_type
    try:
        match efg:
            case "local":
                if cfg == "chrome_browser":
                    driver = webdriver.Chrome()
                elif cfg == "firefox_browser":
                    driver = webdriver.Firefox()
            case "grid":
                selenium_grid_config = {
                    'browserName': browser_type,
                }
                options = {
                    "chrome_browser": webdriver.ChromeOptions(),
                    "firefox_browser": webdriver.FirefoxOptions()
                }.get(cfg)
                driver = webdriver.Remote(
                    command_executor='http://localhost:4444',
                    options=options
                )
                print(options)
        yield driver
    finally:
        if driver:
            driver.quit()

