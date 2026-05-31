from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class EventCard:
    """Event Card Component"""
    
    def __init__(self, driver: WebDriver, element: WebElement):
        self.driver = driver
        self.element = element
        
        # Locators relative to card
        self.CARD_TITLE = (By.CSS_SELECTOR, "[class*='event-title']")
        self.CARD_DATE = (By.CSS_SELECTOR, "[class*='event-date']")
        self.CARD_LOCATION = (By.CSS_SELECTOR, "[class*='event-location']")
        self.CARD_BUTTON = (By.CSS_SELECTOR, "[class*='event-btn']")
    
    def get_title(self) -> str:
        """Get event card title"""
        return self.element.find_element(*self.CARD_TITLE).text
    
    def get_date(self) -> str:
        """Get event card date"""
        return self.element.find_element(*self.CARD_DATE).text
    
    def get_location(self) -> str:
        """Get event card location"""
        return self.element.find_element(*self.CARD_LOCATION).text
    
    def click_card(self):
        """Click on event card"""
        self.element.click()
    
    def click_button(self):
        """Click card button"""
        self.element.find_element(*self.CARD_BUTTON).click()
