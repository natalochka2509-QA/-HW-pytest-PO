"""Test module for Events Page functionality"""
import pytest
import allure
from src.pages import EventsPage
from src.components import Header, FilterPanel, EventCard


@allure.feature("Events Page")
@allure.story("Display and Navigation")
class TestEventsPageDisplay:
    """Test class for events page display functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        """Setup test fixtures."""
        self.driver = setup_teardown
        self.events_page = EventsPage(self.driver)
        self.header = Header(self.driver)

    @allure.title("Test events page loads successfully")
    @allure.description("Verify that events page loads and events container is visible")
    @pytest.mark.smoke
    def test_events_page_loads(self):
        """Test that events page loads successfully."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Verify events page is loaded"):
            assert (
                self.events_page.is_events_loaded()
            ), "Events page did not load"

        allure.attach.file(
            self.driver.get_screenshot_as_png,
            name="page_loaded",
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.title("Test header visibility on events page")
    @allure.description("Verify that header is visible when on events page")
    @pytest.mark.smoke
    def test_header_is_visible(self):
        """Test that header is visible on events page."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Verify header is visible"):
            assert self.header.is_header_visible(), "Header is not visible"

    @allure.title("Test events are displayed on page")
    @allure.description("Verify that at least one event card is displayed")
    @pytest.mark.regression
    def test_events_displayed(self):
        """Test that events are displayed on page."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Get count of displayed events"):
            events_count = self.events_page.get_events_count()

        with allure.step("Verify at least one event is displayed"):
            assert events_count > 0, "No events found on page"

        allure.attach(
            f"Found {events_count} event(s)", "Events Count", allure.attachment_type.TEXT
        )


@allure.feature("Events Page")
@allure.story("Event Titles")
class TestEventTitles:
    """Test class for event titles functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        """Setup test fixtures."""
        self.driver = setup_teardown
        self.events_page = EventsPage(self.driver)

    @allure.title("Test getting event titles")
    @allure.description(
        "Verify that all event titles can be retrieved and are strings"
    )
    @pytest.mark.regression
    def test_get_event_titles(self):
        """Test getting event titles from page."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Retrieve all event titles"):
            titles = self.events_page.get_event_titles()

        with allure.step("Verify titles list is not empty"):
            assert len(titles) > 0, "No event titles found"

        with allure.step("Verify all titles are strings"):
            assert all(
                isinstance(title, str) for title in titles
            ), "Not all titles are strings"

        with allure.step("Log titles found"):
            titles_text = "\n".join(titles)
            allure.attach(
                titles_text,
                "Event Titles",
                allure.attachment_type.TEXT,
            )


@allure.feature("Events Page")
@allure.story("Filtering")
class TestEventFiltering:
    """Test class for event filtering functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, setup_teardown):
        """Setup test fixtures."""
        self.driver = setup_teardown
        self.events_page = EventsPage(self.driver)
        self.filter_panel = FilterPanel(self.driver)

    @allure.title("Test filter button is clickable")
    @allure.description("Verify that filter button can be clicked and panel appears")
    @pytest.mark.smoke
    def test_filter_button_clickable(self):
        """Test that filter button is clickable."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Click filter button"):
            self.events_page.click_filter_button()

        with allure.step("Verify filter panel is visible"):
            assert (
                self.filter_panel.is_filter_panel_visible()
            ), "Filter panel did not appear"

        allure.attach.file(
            self.driver.get_screenshot_as_png,
            name="filter_panel_visible",
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.title("Test filter options are available")
    @allure.description("Verify that filter panel has available filter options")
    @pytest.mark.regression
    def test_filter_options_exist(self):
        """Test that filter options exist in the panel."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Click filter button to open panel"):
            self.events_page.click_filter_button()

        with allure.step("Get count of filter options"):
            options_count = self.filter_panel.get_filter_options_count()

        with allure.step("Verify at least one filter option exists"):
            assert options_count > 0, "No filter options found"

        allure.attach(
            f"Found {options_count} filter option(s)",
            "Filter Options Count",
            allure.attachment_type.TEXT,
        )

    @allure.title("Test filter option selection")
    @allure.description("Verify that filter option can be selected")
    @pytest.mark.regression
    def test_select_filter_option(self):
        """Test selecting a filter option."""
        with allure.step("Navigate to events page"):
            self.events_page.navigate_to_events()

        with allure.step("Click filter button to open panel"):
            self.events_page.click_filter_button()

        with allure.step("Get filter options count"):
            options_count = self.filter_panel.get_filter_options_count()

        if options_count > 0:
            with allure.step("Select first filter option"):
                result = self.filter_panel.select_filter_option(0)
                assert result, "Failed to select filter option"

            allure.attach(
                "First filter option selected successfully",
                "Result",
                allure.attachment_type.TEXT,
            )
        else:
            pytest.skip("No filter options available to select")
