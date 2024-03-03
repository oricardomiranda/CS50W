import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Use the ChromeService to set the executable path for ChromeDriver
        chrome_options = ChromeOptions()
        chrome_options.binary_location ='/Applications/Chromium'
        cls.driver = Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver after all tests are executed
        cls.driver.quit()

    def test_title(self):
        self.driver.get(file_uri("counter.html"))
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        for i in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "3")

if __name__ == "__main__":
    unittest.main()
