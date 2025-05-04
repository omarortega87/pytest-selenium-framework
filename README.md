# Python Selenium Project

This project follows the sequence of my blog site: [Omar Ortega Blog](https://omarortega.blog).

The main goal is to learn and create a *Pytest/Selenium* framework from scratch.

## Project Overview

This project is a Pytest/Selenium framework designed to Automat Web Application Test Scripts. It adheres to best practices such as:

- **Page Object Model (POM)**: Separates test logic from UI interactions.
- **Reusable Locators**: Ensures maintainability by defining locators as constants or properties.
- **Encapsulation**: Encapsulates element interactions within page classes.
- **Explicit Waits**: Handles dynamic elements effectively.
- **Data-Driven Testing**: Supports parameterized tests for running the same test with different data sets.
- **Cross-Browser Testing**: Ensures compatibility across multiple browsers.

### Key Features

- **BaseElement Class**: Encapsulates common actions like `click`, `send_keys`, and `get_text`.
- **BasePage Class**: Provides a foundation for all page classes.
- **CI/CD Integration**: Supports automated test execution using tools like GitHub Actions or Jenkins.
- **Reporting**: Generates detailed test reports using libraries pytest-html.

### Folder Structure

- **pages/**: Contains page classes following the Page Object Model.
- **tests/**: Includes test cases that utilize the page classes.
- **config.py**: Stores configuration settings for the framework.
- **conftest.py**: Contains fixtures and shared setup/teardown logic.

### Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   pytest --browser chrome --execution local 
   ```
