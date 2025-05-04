# Best Practices for Selenium

## General Best Practices
1. **Use Explicit Waits**: Always use explicit waits to handle dynamic elements instead of hardcoded sleep statements.
2. **Page Object Model (POM)**: Implement the Page Object Model to separate test logic from UI interactions.
3. **Reusable Locators**: Define locators as constants or properties to avoid duplication.
4. **Encapsulation**: Encapsulate element interactions (e.g., click, send_keys) within page classes.
5. **Error Handling**: Use try-except blocks to handle exceptions gracefully and log meaningful error messages.
6. **Headless Mode**: Use headless mode for faster execution in CI/CD pipelines.
7. **Cross-Browser Testing**: Test on multiple browsers to ensure compatibility.
8. **Data-Driven Testing**: Use parameterized tests to run the same test with different data sets.
9. **Logging**: Implement logging to capture test execution details.
10. **Assertions**: Use meaningful assertions to validate test outcomes.

## BaseElement Class Implementation
- The `BaseElement` class should encapsulate common actions like `click`, `send_keys`, `get_text`, etc.
- Every page class must use the `BaseElement` class for element interactions.

## Page Class Implementation
- All page classes must extend the `BasePage` class.
- Define locators as properties using the following structure:

```python
@property
def example_element(self):
    locator = (By.CSS_SELECTOR, "css_selector_here")
    return BaseElement(driver=self.driver, locator=locator)
```

- Example:

```python
from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage

class ExamplePage(BasePage):

    @property
    def example_link(self):
        locator = (By.CSS_SELECTOR, "a[href='/example']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def example_header(self):
        locator = (By.CSS_SELECTOR, ".example > h3")
        return BaseElement(driver=self.driver, locator=locator)
```

## Test Implementation
- Use the page classes to encapsulate test logic.
- Add the `execution` argument to every test method to pass the WebDriver instance.
- Example:

```python
def test_example(execution):
    driver = execution
    example_page = ExamplePage(driver)

    example_page.go("https://example.com")
    example_page.example_link.click()
    assert "Expected Text" in example_page.example_header.text
```

## CI/CD Integration
- Use tools like GitHub Actions or Jenkins to automate test execution.
- Run tests in parallel to reduce execution time.
- Generate and store test reports for analysis.

## Reporting
- Use libraries like Allure or pytest-html to generate detailed test reports.

## Maintenance
- Regularly update locators to match UI changes.
- Refactor code to remove redundancy and improve readability.