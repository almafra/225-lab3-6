from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest

class TestH5Tag(unittest.TestCase):
    def setUp(self):
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Run in headless mode
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_h5_tag_content(self):
        driver = self.driver
        driver.get("http://10.48.10.147")  # Replace with your actual Cluster IP

        try:
            # Wait up to 10 seconds for the <h5> tag to appear
            h5_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h5"))
            )
            h5_text = h5_element.text
        except TimeoutException:
            self.fail("Timed out waiting for <h5> tag to be present.")
        except NoSuchElementException:
            self.fail("No <h5> tag found on the page.")
        else:
            # Assert that the text of the <h5> tag is as expected
            self.assertEqual("Lab 3-6 Works!", h5_text, "The <h5> tag does not contain the expected text.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
