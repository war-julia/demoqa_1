# Ломоносовская Гимназия Test Automation Framework

This project contains automated tests for the [Ломоносовская гимназия](https://ломоносовскаягимназия.рф/) website using Selenium WebDriver and Python.

## Project Structure

```
demoqa/
├── components/
│   └── components.py          # WebElement wrapper class
├── pages/
│   ├── base_page.py          # Base page object
│   ├── main_page.py          # Main page of the school website
│   ├── news_page.py          # News and announcements page
│   ├── education_page.py     # Educational programs page
│   └── contacts_page.py      # Contact information page
├── tests/
│   ├── test_main_page.py     # Tests for main page functionality
│   ├── test_news_page.py     # Tests for news section
│   ├── test_education_page.py # Tests for educational programs
│   └── test_contacts_page.py # Tests for contact information
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
pytest tests/test_main_page.py
```

Run with verbose output:
```bash
pytest -v
```

## Test Cases

### test_main_page.py
- Tests main page loading and navigation
- Tests school information display
- Tests menu navigation functionality

### test_news_page.py
- Tests news section accessibility
- Tests announcement display
- Tests news filtering and search

### test_education_page.py
- Tests educational programs information
- Tests curriculum details
- Tests enrollment information

### test_contacts_page.py
- Tests contact information display
- Tests contact form functionality
- Tests location and map information

## Framework Features

- **Page Object Model**: Organized page classes for better maintainability
- **WebElement Wrapper**: Custom WebElement class with timeout handling
- **Explicit Waits**: Proper element waiting with WebDriverWait
- **Error Handling**: Comprehensive exception handling for element interactions
- **Pytest Integration**: Full pytest framework integration with fixtures
- **Russian Language Support**: Optimized for Russian language website testing

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

### MainPage
- Main page elements and interactions
- School information verification
- Navigation menu testing

### NewsPage
- News section specific functionality
- Announcement verification
- News filtering capabilities

### EducationPage
- Educational programs testing
- Curriculum information verification
- Enrollment process testing

### ContactsPage
- Contact information verification
- Contact form testing
- Location and map functionality

## Browser Configuration

The framework uses Chrome WebDriver with optimized settings:
- No sandbox mode for stability
- Disabled GPU for headless compatibility
- Implicit wait of 10 seconds
- Maximized window for consistent testing
- Russian language support for proper character encoding

## Website Information

**Ломоносовская гимназия** is an educational institution implementing programs in humanities, technology, and natural sciences. The school offers:
- 864 students in primary, basic, and secondary general education programs
- Specialized education from 5th grade with humanities profile
- Second foreign language (German) from 5th grade
- Profile education in 10-11 grades: humanities, natural sciences, and technology
- Various extracurricular activities and clubs
- International and all-Russian project participation
