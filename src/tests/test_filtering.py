import pytest
from src.pages.discover_page import DiscoverPage
import logging

class TestFiltering:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.discover_page = DiscoverPage(driver)
        self.discover_page.navigate_to()
        self.logger = logging.getLogger(__name__)
    
    def test_category_filter_popular(self):
        """Test filtering by Popular category"""
        self.logger.info("Testing Popular category filter")
        self.discover_page.select_category("Popular")
        assert "popular" in self.discover_page.get_current_url().lower()
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Popular category test passed")
    
    def test_category_filter_trending(self):
        """Test filtering by Trending category"""
        self.logger.info("Testing Trending category filter")
        self.discover_page.select_category("Trending")
        assert "trending" in self.discover_page.get_current_url().lower()
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Trending category test passed")
    
    def test_search_by_title(self):
        """Test search functionality by movie title"""
        self.logger.info("Testing search functionality")
        self.discover_page.search_movie("avatar")
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Search test passed")
    
    def test_filter_by_type_movies(self):
        """Test filtering by Movies type"""
        self.logger.info("Testing Movies type filter")
        self.discover_page.select_type("Movies")
        # Add assertion to verify only movies are shown
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Movies filter test passed")
    
    def test_filter_by_year(self):
        """Test filtering by release year"""
        self.logger.info("Testing year filter")
        self.discover_page.filter_by_year(2023)
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Year filter test passed")
    
    def test_filter_by_rating(self):
        """Test filtering by minimum rating"""
        self.logger.info("Testing rating filter")
        self.discover_page.filter_by_rating(7.0)
        assert self.discover_page.get_movie_count() > 0
        self.logger.info(" Rating filter test passed")