from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

def get_chrome_driver():
    """Get Chrome driver with reliable setup"""
    chrome_options = webdriver.ChromeOptions()
    
    # Basic options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    
    # Remove headless for now to see what's happening
    # chrome_options.add_argument("--headless")
    
    driver = None
    
    # Method 1: Try to use webdriver-manager with correct binary
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.core.os_manager import ChromeType
        
        # Use ChromeType to ensure we get the right binary
        service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logger.info(" Using webdriver-manager ChromeDriver")
        return driver
    except Exception as e:
        logger.warning(f"WebDriver Manager failed: {e}")
    
    # Method 2: Manual ChromeDriver installation
    try:
        print("🔄 Attempting to install ChromeDriver via Homebrew...")
        result = subprocess.run(['brew', 'install', 'chromedriver'], capture_output=True, text=True)
        if result.returncode == 0:
            service = Service('/opt/homebrew/bin/chromedriver')
            driver = webdriver.Chrome(service=service, options=chrome_options)
            logger.info(" Using Homebrew ChromeDriver")
            return driver
    except Exception as e:
        logger.warning(f"Homebrew installation failed: {e}")
    
    # Method 3: Let Selenium find it automatically (seems to be working!)
    try:
        driver = webdriver.Chrome(options=chrome_options)
        logger.info(" Using auto-detected ChromeDriver")
        return driver
    except Exception as e:
        logger.error(f"Auto-detection failed: {e}")
    
    raise Exception("""
 Could not initialize ChromeDriver. 

The auto-detection is working but if you want to fix webdriver-manager:
1. brew install chromedriver
2. Or download manually from: https://chromedriver.chromium.org/
""")

def get_firefox_driver():
    """Fallback to Firefox if Chrome fails"""
    try:
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        logger.info(" Using Firefox as fallback")
        return driver
    except Exception as e:
        logger.error(f"Firefox also failed: {e}")
        return None