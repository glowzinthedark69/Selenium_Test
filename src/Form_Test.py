import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestFormSubmission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")

    def test_form_submission(self):
        self.driver.find_element(By.ID, "userName").send_keys("student")
        self.driver.find_element(By.ID, "userEmail").send_keys("test@test.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys(
            "13678 Krameria St.\nThornton, CO\n80602"
        )
        self.driver.find_element(By.ID, "permanentAddress").send_keys(
            "13678 Krameria St.\nThornton, CO\n80602"
        )

        # Since the submit button is at the end of the form, we'll keep a wait before it to ensure all previous
        # operations are complete
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        submit_button.click()

        # Validate that the submission was successful after clicking the Submit button
        try:
            output = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "output"))
            )
            name = output.find_element(By.ID, "name")
            assert "student" in name.text

            email = output.find_element(By.ID, "email")
            assert "test@test.com" in email.text

            # ... other assertions for output
        except TimeoutException:
            self.driver.quit()
            raise Exception("The expected output was not found on the page")

    def test_form_submission_error(self):
        self.driver.find_element(By.ID, "userName").send_keys("student")
        self.driver.find_element(By.ID, "userEmail").send_keys("test#test.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys(
            "13678 Krameria St.\nThornton, CO\n80602"
        )
        self.driver.find_element(By.ID, "permanentAddress").send_keys(
            "13678 Krameria St.\nThornton, CO\n80602"
        )

        # Since the submit button is at the end of the form, we'll keep a wait before it to ensure all previous
        # operations are complete
        submit_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        submit_button.click()

        time.sleep(3)

        # Validate that the submission was unsuccessful after clicking the Submit button
        try:
            email_error = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#userEmail.field-error")
                )
            )

            # Assert that the error field exists
            assert email_error is not None

            # Get the CSS border property of the input field
            border_color = email_error.value_of_css_property("border-color")

            # Print the border color to the console
            print(f"Border color: {border_color}")

            # Assert that the color is what you expect
            assert "rgb(255, 0, 0)" in border_color

            # ... other assertions for output
        except TimeoutException:
            self.driver.quit()
            raise Exception("The expected output was not found on the page")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
