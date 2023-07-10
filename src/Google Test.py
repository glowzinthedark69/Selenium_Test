import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_website():
    # Create a new instance of the Chrome driver.
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the website we want to test.
    driver.get("https://www.google.com/")

    # Find the search bar and enter a search term.
    search_bar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    search_bar.send_keys("Selenium")

    # Click the search button. Google's search can be triggered by hitting the ENTER key.
    search_bar.send_keys(Keys.RETURN)
    print(driver.current_url)

    # Wait for the search results to load.
    time.sleep(3)

    # Check that the search results page contains the search term.
    assert "Selenium" in driver.page_source

    # Close the driver.
    driver.quit()


if __name__ == "__main__":
    test_website()
