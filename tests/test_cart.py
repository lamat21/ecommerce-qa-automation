
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Log in
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for products page
        wait.until(EC.url_contains("inventory.html"))

        # Add backpack to cart
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # Verify cart badge shows 1
        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert cart_badge.text == "1"

        # Open shopping cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verify correct product
        product_name = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert product_name.text == "Sauce Labs Backpack"

        print("Add to cart test PASSED!")

    finally:
        driver.quit()

def test_remove_product_from_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        # Log in
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for products page
        wait.until(EC.url_contains("inventory.html"))

        # Add backpack to cart
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # Verify product was added
        assert driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        ).text == "1"

        # Open shopping cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Remove backpack
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
        ).click()

        # Verify product is removed
        wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

        print("Remove from cart test PASSED!")

    finally:
        driver.quit()
