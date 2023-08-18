import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.PageObjects.Login_Sample_Test_Objects import LoginPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


class TestLoginFunction(BaseTest):

    def setUp(self):
        super().setUp()  # This will call the setUp method of BaseTest
        self.test_page = LoginPage(self.driver)
        self.test_page.open()

    def test_form_submission(self):
        self.test_page.fill_form(
            "student",
            "Password123")

        # Submit the form
        self.test_page.submit_form()

    def test_login(self):
        driver = webdriver.Chrome()  # corrected line
        # maximize window
        driver.maximize_window()
        # open the website
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # locating username field and keying in the username
        username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "username"))
        )
        username.send_keys("student")

        # locating password field and keying in the password
        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password.send_keys("Password123")

        # locating login button and clicking it to login
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        login_button.click()

        # Pause the execution of the script for 5 seconds
        time.sleep(5)

        # Check if the login was successful by validating the presence of a logout button
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )

        # Assert that the logout button is displayed, meaning a successful login
        assert logout_link.is_displayed()

        # Attempt to locate the text element
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//*[text()='Congratulations student. You successfully logged in!']",
                    )
                )
            )
        except TimeoutException:
            driver.quit()
            raise Exception("The expected text was not found on the page")

        # close the driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()
