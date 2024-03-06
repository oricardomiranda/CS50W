import os
import pathlib
import unittest
import logging
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebpageNaviTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = ChromeOptions()
        chrome_driver_path = "/usr/bin/chromedriver"

        cls.selenium.binary_location = "/usr/bin/google-chrome"
        cls.selenium.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
        cls.selenium.add_argument('--disable-gpu')
        cls.selenium.add_argument('--headless') #Disable to see the browser
        cls.selenium.add_argument('--no-sandbox')
        cls.selenium.add_argument('--disable-dev-shm-usage')
        cls.selenium.add_argument('--disable-software-rasterizer')
        cls.selenium.add_argument('--disable-extensions')
        cls.selenium.add_argument('--window-size=1920,1080')

        try:
            cls.chrome_version = cls.selenium.capabilities.get('browserVersion', 'unknown')
        except KeyError:
            cls.chrome_version = 'unknown'

        cls.selenium = Chrome(options=cls.selenium)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_navi_all_posts(self):
        self.selenium.get(f"{self.live_server_url}")

        try:
            navi_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "About")))
            navi_element.click()

            actual_title_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Who am I")))
            actual_title = actual_title_element.text
            expected_title = "Who am I"

            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
        except Exception as e:
            logging.exception("Error in test_navi_following: %s", str(e))
            raise e

    def test_navi_login(self):
        self.selenium.get(f"{self.live_server_url}")

        try:
            navi_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Experience")))
            navi_element.click()

            actual_title_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Career")))
            actual_title = actual_title_element.text
            expected_title = "Career"

            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
        except Exception as e:
            logging.exception("Error in test_navi_following: %s", str(e))
            raise e

    def test_navi_register(self):
        self.selenium.get(f"{self.live_server_url}")

        try:
            navi_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Work")))
            navi_element.click()

            actual_title_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Who am I")))
            actual_title = actual_title_element.text
            expected_title = "Who am I"

            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
        except Exception as e:
            logging.exception("Error in test_navi_following: %s", str(e))
            raise e

    def test_navi_capstone(self):
        self.selenium.get(f"{self.live_server_url}")

        try:
            navi_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Contact Me")))
            navi_element.click()

            actual_title_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Email address")))
            actual_title = actual_title_element.text
            expected_title = "Email address"

            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
        except Exception as e:
            logging.exception("Error in test_navi_following: %s", str(e))
            raise e

if __name__ == "__main__":
    unittest.main()
