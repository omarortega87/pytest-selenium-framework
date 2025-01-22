from pytest import fixture
from selenium import webdriver
from config import Config

def pytest_addoption(parser):
    parser.addoption(
            "--browser",
            action="store",
            help="browser to run the test against"
    )

@fixture(scope="function")
def browser_type(request):
    return request.config.getoption("--browser")

@fixture(scope='function')
def browser(browser_type):
    cfg = Config(browser_type).browser_type
    match cfg:
        case "chrome_browser":
            return webdriver.Chrome()
        case "firefox_browser":
            return webdriver.Firefox()
