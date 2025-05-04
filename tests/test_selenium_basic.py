from pages.ab_testing import AB_TESTING
from pages.drag_drop_testing import DragDropTesting

def test_home_page_loaded(execution):

    training_page = AB_TESTING(driver=execution)
    training_page.go()
    training_page.ab_testing_link.click()
    header_text = training_page.ab_testing_header.text
    assert "A/B Test Control" in header_text

def test_drag_and_drop_page_loaded(execution):

    training_page = DragDropTesting(driver=execution)
    training_page.go()
    training_page.drag_drop_link.click()
    header_text = training_page.drag_drop_header.text
    assert "Drag and Drop" in header_text
    
    print("first item text: ", training_page.drag_and_drop_first_item.text)
    print("second item text: ", training_page.drag_and_drop_second_item.text)
    
    training_page.drag_and_drop_first_item.drag_and_drop(training_page.drag_and_drop_second_item)
    
    assert "B" in training_page.drag_and_drop_first_item.text  
    assert "A" in training_page.drag_and_drop_second_item.text

def test_checkboxes_page(execution):
    checkboxes_page = AB_TESTING(driver=execution)
    # Navigate to the site
    checkboxes_page.go()
    # Click on the Checkboxes link
    checkboxes_page.checkboxes_link.click()
    # Check the first checkbox and assert it is checked
    checkboxes_page.first_checkbox.click()
    assert checkboxes_page.first_checkbox.is_selected()
    # Uncheck the second checkbox and assert it is unchecked
    if checkboxes_page.second_checkbox.is_selected():
        checkboxes_page.second_checkbox.click()
    assert not checkboxes_page.second_checkbox.is_selected()

