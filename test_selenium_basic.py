from pytest import mark

@mark.smoke
def test_home_page_loaded(chrome_browser):
    chrome_browser.get("https://the-internet.herokuapp.com/")
    title = chrome_browser.title
    print(title)
    assert "The Internet" in title
