import pytest
from selenium import webdriver
import allure
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Take screenshot on failure
        driver = item.funcargs['driver']
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)