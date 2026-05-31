"""Header Component"""
from selenium.webdriver.common.by import By
from .base_component import BaseComponent


class Header(BaseComponent):
    """Header Component for top navigation and search functionality."""

    # Locators
    LOGO = (By.CSS_SELECTOR, "[class*='logo']")
    NAV_MENU = (By.CSS_SELECTOR, "[class*='nav-menu']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[class*='search-input']")
    USER_PROFILE = (By.CSS_SELECTOR, "[class*='user-profile']")

    def click_logo(self):
        """Click on logo to navigate to home page."""
        self.click_element(self.LOGO)

    def is_header_visible(self) -> bool:
        """
        Check if header is visible on page.

        Returns:
            True if header is visible, False otherwise
        """
        return self.is_element_visible(self.LOGO)

    def search(self, query: str):
        """
        Perform search with given query.

        Args:
            query: Search query string
        """
        self.input_text(self.SEARCH_INPUT, query)
