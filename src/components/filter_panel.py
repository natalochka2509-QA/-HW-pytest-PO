"""Filter Panel Component"""
from selenium.webdriver.common.by import By
from .base_component import BaseComponent


class FilterPanel(BaseComponent):
    """Filter Panel Component for filtering events by tags and options."""

    # Locators
    FILTER_CONTAINER = (By.CSS_SELECTOR, "[class*='filter-panel']")
    FILTER_OPTIONS = (By.CSS_SELECTOR, "[class*='filter-option']")
    APPLY_BUTTON = (By.CSS_SELECTOR, "[class*='apply-filters']")
    RESET_BUTTON = (By.CSS_SELECTOR, "[class*='reset-filters']")

    def is_filter_panel_visible(self) -> bool:
        """
        Check if filter panel is visible on page.

        Returns:
            True if filter panel is visible, False otherwise
        """
        return self.is_element_visible(self.FILTER_CONTAINER)

    def get_filter_options_count(self) -> int:
        """
        Get count of available filter options.

        Returns:
            Count of filter options
        """
        return self.get_element_count(self.FILTER_OPTIONS)

    def select_filter_option(self, option_index: int):
        """
        Select filter option by index.

        Args:
            option_index: Index of filter option to select

        Returns:
            True if option was selected, False if index is out of range
        """
        options = self.find_elements(self.FILTER_OPTIONS)
        if option_index < len(options):
            options[option_index].click()
            return True
        return False

    def apply_filters(self):
        """Click apply filters button to apply selected filters."""
        self.click_element(self.APPLY_BUTTON)

    def reset_filters(self):
        """Click reset filters button to clear all filters."""
        self.click_element(self.RESET_BUTTON)
