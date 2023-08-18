import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_objects import TextBoxPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


class TestFormSubmission(BaseTest):
    def setUp(self):
        super().setUp()  # This will call the setUp method of BaseTest
        self.text_box_page = TextBoxPage(self.driver)
        self.text_box_page.open()

    def test_form_submission(self):
        self.text_box_page.fill_form(
            "student",
            "test@test.com",
            "13678 Krameria St.\nThornton, CO\n80602",
            "13678 Krameria St.\nThornton, CO\n80602")

        # Submit the form
        self.text_box_page.submit_form()

        try:
            validation_data = self.text_box_page.form_success_validation()

            assert "student" in validation_data["name"]
            assert "test@test.com" in validation_data["email"]

            # Add other assertions if needed...
        except TimeoutException:
            self.driver.quit()
            raise Exception("The expected output was not found on the page")
        # Continue the rest of the test...

    def test_form_submission_fail(self):
        self.text_box_page.fill_form(
            "student",
            "test#test.com",
            "13678 Krameria St.\nThornton, CO\n80602",
            "13678 Krameria St.\nThornton, CO\n80602")

        # Submit the form
        self.text_box_page.submit_form()
        time.sleep(3)

        try:
            error_validation_data = self.text_box_page.form_error_validation()

            # Assert that the error field exists
            assert error_validation_data["error_element"] is not None

            # Assert that the color is what you expect
            # print("Actual border color:", error_validation_data["border_color"])
            assert "rgb(255, 0, 0)" in error_validation_data["border_color"]

            # Add other assertions if needed...
        except TimeoutException:
            self.driver.quit()
            raise Exception("The expected output was not found on the page")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# Previous version of test without using page object model

# class TestFormSubmissions(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://demoqa.com/text-box")
#
#     def test_form_submission(self):
#         self.driver.find_element(By.ID, "userName").send_keys("student")
#         self.driver.find_element(By.ID, "userEmail").send_keys("test@test.com")
#         self.driver.find_element(By.ID, "currentAddress").send_keys(
#             "13678 Krameria St.\nThornton, CO\n80602"
#         )
#         self.driver.find_element(By.ID, "permanentAddress").send_keys(
#             "13678 Krameria St.\nThornton, CO\n80602"
#         )
#
#         # Since the submit button is at the end of the form, we'll keep a wait before it to ensure all previous
#         # operations are complete
#         submit_button = WebDriverWait(self.driver, 5).until(
#             EC.element_to_be_clickable((By.ID, "submit"))
#         )
#         submit_button.click()
#
#         # Validate that the submission was successful after clicking the Submit button
#         try:
#             output = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located((By.ID, "output"))
#             )
#             name = output.find_element(By.ID, "name")
#             assert "student" in name.text
#
#             email = output.find_element(By.ID, "email")
#             assert "test@test.com" in email.text
#
#             # ... other assertions for output
#         except TimeoutException:
#             self.driver.quit()
#             raise Exception("The expected output was not found on the page")
#
#     def test_form_submission_error(self):
#         self.driver.find_element(By.ID, "userName").send_keys("student")
#         self.driver.find_element(By.ID, "userEmail").send_keys("test#test.com")
#         self.driver.find_element(By.ID, "currentAddress").send_keys(
#             "13678 Krameria St.\nThornton, CO\n80602"
#         )
#         self.driver.find_element(By.ID, "permanentAddress").send_keys(
#             "13678 Krameria St.\nThornton, CO\n80602"
#         )
#
#         # Since the submit button is at the end of the form, we'll keep a wait before it to ensure all previous
#         # operations are complete
#         submit_button = WebDriverWait(self.driver, 5).until(
#             EC.element_to_be_clickable((By.ID, "submit"))
#         )
#         submit_button.click()
#
#         time.sleep(3)
#
#         # Validate that the submission was unsuccessful after clicking the Submit button
#         try:
#             email_error = WebDriverWait(self.driver, 5).until(
#                 EC.presence_of_element_located(
#                     (By.CSS_SELECTOR, "#userEmail.field-error")
#                 )
#             )
#
#             # Assert that the error field exists
#             assert email_error is not None
#
#             # Get the CSS border property of the input field
#             border_color = email_error.value_of_css_property("border-color")
#
#             # Assert that the color is what you expect
#             assert "rgb(255, 0, 0)" in border_color
#
#             # ... other assertions for output
#         except TimeoutException:
#             self.driver.quit()
#             raise Exception("The expected output was not found on the page")
#
#     def tearDown(self):
#         self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()
