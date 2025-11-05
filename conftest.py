import pytest
import logging
import allure
from src.browser_setup import get_chrome_driver

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    """Setup Chrome driver fixture"""
    logger = logging.getLogger(__name__)
    driver_instance = None
    
    try:
        driver_instance = get_chrome_driver()
        logger.info(" WebDriver initialized successfully")
        yield driver_instance
    except Exception as e:
        logger.error(f" WebDriver initialization failed: {e}")
        pytest.fail(f"WebDriver setup failed: {e}")
    finally:
        if driver_instance:
            driver_instance.quit()
            logger.info(" WebDriver closed")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Take screenshot
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
                
                # Get page source for debugging
                page_source = driver.page_source
                allure.attach(page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
                
                logging.getLogger(__name__).info("📸 Captured screenshot and page source on failure")
            except Exception as e:
                logging.getLogger(__name__).error(f"Failed to capture failure evidence: {e}")