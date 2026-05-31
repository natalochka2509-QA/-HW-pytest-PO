"""Event Card Component"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EventCard:
    """Event Card Component for individual event representation."""

    def __init__(self, driver: WebDriver, element: WebElement):
        """
        Initialize EventCard component.

        Args:
            driver: Selenium WebDriver instance
            element: WebElement representing the event card
        """
        self.driver = driver
        self.element = element

        # Locators relative to card
        self.CARD_TITLE = (By.CSS_SELECTOR, "[class*='event-title']")
        self.CARD_DATE = (By.CSS_SELECTOR, "[class*='event-date']")
        self.CARD_LOCATION = (By.CSS_SELECTOR, "[class*='event-location']")
        self.CARD_BUTTON = (By.CSS_SELECTOR, "[class*='event-btn']")

    def get_title(self) -> str:
        """
        Get event card title.

        Returns:
            Title text of the event
        """
        return self.element.find_element(*self.CARD_TITLE).text

    def get_date(self) -> str:
        """
        Get event card date.

        Returns:
            Date text of the event
        """
        return self.element.find_element(*self.CARD_DATE).text

    def get_location(self) -> str:
        """
        Get event card location.

        Returns:
            Location text of the event
        """
        return self.element.find_element(*self.CARD_LOCATION).text

    def click_card(self):
        """Click on event card to view details."""
        self.element.click()

    def click_button(self):
        """Click action button on event card."""
        self.element.find_element(*self.CARD_BUTTON).click()
