from selenium import webdriver


def test_home_page_loaded():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title
    print(title)
    assert "The Internet" in title
