from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
import time

class DiscoverPage(BasePage):
    # Locators (to find these in the next step)
    SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Search movies...']")
    CATEGORY_BUTTONS = (By.CSS_SELECTOR, ".categories button")
    MOVIE_CARDS = (By.CSS_SELECTOR, ".movie-card")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.next")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = self.config["base_url"]
    
    def navigate_to(self):
        """avigate to the main page"""
        self.driver.get(self.base_url)
        self.logger.info(f"Navigated to: {self.base_url}")
        time.sleep(2)  # Let page load
    
    def search_movie(self, movie_title):
        """Search for a movie by title"""
        self.enter_text(self.SEARCH_BOX, movie_title)
        time.sleep(2)  # Wait for results
        self.logger.info(f"Searched for movie: {movie_title}")
    
    def select_category(self, category_name):
        """Select a category like Popular, Trending, etc."""
        # This is a simplified version - so that if needed we can inspect the actual website
        categories = self.find_elements(self.CATEGORY_BUTTONS)
        for category in categories:
            if category_name.lower() in category.text.lower():
                category.click()
                self.logger.info(f"Selected category: {category_name}")
                time.sleep(2)
                return
        self.logger.error(f"Category not found: {category_name}")
    
    def get_movie_count(self):
        """Get number of movie cards displayed"""
        movies = self.find_elements(self.MOVIE_CARDS)
        count = len(movies)
        self.logger.info(f"Found {count} movie cards")
        return count
    
    def go_to_next_page(self):
        """Click next page button"""
        self.click_element(self.NEXT_BUTTON)
        time.sleep(2)
        self.logger.info("Clicked next page button")