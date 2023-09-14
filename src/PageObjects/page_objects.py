import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        self.user_name_field = (By.ID, "userName")
        self.user_email_field = (By.ID, "userEmail")
        self.current_address_field = (By.ID, "currentAddress")
        self.permanent_address_field = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_validation = (By.ID, "output")
        self.name_validation_locator = (By.ID, "name")
        self.email_validation_locator = (By.ID, "email")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, user_name, user_email, current_address, permanent_address):
        self.driver.find_element(*self.user_name_field).send_keys(user_name)
        self.driver.find_element(*self.user_email_field).send_keys(user_email)
        self.driver.find_element(*self.current_address_field).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_field).send_keys(permanent_address)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        submit_button.click()

    def form_success_validation(self):
        output = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.output_validation)
        )
        name_validation = output.find_element(*self.name_validation_locator)
        email_validation = output.find_element(*self.email_validation_locator)
        # Extract other elements if needed...

        return {
            "name": name_validation.text,
            "email": email_validation.text
            # Add other extracted data if needed...
        }

    def form_error_validation(self):
        email_error = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail.field-error"))
        )
        border_color = email_error.value_of_css_property("border-color")
        return {
            "error_element": email_error,
            "border_color": border_color
        }
    # In your test class:
