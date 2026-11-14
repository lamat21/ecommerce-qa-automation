
import os
import time
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import SessionNotCreatedException


def create_driver():
    is_ci = os.getenv("CI", "").lower() == "true"
    max_attempts = 3 if is_ci else 1

    for attempt in range(1, max_attempts + 1):
        options = webdriver.ChromeOptions()

        if is_ci:
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

        try:
            print(
                f"Starting Chrome: attempt "
                f"{attempt}/{max_attempts}",
                flush=True
            )

            driver = webdriver.Chrome(
                options=options,
                service=service
            )

            print("Chrome started successfully!", flush=True)
            return driver

        except SessionNotCreatedException:
            print(
                f"Chrome startup failed on attempt {attempt}. "
                f"See {log_path}",
                flush=True
            )

            if attempt == max_attempts:
                raise

            time.sleep(2 * attempt)
