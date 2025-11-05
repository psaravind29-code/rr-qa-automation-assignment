import pytest
import logging
from src.pages.discover_page import DiscoverPage

logger = logging.getLogger(__name__)

class TestFiltering:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.discover_page = DiscoverPage(driver)
        self.discover_page.navigate_to()
        logger.info("Test setup completed")
    
    def test_category_filter_popular(self):
        """Test filtering by Popular category"""
        logger.info("Testing Popular category filter")
        
        # Select Popular category
        assert self.discover_page.select_category("Popular"), "Should select Popular category"
        
        # Verify URL or page content changed
        current_url = self.discover_page.get_current_url()
        logger.info(f"Current URL after selecting Popular: {current_url}")
        
        # Verify movies are displayed
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0, "Should display movies after selecting Popular"
        logger.info(f" Popular category shows {movie_count} movies")
    
    def test_category_filter_trending(self):
        """Test filtering by Trending category"""
        logger.info("Testing Trending category filter")
        
        # Select Trending category
        assert self.discover_page.select_category("Trending"), "Should select Trending category"
        
        # Verify movies are displayed
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0, "Should display movies after selecting Trending"
        logger.info(f" Trending category shows {movie_count} movies")
    
    def test_search_by_title(self):
        """Test search functionality by movie title"""
        logger.info("Testing search functionality")
        
        # Search for a movie
        assert self.discover_page.search_movie("avatar"), "Should perform search"
        
        # Verify search results
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0, "Should display search results"
        logger.info(f" Search shows {movie_count} results")
    
    def test_category_filter_newest(self):
        """Test filtering by Newest category"""
        logger.info("Testing Newest category filter")
        
        # Select Newest category
        assert self.discover_page.select_category("Newest"), "Should select Newest category"
        
        # Verify movies are displayed
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0, "Should display movies after selecting Newest"
        logger.info(f" Newest category shows {movie_count} movies")
    
    def test_category_filter_top_rated(self):
        """Test filtering by Top Rated category"""
        logger.info("Testing Top Rated category filter")
        
        # Select Top Rated category
        assert self.discover_page.select_category("Top Rated"), "Should select Top Rated category"
        
        # Verify movies are displayed
        movie_count = self.discover_page.get_movie_count()
        assert movie_count > 0, "Should display movies after selecting Top Rated"
        logger.info(f" Top Rated category shows {movie_count} movies")