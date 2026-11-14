
from selenium import webdriver


def test_homepage_loads():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        assert "Swag Labs" in driver.title
        print("Homepage test passed!")

    finally:
        driver.quit()
