import os
import pathlib
import unittest
import logging
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


class WebpageTitlesTest(unittest.TestCase):

    @classmethod   
    def setUpClass(cls):
        chrome_options = ChromeOptions()
        chrome_driver_path = "/usr/bin/chromedriver"
        
        chrome_options.binary_location = "/usr/bin/google-chrome" 
        chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        cls.driver = Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
            
    def test_all_titles(self):
        test_cases = [
            {"url": "capstone/templates/capstone/index.html", "expected_title": "All Posts"},
            {"url": "capstone/templates/capstone/following.html", "expected_title": "Following"},
            {"url": "capstone/templates/capstone/login.html", "expected_title": "Login"},
            {"url": "capstone/templates/capstone/register.html", "expected_title": "Register"},
            {"url": "capstone/templates/capstone/profile.html", "expected_title": "{{ username }}'s Profile"},
        ]

        for test_case in test_cases:
            self.driver.get(file_uri(test_case["url"]))
            title_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1")))
            actual_title = title_element.text
            expected_title = test_case["expected_title"]
            self.assertEqual(
                actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}' for URL: {test_case['url']}"
            )

        

if __name__ == "__main__":
    unittest.main()
