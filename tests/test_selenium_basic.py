from pages.ab_testing import AB_TESTING

def test_home_page_loaded(browser):

    training_page = AB_TESTING(driver=browser)
    training_page.go()
    training_page.ab_testing_link.click()
    header_text = training_page.ab_testing_header.text
    assert "A/B Test Control" in header_text
