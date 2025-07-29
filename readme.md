# Sauce Demo Test Automation Framework

This project contains automated tests for the [Sauce Demo](https://www.saucedemo.com/) website using Selenium WebDriver and Python.

## Project Structure

```
demoqa/
├── components/
│   └── components.py          # WebElement wrapper class
├── pages/
│   ├── base_page.py          # Base page object
│   ├── demoqa.py             # Sauce Demo login page
│   └── elements_page.py      # Inventory page
├── tests/
│   ├── test_login_functionality.py
│   └── test_inventory_functionality.py
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
pytest tests/test_login_functionality.py
```

Run with verbose output:
```bash
pytest -v
```

## Test Cases

### test_login_functionality.py
- Tests login functionality with valid credentials
- Tests login with invalid credentials and error message verification

### test_inventory_functionality.py
- Tests adding items to cart functionality
- Tests logout functionality and navigation back to login page

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

### SauceDemo Page
- Login page elements and interactions
- User authentication methods
- Error message handling

### InventoryPage
- Inventory page specific functionality
- Shopping cart interactions
- Logout functionality

## Browser Configuration

The framework uses Chrome WebDriver with optimized settings:
- No sandbox mode for stability
- Disabled GPU for headless compatibility
- Implicit wait of 10 seconds
- Maximized window for consistent testing
