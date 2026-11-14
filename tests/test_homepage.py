
from selenium import webdriver
from browser import create_driver

def test_homepage_loads():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")

        assert "Swag Labs" in driver.title
        print("Homepage test passed!")

    finally:
        driver.quit()
