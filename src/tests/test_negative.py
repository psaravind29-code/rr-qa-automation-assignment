import pytest
import logging
from src.pages.discover_page import DiscoverPage

logger = logging.getLogger(__name__)

class TestNegative:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.discover_page = DiscoverPage(driver)
        logger.info("Negative test setup completed")
    
    def test_direct_slug_access(self):
        """Test known issue with direct slug access"""
        logger.info("Testing direct slug access issue")
        
        # Try to access popular page directly (known issue from assignment)
        self.discover_page.driver.get("https://tmdb-discover.surge.sh/popular")
        
        # Check if page loaded properly
        if self.discover_page.is_page_loaded():
            movie_count = self.discover_page.get_movie_count()
            logger.info(f"Direct slug access shows {movie_count} movies")
        else:
            logger.warning(" Direct slug access failed (expected behavior)")
        
        # Take screenshot for evidence
        self.discover_page.take_screenshot('reports/direct_slug_test.png')
        logger.info(" Direct slug access test completed")
    
    def test_search_invalid_title(self):
        """Test search with invalid movie title"""
        logger.info("Testing search with invalid title")
        
        # Navigate to main page first
        self.discover_page.navigate_to()
        
        # Search for invalid movie title
        assert self.discover_page.search_movie("invalid_movie_title_xyz123"), "Should attempt search"
        
        # Check results
        movie_count = self.discover_page.get_movie_count()
        logger.info(f"Invalid search shows {movie_count} results")
        
        if movie_count == 0:
            logger.info(" No results for invalid search (expected)")
        else:
            logger.info(" Unexpected results for invalid search")
        
        logger.info(" Invalid search test completed")
    
    def test_empty_search(self):
        """Test search with empty string"""
        logger.info("Testing empty search")
        
        # Navigate to main page
        self.discover_page.navigate_to()
        
        # Search with empty string
        assert self.discover_page.search_movie(""), "Should attempt empty search"
        
        # Check if page still works
        assert self.discover_page.is_page_loaded(), "Page should still be functional"
        logger.info(" Empty search test completed")