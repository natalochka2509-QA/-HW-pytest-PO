"""Pytest configuration and fixtures for test setup and teardown"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    """
    Initialize and teardown browser session.

    Yields:
        WebDriver: Selenium WebDriver instance
    """
    headless = os.getenv("HEADLESS_MODE", "false").lower() == "true"
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    yield driver

    driver.quit()


@pytest.fixture
def setup_teardown(browser):
    """
    Setup and teardown for each test.

    Args:
        browser: Browser fixture

    Yields:
        WebDriver: Configured WebDriver instance for test
    """
    # Setup
    implicit_wait = int(os.getenv("IMPLICIT_WAIT", "10"))
    browser.implicitly_wait(implicit_wait)

    yield browser

    # Teardown
    browser.delete_all_cookies()
