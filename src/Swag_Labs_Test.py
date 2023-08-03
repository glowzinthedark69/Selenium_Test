import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_website_login():
    # Create a new instance of the Chrome driver.
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the website we want to test.
    driver.get("https://www.saucedemo.com/")
    # time.sleep(2)

    # Assert that the current URL is the homepage
    assert "saucedemo.com" in driver.current_url
    # time.sleep(2)

    # Assert that the "Test login" heading" exists on the page as expected
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "login_logo"))).text == "Swag Labs"

    # Assert that the credentials fields exists on the page as expected, and we can type into them
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    username_input.send_keys("standard_user")
    assert username_input.get_attribute("value") == "standard_user"
    # time.sleep(2)

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")
    assert password_input.get_attribute("value") == "secret_sauce"
    # time.sleep(2)

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
    login_button.click()
    # time.sleep(2)

    # Assert that the current URL is the logged-in-successfully page
    assert "/inventory.html" in driver.current_url

    # Assert that the login was successful
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))).text == "Swag Labs"

    driver.quit()  # Close the browser


if __name__ == "__main__":
    test_website_login()
