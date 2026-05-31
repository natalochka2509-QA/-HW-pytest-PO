from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Header:
    """Header Component"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
        # Locators
        self.LOGO = (By.CSS_SELECTOR, "[class*='logo']")
        self.NAV_MENU = (By.CSS_SELECTOR, "[class*='nav-menu']")
        self.SEARCH_INPUT = (By.CSS_SELECTOR, "[class*='search-input']")
        self.USER_PROFILE = (By.CSS_SELECTOR, "[class*='user-profile']")
    
    def click_logo(self):
        """Click on logo"""
        self.driver.find_element(*self.LOGO).click()
    
    def is_header_visible(self) -> bool:
        """Check if header is visible"""
        try:
            return self.driver.find_element(*self.LOGO).is_displayed()
        except:
            return False
    
    def search(self, query: str):
        """Search functionality"""
        search_field = self.driver.find_element(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(query)
