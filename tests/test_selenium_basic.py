import pytest
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

