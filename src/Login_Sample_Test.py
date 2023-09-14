import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.PageObjects.Login_Sample_Test_Objects import LoginPage


class BaseTest(unittest.TestCase):
    # Each test will automatically open a new browser window at the start and close it at the end when inherited
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class TestSuccessfulLogin(BaseTest):

    def setUp(self):
        super().setUp()  # This will call the setUp method of BaseTest
        self.test_page = LoginPage(self.driver)
        self.test_page.open()

    def test_successful_login(self):
        self.test_page.fill_form(
            "student",
            "Password123")

        # Submit the form
        self.test_page.submit_form()
        time.sleep(5)
        self.test_page.validate_successful_login()


if __name__ == "__main__":
    unittest.main()
