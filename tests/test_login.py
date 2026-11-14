
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.url_contains("inventory.html"))

        assert "inventory.html" in driver.current_url

        print("Login test PASSED!")

    finally:
        driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("wrong_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("wrong_password")

        driver.find_element(By.ID, "login-button").click()

        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        assert "Username and password do not match" in error_message.text

        print("Invalid login test PASSED!")

    finally:
        driver.quit()
