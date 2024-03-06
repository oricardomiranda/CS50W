import os
import pathlib
import unittest
import logging
import uuid
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from capstone.models import User
from selenium.webdriver.common.keys import Keys

class WebpageNaviTests(StaticLiveServerTestCase):

    @classmethod   
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = ChromeOptions()
        chrome_driver_path = "/usr/bin/chromedriver"
        
        cls.selenium.binary_location = "/usr/bin/google-chrome" 
        cls.selenium.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
        cls.selenium.add_argument('--disable-gpu')
        #cls.selenium.add_argument('--headless') #Disable to see the browser
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

    def tearDown(self):
        User.objects.filter(username="testuser").delete()
        super().tearDown()

    def create_test_user(self):
        return User.objects.create_user(
            username="testuser",
            password="12345",
            email="testuser@example.com"
        )

    def test_registration_and_login(self):
        # Create a user
        user = self.create_test_user()

        # Navigate to the registration page
        self.selenium.get(f"{self.live_server_url}/register/")  # adjust the URL as needed

        # Fill in the registration form
        WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys(user.username)

        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys(user.email)

        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys(user.password)
        
        confirmation_password_input = self.selenium.find_element(By.NAME, "confirmation")
        confirmation_password_input.send_keys(user.password)
        confirmation_password_input.send_keys(Keys.ENTER)

    

        # Verify registration success (check for elements on the registration success page)
        #Assert here
        WebDriverWait(self.selenium, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "All Posts")))
        self.assertTrue(self.selenium.find_element(By.PARTIAL_LINK_TEXT, "All Posts").is_displayed())


        # Navigate to the login page
        self.selenium.get(f"{self.live_server_url}/login/")  # adjust the URL as needed

        # Fill in the login form
        login_username_input = self.selenium.find_element(By.NAME, "username")
        login_username_input.send_keys(user.username)

        login_password_input = self.selenium.find_element(By.NAME, "password")
        login_password_input.send_keys("12345")

        # Submit the login form
        login_button = self.selenium.find_element(By.NAME, "login")
        login_button.click()

        # Verify successful login (check for elements on the logged-in user's home page)
        #Assert here
        WebDriverWait(self.selenium, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "All Posts")))
        self.assertTrue(self.selenium.find_element(By.PARTIAL_LINK_TEXT, "All Posts").is_displayed())

        # Logout
        """logout_button = logout_button = WebDriverWait(self.selenium, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Log Out")))
        logout_button.click()"""

if __name__ == "__main__":
    unittest.main()
