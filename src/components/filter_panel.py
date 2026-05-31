from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class FilterPanel:
    """Filter Panel Component"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
        # Locators
        self.FILTER_CONTAINER = (By.CSS_SELECTOR, "[class*='filter-panel']")
        self.FILTER_OPTIONS = (By.CSS_SELECTOR, "[class*='filter-option']")
        self.APPLY_BUTTON = (By.CSS_SELECTOR, "[class*='apply-filters']")
        self.RESET_BUTTON = (By.CSS_SELECTOR, "[class*='reset-filters']")
    
    def is_filter_panel_visible(self) -> bool:
        """Check if filter panel is visible"""
        try:
            return self.driver.find_element(*self.FILTER_CONTAINER).is_displayed()
        except:
            return False
    
    def get_filter_options_count(self) -> int:
        """Get count of filter options"""
        return len(self.driver.find_elements(*self.FILTER_OPTIONS))
    
    def select_filter_option(self, option_index: int):
        """Select filter option by index"""
        options = self.driver.find_elements(*self.FILTER_OPTIONS)
        if option_index < len(options):
            options[option_index].click()
    
    def apply_filters(self):
        """Click apply filters button"""
        self.driver.find_element(*self.APPLY_BUTTON).click()
    
    def reset_filters(self):
        """Click reset filters button"""
        self.driver.find_element(*self.RESET_BUTTON).click()
