# RR QA Automation Assignment

This repository contains the automation test suite for the TMDB Discover demo website (https://tmdb-discover.surge.sh/), developed as part of the Rapyuta Robotics QA Automation Engineer application process.

## 🚀 Overview

The project automates functional testing for the key features of the site:
*   **Filtering & Search:** Categories, Titles, Type, Year, Rating, Genre.
*   **Pagination:** Navigating through multiple pages of results.
*   **Negative Testing:** Handling known issues and unexpected behavior.

The framework is built with a focus on **maintainability, clarity, and reporting**.

## 🛠️ Tech Stack & Framework

*   **Language:** Python 3.x
*   **Test Framework:** Pytest
*   **Browser Automation:** Selenium WebDriver
*   **Reporting:** Allure Report (for rich HTML reports) & Pytest-sugar (for improved console output)
*   **API Testing:** Requests library
*   **Logging:** Custom Python logger
*   **Patterns:** Page Object Model (POM)

## 📋 Testing Strategy & Design

A detailed breakdown of the test strategy, generated test cases, and the reasoning behind them can be found here:
[**Test Strategy and Cases Document**](./docs/Test_Strategy_and_Cases.md)

Highlights:
*   **Test Design Techniques:** Equivalence Partitioning, Boundary Value Analysis, Positive/Negative Testing.
*   **Scope:** ~15-20 core automated test cases covering the main functionalities.
*   **Why these cases?** They represent the most critical user journeys and high-risk areas based on the assignment description.

## ▶️ How to Run the Tests

### Prerequisites
1.  Python 3.8+ installed on your machine.
2.  Clone this repository: `git clone https://github.com/<your-username>/rr-qa-automation-assignment.git`
3.  Navigate to the project directory.

### Installation & Execution

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Full Test Suite:**
    ```bash
    # This will run all tests and generate Allure results
    python run_tests.py

    # Or run directly with pytest
    pytest src/tests/ -v -s --alluredir=reports/allure_results
    ```

3.  **Generate the HTML Report:**
    After execution, generate the Allure report:
    ```bash
    allure serve reports/allure_results
    ```
    This will open a detailed, interactive HTML report in your browser.

## 🧩 Framework Explanation

### Patterns Used
*   **Page Object Model (POM):** All UI interactions are encapsulated within classes in the `src/pages/` directory. This separates test logic from page-specific code, making tests cleaner and more robust against UI changes.
*   **Logging:** A custom logger is used throughout the framework. Every key action (e.g., "Clicking filter button", "Asserting title is correct") is logged to both the console and a file (`reports/console_logs.log`), which is invaluable for debugging.

### API & UI Integration
*   The `api_client.py` utility is used to make direct API calls (e.g., to get the total number of movies from the backend). This allows for powerful assertions where we can compare UI data with source-of-truth API data.

## 🐛 Defects Found

During test execution, the following issues were identified and documented:

1.  **Defect #1: Pagination Inconsistency**
    *   **Description:** The "Last" page button is sometimes clickable but leads to an empty or error state, especially when the total number of pages is high. The UI does not consistently disable the button as expected.
    *   **Steps to Reproduce:** Navigate to the "Top Rated" category and repeatedly click the "Next" button until near the end. Observe the behavior of the "Last" button.
    *   **Evidence:** Attached in the Allure report under the `test_pagination_breakage` test case.

2.  **Defect #2: Direct Slug Access Failure**
    *   **Description:** Accessing the page directly via a slug (e.g., `.../popular`) results in a blank page or a "No Results" message, as mentioned in the assignment. This breaks deep linking.
    *   **Steps to Reproduce:** Open a new browser tab and navigate to `https://tmdb-discover.surge.sh/popular`.
    *   **Evidence:** Automated in the `test_direct_slug_access` negative test case.

## 🚀 CI/CD Integration Approach

While not implemented here, the approach for integrating this suite into a CI pipeline (e.g., Jenkins, GitLab CI, GitHub Actions) would be as follows:

1.  **Source Control Hook:** The pipeline would be triggered on every pull request to the `main`/`develop` branches.
2.  **Pipeline Stages:**
    *   **Install:** Spin up a clean CI agent (e.g., a Docker container). Install Python and Chrome/Firefox.
    *   **Dependencies:** Run `pip install -r requirements.txt`.
    *   **Execution:** Run the test suite using the `pytest` command.
    *   **Post-actions:**
        *   **Report Generation:** Always generate the Allure report and publish it as a build artifact.
        *   **Notification:** On failure, notify the team via Slack/Email with a link to the failed build report.
3.  **Dockerization:** To ensure consistency, the entire test environment (code, browser, dependencies) would be containerized using a `Dockerfile`. The CI pipeline would simply build and run this image.
4.  **Parallel Execution:** To speed up feedback, tests would be split and run in parallel on multiple CI agents.

---
**Developed by [Aravind P S] for Rapyuta Robotics.**