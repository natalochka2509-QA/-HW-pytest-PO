import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    """Initialize and teardown browser session"""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver
    
    driver.quit()

@pytest.fixture
def setup_teardown(browser):
    """Setup and teardown for each test"""
    # Setup
    browser.implicitly_wait(10)
    browser.maximize_window()
    
    yield browser
    
    # Teardown
    browser.delete_all_cookies()
