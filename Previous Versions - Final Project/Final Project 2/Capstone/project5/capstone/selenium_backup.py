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

    def test_title_index(self):
        self.driver.get(file_uri("index.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h1")
        actual_title = title_element.text
        expected_title = "All Posts"
        self.assertEqual(self.driver.title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
    
    def test_title_following(self):
        self.driver.get(file_uri("capstone/templates/capstone/following.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h1")        
        actual_title = title_element.text
        expected_title = "Following"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_title_login(self):
        self.driver.get(file_uri("capstone/templates/capstone/login.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h2")        
        actual_title = title_element.text
        expected_title = "Login"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_title_register(self):
        self.driver.get(file_uri("capstone/templates/capstone/register.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h2")        
        actual_title = title_element.text
        expected_title = "Register"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_title_profile(self):
        self.driver.get(file_uri("capstone/templates/capstone/profile.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h1")        
        actual_title = title_element.text
        expected_title = "{{ username }}'s Profile"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")


   

class WebpageNaviTests(unittest.TestCase):

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
        chrome_options.add_argument('--disable-software-rasterizer')  # Disable software rasterizer
        chrome_options.add_argument('--disable-extensions')  # Disable extensions
        chrome_options.add_argument('--window-size=1920,1080')

        cls.driver = Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, 'driver', None):
            cls.driver.quit()

    def test_navi_following(self):
        self.driver.get(file_uri("capstone/templates/capstone/index.html"))
    
        try:
            navi_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Following")))
            navi_element.click()
            
            actual_title_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
            actual_title = actual_title_element.text
            expected_title = "Following"
            
            self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")
        except Exception as e:
            logging.exception("Error in test_navi_following: %s", str(e))
            raise e




    """def test_navi_index(self):
        self.driver.get(file_uri("capstone/templates/capstone/index.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h1")        
        actual_title = title_element.text
        expected_title = "All Posts"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_navi_login(self):
        self.driver.get(file_uri("capstone/templates/capstone/index.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h2")        
        actual_title = title_element.text
        expected_title = "Login"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_navi_register(self):
        self.driver.get(file_uri("capstone/templates/capstone/index.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h2")        
        actual_title = title_element.text
        expected_title = "Register"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")

    def test_navi_profile(self):
        self.driver.get(file_uri("capstone/templates/capstone/index.html"))
        title_element = self.driver.find_element(By.TAG_NAME, "h1")        
        actual_title = title_element.text
        expected_title = "{{ username }}'s Profile"
        self.assertEqual(actual_title, expected_title, f"Expected title '{expected_title}', but found '{actual_title}'")"""

    """def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        for i in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "3")"""

if __name__ == "__main__":
    unittest.main()
