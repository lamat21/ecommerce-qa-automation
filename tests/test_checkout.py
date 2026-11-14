
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import create_driver

def test_complete_checkout():
    driver = create_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Step 1: Log in
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.url_contains("inventory.html"))

        # Step 2: Add product to cart
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        # Step 3: Open cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.url_contains("cart.html"))

        # Verify product is in cart
        assert driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text == "Sauce Labs Backpack"

        # Step 4: Start checkout
        driver.find_element(By.ID, "checkout").click()

        wait.until(EC.url_contains("checkout-step-one.html"))

        # Step 5: Enter customer information
        
        # Step 5: Enter customer information

        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )
        first_name.send_keys("Test")

        last_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        )
        last_name.send_keys("User")

        postal_code = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )
        postal_code.send_keys("L5B 1M1")

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        ).click()


        
        # Step 6: Verify checkout overview
        wait.until(EC.url_contains("checkout-step-two.html"))

        # Wait until the backpack appears
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".cart_item .inventory_item_name"),
                "Sauce Labs Backpack"
            )
        )

        print("Checkout overview verified!")

       
        # Step 7: Complete checkout
        finish_button = wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_button.click()

        # Step 8: Wait for order confirmation
        try:
            wait.until(
                EC.url_contains("checkout-complete.html")
            )

            confirmation = wait.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "complete-header")
                )
            )

            assert confirmation.text == "Thank you for your order!"

            print("Complete checkout test PASSED!")

        except Exception:
            print("Checkout URL:", driver.current_url)
            print("Page text:", driver.find_element(By.TAG_NAME, "body").text)
            driver.save_screenshot("checkout_failure.png")
            raise

    finally:
        driver.quit()
