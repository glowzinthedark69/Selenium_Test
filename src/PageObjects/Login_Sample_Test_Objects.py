import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicetestautomation.com/practice-test-login/"
        self.user_name_field = (By.ID, "username")
        self.user_password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.login_message = (By.XPATH,
                              "//*[text()='Congratulations student. You successfully logged in!']")
        self.logout_button = (By.LINK_TEXT, "Log out")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, user_name, user_password):
        # Wait for the 'userName' field to be present before interacting with it
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.user_name_field)
        )
        self.driver.find_element(*self.user_name_field).send_keys(user_name)

        # Similarly, wait for the 'password' field
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.user_password_field)
        )
        self.driver.find_element(*self.user_password_field).send_keys(user_password)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        submit_button.click()

    def get_login_success_message(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.login_message))

    def get_logout_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_button))

    def validate_successful_login(self):
        # Check if the login message is displayed
        assert self.get_login_success_message().is_displayed(), "Login success message not displayed"

        # Check if the logout button is displayed
        assert self.get_logout_button().is_displayed(), "Logout button not displayed"

    # def form_error_validation(self):
    #     email_error = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail.field-error"))
    #     )
    #     border_color = email_error.value_of_css_property("border-color")
    #     return {
    #         "error_element": email_error,
    #         "border_color": border_color
    #     }
    # In your test class:
