
import os
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver():
    options = webdriver.ChromeOptions()

    if os.getenv("CI", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-pipe")

    with tempfile.NamedTemporaryFile(
        prefix="chromedriver_",
        suffix=".log",
        dir=".",
        delete=False
    ) as logfile:
        log_path = logfile.name

    service = Service(
        service_args=["--verbose"],
        log_output=log_path
    )

    return webdriver.Chrome(
        options=options,
        service=service
    )
