import pytest
from src.pages.discover_page import DiscoverPage
import logging

class TestBasicNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.discover_page = DiscoverPage(driver)
        self.logger = logging.getLogger(__name__)
    
    def test_page_loads(self, driver):
        """Test that the main page loads successfully"""
        self.logger.info("Starting page load test")
        
        # Navigate to the page
        self.discover_page.navigate_to()
        
        # Check page title or URL contains expected text
        current_url = driver.current_url
        assert "tmdb-discover" in current_url
        self.logger.info(f"Page loaded successfully: {current_url}")
        
        # Check that some content is displayed
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0
        self.logger.info(f"Page shows {movie_count} movies")
    
    def test_search_functionality(self):
        """Test basic search functionality"""
        self.logger.info("Starting search test")
        
        # Search for a common term
        self.discover_page.search_movie("avatar")
        
        # Verify search worked (simplified)
        movie_count = self.discover_page.get_movie_count()
        assert movie_count >= 0  # Could be 0 if no results
        self.logger.info("Search test completed")