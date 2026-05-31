"""Events Page Object"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class EventsPage(BasePage):
    """Page Object for Events page with event-related actions."""

    # Locators
    EVENTS_CONTAINER = (By.CSS_SELECTOR, "[class*='events-container']")
    EVENT_CARDS = (By.CSS_SELECTOR, "[class*='event-card']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "[class*='filter-btn']")
    EVENT_TITLE = (By.CSS_SELECTOR, "[class*='event-title']")
    EVENT_DATE = (By.CSS_SELECTOR, "[class*='event-date']")

    def __init__(self, driver):
        """
        Initialize EventsPage.

        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
        self.page_url = f"{self.base_url}/events"

    def navigate_to_events(self):
        """Navigate to events page."""
        self.navigate_to(self.page_url)

    def get_events_count(self) -> int:
        """
        Get count of event cards on page.

        Returns:
            Count of event cards
        """
        return len(self.find_elements(self.EVENT_CARDS))

    def get_event_titles(self) -> list:
        """
        Get all event titles displayed on page.

        Returns:
            List of event title strings
        """
        elements = self.find_elements(self.EVENT_TITLE)
        return [elem.text for elem in elements]

    def click_filter_button(self):
        """Click filter button to open filter panel."""
        self.click_element(self.FILTER_BUTTON)

    def is_events_loaded(self) -> bool:
        """
        Check if events container is visible.

        Returns:
            True if events are loaded, False otherwise
        """
        return self.is_element_visible(self.EVENTS_CONTAINER)
