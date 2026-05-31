"""
Usage examples for GreenCity Tests Framework
"""

# Example 1: Using Page Objects
from selenium import webdriver
from src.pages import EventsPage

driver = webdriver.Chrome()

# Create page object
events_page = EventsPage(driver)

# Navigate to events
events_page.navigate_to_events()

# Get events count
count = events_page.get_events_count()
print(f"Found {count} events")

# Get event titles
titles = events_page.get_event_titles()
for title in titles:
    print(f"Event: {title}")


# Example 2: Using Components
from src.components import Header, FilterPanel

# Create components
header = Header(driver)
filter_panel = FilterPanel(driver)

# Check if header is visible
if header.is_header_visible():
    print("Header is visible")

# Search for events
header.search("workshop")

# Open filter panel
events_page.click_filter_button()

# Get filter options
options_count = filter_panel.get_filter_options_count()
print(f"Available filters: {options_count}")

# Select first filter
filter_panel.select_filter_option(0)

# Apply filters
filter_panel.apply_filters()


# Example 3: Using EventCard Component
from src.components import EventCard

# Get all event cards
event_elements = events_page.find_elements(events_page.EVENT_CARDS)

# Iterate through cards
for event_element in event_elements:
    event_card = EventCard(driver, event_element)
    print(f"Title: {event_card.get_title()}")
    print(f"Date: {event_card.get_date()}")
    print(f"Location: {event_card.get_location()}")
    print("---")


# Example 4: Creating a test
import pytest
import allure
from src.pages import EventsPage
from src.components import Header


@allure.feature("Events")
@allure.story("Event Display")
class TestNewFeature:
    
    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        self.driver = setup_teardown
        self.events_page = EventsPage(self.driver)
    
    @allure.title("Test new feature")
    @pytest.mark.regression
    def test_new_feature(self):
        """Test description"""
        with allure.step("Navigate to events"):
            self.events_page.navigate_to_events()
        
        with allure.step("Perform action"):
            count = self.events_page.get_events_count()
        
        with allure.step("Verify result"):
            assert count > 0, "No events found"
