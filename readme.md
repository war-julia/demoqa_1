# DemoQA Test Automation Framework

This project contains automated tests for the DemoQA website using Selenium WebDriver and Python.

## Project Structure

```
demoqa/
├── components/
│   └── components.py          # WebElement wrapper class
├── pages/
│   ├── base_page.py          # Base page object
│   ├── demoqa.py             # DemoQA main page
│   └── elements_page.py      # Elements page
├── tests/
│   ├── test_check_icon_demoqa.py
│   └── test_go_to_page_elements.py
├── conftest.py               # Pytest configuration
├── requirements.txt          # Python dependencies
└── chromedriver.exe         # Chrome WebDriver
```

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Chrome browser is installed

3. Make sure `chromedriver.exe` is in the project root directory

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_check_icon_demoqa.py
```

Run with verbose output:
```bash
pytest -v
```

## Test Cases

### test_check_icon_demoqa.py
- Tests that the DemoQA logo icon exists and is clickable
- Verifies the icon click doesn't navigate away from the page

### test_go_to_page_elements.py
- Tests navigation from main page to Elements page
- Verifies proper URL changes after navigation

## Framework Features

- **Page Object Model**: Organized page classes for better maintainability
- **WebElement Wrapper**: Custom WebElement class with timeout handling
- **Explicit Waits**: Proper element waiting with WebDriverWait
- **Error Handling**: Comprehensive exception handling for element interactions
- **Pytest Integration**: Full pytest framework integration with fixtures

## Key Components

### BasePage
- Common methods for all pages
- URL management and navigation
- Base URL validation

### WebElement
- Wrapper around Selenium WebElement
- Built-in timeout handling
- Explicit wait implementation
- Better error messages

### DemoQa Page
- Main page elements and interactions
- Icon verification methods
- Navigation to sub-pages

### ElementsPage
- Elements page specific functionality
- Page-specific element locators

## Browser Configuration

The framework uses Chrome WebDriver with optimized settings:
- No sandbox mode for stability
- Disabled GPU for headless compatibility
- Implicit wait of 10 seconds
- Maximized window for consistent testing
