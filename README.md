
# E-commerce QA Automation Framework


[![E-commerce QA Automated Tests](https://github.com/lamat21/ecommerce-qa-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/lamat21/ecommerce-qa-automation/actions/workflows/tests.yml)

Automated UI testing project for an e-commerce website using Python, Selenium WebDriver, and Pytest.

## Technologies
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Google Chrome
- Git & GitHub

## Website Under Test
https://www.saucedemo.com/

## Automated Test Scenarios
1. Verify homepage loads successfully.
2. Verify login with valid credentials.
3. Verify error message for invalid login.
4. Verify adding a product to the shopping cart.
5. Verify removing a product from the shopping cart.
6. Verify completing the checkout process.

## Project Structure

ecommerce-qa-automation/
    tests/
        test_homepage.py
        test_login.py
        test_cart.py
        test_checkout.py
    requirements.txt
    .gitignore
    README.md

## Installation

Clone the repository and navigate into the project folder.

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

## Running Tests

Run all tests:

    python -m pytest tests/ -v

Generate an HTML test report:

    python -m pytest tests/ -v --html=report.html --self-contained-html

## Test Reporting

This framework generates HTML reports showing test execution results, passed and failed tests, and execution durations.

## Future Improvements
- Page Object Model (POM)
- Data-driven testing
- GitHub Actions CI/CD
- Cross-browser testing
- Automated screenshots on failure
