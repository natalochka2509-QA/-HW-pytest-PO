"""Base Page Object class"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Base Page Object class with common methods for page interactions."""

    def __init__(self, driver: WebDriver, base_url: str = None):
        """
        Initialize base page.

        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL for the application
        """
        self.driver = driver
        self.base_url = base_url or "https://greencity.com"
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url: str = None):
        """
        Navigate to URL.

        Args:
            url: URL to navigate to. If None, uses base_url
        """
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.base_url)

    def find_element(self, locator):
        """
        Find element with explicit wait.

        Args:
            locator: Tuple of (By, value)

        Returns:
            WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """
        Find multiple elements.

        Args:
            locator: Tuple of (By, value)

        Returns:
            List of WebElements
        """
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """
        Click element with explicit wait.

        Args:
            locator: Tuple of (By, value)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text: str):
        """
        Input text into element.

        Args:
            locator: Tuple of (By, value)
            text: Text to input
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator) -> str:
        """
        Get element text.

        Args:
            locator: Tuple of (By, value)

        Returns:
            Element text
        """
        return self.find_element(locator).text

    def is_element_visible(self, locator) -> bool:
        """
        Check if element is visible.

        Args:
            locator: Tuple of (By, value)

        Returns:
            True if visible, False otherwise
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def scroll_to_element(self, locator):
        """
        Scroll to element.

        Args:
            locator: Tuple of (By, value)
        """
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
