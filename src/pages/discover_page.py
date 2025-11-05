from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class DiscoverPage:
    # Updated locators for TMDB Discover website
    BASE_URL = "https://tmdb-discover.surge.sh/"
    
    # Generic selectors that should work with most movie sites
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='search'], input[name*='search']")
    CATEGORY_BUTTONS = (By.CSS_SELECTOR, "button, a, nav a, nav button, .tab, .category")
    MOVIE_CARDS = (By.CSS_SELECTOR, "div, article, section, .card, .movie, [class*='item']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button, a, [class*='next'], [aria-label*='next']")
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to(self):
        """Navigate to the main page"""
        self.logger.info(f"Navigating to: {self.BASE_URL}")
        self.driver.get(self.BASE_URL)
        time.sleep(3)  # Wait for page to load
        return self
    
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def search_movie(self, movie_title):
        """Search for a movie by title"""
        self.logger.info(f"Searching for movie: {movie_title}")
        try:
            # Try multiple search box selectors
            selectors = [
                "input[type='search']",
                "input[placeholder*='search']",
                "input[placeholder*='Search']",
                "input[name*='search']",
                "input[class*='search']"
            ]
            
            for selector in selectors:
                try:
                    search_box = self.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    search_box.clear()
                    search_box.send_keys(movie_title)
                    
                    # Try to submit
                    try:
                        search_box.submit()
                    except:
                        # If submit doesn't work, press Enter
                        from selenium.webdriver.common.keys import Keys
                        search_box.send_keys(Keys.RETURN)
                    
                    time.sleep(2)
                    self.logger.info(f"Successfully searched for: {movie_title}")
                    return True
                except:
                    continue
            
            self.logger.warning("No search box found with any selector")
            return False
            
        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return False
    
    def select_category(self, category_name):
        """Select a category like Popular, Trending, etc."""
        self.logger.info(f"Selecting category: {category_name}")
        try:
            # Get all clickable elements
            clickable_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button, a"))
            )
            
            for element in clickable_elements:
                text = element.text.strip()
                if text and category_name.lower() in text.lower():
                    self.driver.execute_script("arguments[0].click();", element)
                    time.sleep(2)
                    self.logger.info(f"✅ Successfully selected: {text}")
                    return True
            
            self.logger.warning(f"Category not found: {category_name}")
            return False
            
        except Exception as e:
            self.logger.error(f"Category selection failed: {e}")
            return False
    
    def get_movie_count(self):
        """Get number of movie cards displayed"""
        try:
            # Wait for page content to load
            time.sleep(2)
            
            # Try to find any content elements that might be movies
            content_elements = self.driver.find_elements(By.CSS_SELECTOR, "div, article, section, li")
            
            # Filter elements that might be movie cards (have some content)
            movie_like_elements = [elem for elem in content_elements 
                                 if elem.is_displayed() and 
                                 elem.size['width'] > 100 and 
                                 elem.size['height'] > 100]
            
            count = len(movie_like_elements)
            self.logger.info(f"🎬 Found {count} potential movie elements")
            return count
            
        except Exception as e:
            self.logger.error(f"Error counting movies: {e}")
            return 0
    
    def go_to_next_page(self):
        """Click next page button"""
        self.logger.info("Navigating to next page")
        try:
            # Try to find next button by text
            next_buttons = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Next') or contains(text(), '>') or contains(@aria-label, 'next')]")
            
            for button in next_buttons:
                if button.is_displayed() and button.is_enabled():
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(2)
                    self.logger.info("Successfully clicked next page")
                    return True
            
            self.logger.warning("No next button found")
            return False
            
        except Exception as e:
            self.logger.error(f"Next page navigation failed: {e}")
            return False
    
    def is_page_loaded(self):
        """Check if page is loaded successfully"""
        try:
            # Check if page title or body has content
            title = self.driver.title
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            
            if title or len(body_text) > 10:
                self.logger.info("Page loaded successfully")
                return True
            else:
                self.logger.warning("Page appears empty")
                return False
                
        except Exception as e:
            self.logger.error(f"Page load check failed: {e}")
            return False
    
    def take_screenshot(self, filename):
        """Take screenshot of current page"""
        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"📸 Screenshot saved: {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Screenshot failed: {e}")
            return False