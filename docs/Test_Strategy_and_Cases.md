# Test Strategy & Cases

## 1. Testing Strategy

My strategy is risk-based and user-centric. I focused on the features a user interacts with most frequently: finding content (filtering) and browsing it (pagination).

**Phases:**
1.  **Manual Exploration:** To understand the application's behavior and identify the DOM structure for automation.
2.  **API Analysis:** To understand the data source and create robust assertions.
3.  **Automation Scope:** Prioritize core happy paths, key filtering combinations, and the specific negative cases mentioned in the assignment.

## 2. Generated Test Cases & Rationale

I used **Equivalence Partitioning** (e.g., valid/invalid years) and **Boundary Value Analysis** (e.g., min/max rating) to minimize test cases while maximizing coverage.

### **Test Suite: `test_filtering.py`**

*   **`test_filter_by_category_[Popular|Trending|Newest|TopRated]`**
    *   **Why?** These are the primary ways users discover content. Ensuring each category shows different, correctly sorted results is critical.
    *   **Assertion:** Verify the page URL and content section updates. Verify that results are not empty.

*   **`test_search_by_title`**
    *   **Why?** Core user functionality.
    *   **Assertion:** UI results contain the search string. Compare against a direct API search call.

*   **`test_filter_by_type_[Movies|TV_Shows]`**
    *   **Why?** Fundamental content segregation.
    *   **Assertion:** All result cards display the correct type badge.

*   **`test_filter_by_year`**
    *   **Why?** A common filter. Use a recent valid year (e.g., 2023).
    *   **Assertion:** Verify the release year in each result card matches the filtered year.

*   **`test_filter_by_rating`**
    *   **Why?** Quality filter. Test a lower boundary (e.g., rating >= 7).
    *   **Assertion:** The vote average displayed on each card is >= the selected rating.

*   **`test_filter_by_genre`**
    *   **Why?** Tastes are genre-driven.
    *   **Assertion:** Verify that the selected genre is listed in the genres of each result card (requires API cross-check for accuracy).

*   **`test_combined_filters`**
    *   **Why?** Users rarely use one filter. This tests system integration.
    *   **Example:** `Type=Movies + Genre=Action + Year=2022`.
    *   **Assertion:** All conditions are simultaneously satisfied in the results.

### **Test Suite: `test_pagination.py`**

*   **`test_pagination_navigation`**
    *   **Why?** Validate the basic next/previous workflow.
    *   **Assertion:** Page number changes, and the result set is different from the previous page.

*   **`test_pagination_breakage`** (Negative Test)
    *   **Why?** Explicitly tests the known issue mentioned in the assignment.
    *   **Assertion:** After navigating beyond a certain page (e.g., page 10), the "Next" button might become broken, or results fail to load. The test expects this failure and logs it appropriately.

### **Test Suite: `test_negative.py`**

*   **`test_direct_slug_access`**
    *   **Why?** Tests the other known issue.
    *   **Assertion:** Navigating directly to `base_url/popular` results in an error or empty state, not the popular movies page.

*   **`test_search_invalid_title`**
    *   **Why?** Tests application behavior with invalid input.
    *   **Assertion:** Searching for a random string like "xyz123abc" displays a "No results found" message.

## 3. Test Automation Framework

*   **Libraries:**
    *   `pytest`: Core test runner and structure.
    *   `selenium`: Browser automation.
    *   `allure-pytest`: For beautiful, detailed HTML reports with screenshots on failure.
    *   `requests`: For making API calls to the TMDB backend for validation.
    *   `python-dotenv`: For managing environment variables (if needed).

## 4. Patterns Used

*   **Page Object Model (POM):** This is the most critical pattern. It makes the code:
    *   **Maintainable:** If the UI changes, updates are only needed in one place (the Page Class).
    *   **Readable:** Tests read like a user's journey (`discover_page.select_category("Top Rated")`).
    *   **Reusable:** Page methods can be reused across multiple tests.