
import os
from selenium import webdriver


def create_driver():
    options = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)
