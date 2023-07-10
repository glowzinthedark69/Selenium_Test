from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_can_perform_search(self):
        # Visit DuckDuckGo
        self.driver.get("https://duckduckgo.com")

        # Type "Cypress" into the search box and submit
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Cypress")
        search_box.submit()

        # Assert that results are shown
        results = self.driver.find_element(By.ID, "r1-0")
        self.assertTrue(results.is_displayed())

        # Assert that the first result contains the word "Cypress"
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="result-extras-url-link"]')))

        # Check if any of the result links have the href attribute "https://www.cypress.io"
        hrefs = [result.get_attribute("href") for result in results]
        self.assertTrue(any("https://www.cypress.io" in href for href in hrefs))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
