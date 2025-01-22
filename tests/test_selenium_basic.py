def test_home_page_loaded(browser):
    browser.get("https://the-internet.herokuapp.com/")
    title = browser.title
    print(title)
    assert "The Internet" in title
