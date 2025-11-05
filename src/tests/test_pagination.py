import pytest
import logging
from src.pages.discover_page import DiscoverPage

logger = logging.getLogger(__name__)

class TestPagination:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.discover_page = DiscoverPage(driver)
        self.discover_page.navigate_to()
        logger.info("Pagination test setup completed")
    
    def test_pagination_navigation(self):
        """Test basic pagination functionality"""
        logger.info("Testing pagination navigation")
        
        # Get initial movie count
        initial_count = self.discover_page.get_movie_count()
        logger.info(f"Initial page shows {initial_count} movies")
        
        # Try to go to next page
        if self.discover_page.go_to_next_page():
            # Get new movie count
            new_count = self.discover_page.get_movie_count()
            logger.info(f"Next page shows {new_count} movies")
            
            # Take screenshot for evidence
            self.discover_page.take_screenshot('reports/pagination_test.png')
            logger.info(" Pagination navigation test completed")
        else:
            logger.warning(" Pagination might not be available on this page")
    
    def test_pagination_breakage(self):
        """Test pagination known issue (as mentioned in assignment)"""
        logger.info("Testing pagination breakage - known issue")
        
        # Try multiple page navigations to test the known issue
        for page_num in range(1, 6):  # Try up to 5 pages
            logger.info(f"Attempting to navigate to page {page_num + 1}")
            
            if not self.discover_page.go_to_next_page():
                logger.warning(f" Pagination broke at page {page_num + 1} (expected behavior)")
                break
            
            movie_count = self.discover_page.get_movie_count()
            logger.info(f"Page {page_num + 1} shows {movie_count} movies")
            
            if movie_count == 0:
                logger.warning(" Empty page detected - pagination issue confirmed")
                break
        
        logger.info(" Pagination breakage test completed")