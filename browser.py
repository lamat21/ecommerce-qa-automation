import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver():
    options = webdriver.ChromeOptions()

    if os.getenv("CI", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    service = Service(
        service_args=["--verbose"],
        log_output="chromedriver.log"
    )

    return webdriver.Chrome(
        options=options,
        service=service
    )
