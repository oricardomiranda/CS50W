import time, string, secrets, unittest, hashlib
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert 
from selenium.common.exceptions import TimeoutException
from .forms import HashForm
from .models import Hash
from capstone.models import User
from random import randint

class TestUtilities(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def create_user(self):
        username = f"testuser{randint(100, 1000)}"
        email = f"testuser{randint(100, 1000)}@example.com"
        password = self.generate_password()
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return user

    def generate_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
    
    
class NavBarNotLogged(TestUtilities):
	
    def logout(self):
        try:
            # Logout
            self.driver.find_element(By.ID, 'logout').click()
            print("Logout")
        except:
            print("No logout was needed for NavBar")
            pass
        
    def test_homepage(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('Ricardo Miranda', self.driver.page_source)
        print("Homepage")

    def test_whoami(self):
        self.driver.find_element(By.ID, 'whoami')
        self.assertIn('WhoAmI', self.driver.page_source)
        print("WhoAmI Navbar")
        
    def test_timeline(self):
        self.driver.find_element(By.ID, 'timelinescroll')
        self.assertIn('Timeline', self.driver.page_source)
        print("Timeline Navbar")
        
    def test_referrals(self):
        self.driver.find_element(By.ID, 'referralscroll')
        self.assertIn('Referrals', self.driver.page_source)
        print("Referrals Navbar")
        
    def test_referme(self):
        self.driver.find_element(By.ID, 'referralscroll')
        self.assertIn('Refer Me', self.driver.page_source)
        print("Refer Me Navbar")
        
    """ def test_cv(self):
        self.driver.find_element(By.ID, 'downloadcv')
        self.assertIn('Download CV', self.driver.page_source)
        print("Download CV Navbar") """
        
if __name__ == "__main__":
    unittest.main()
        
        

        
        

 
class RegisterAndLogin(TestUtilities):

    def test_registration_and_login(self):
        # Create a user
        user = self.create_user()
            
        print("Created test user")
        print("Test user data:")
        print(f'Username: {user.username}')
        print(f'Email: {user.email}')
        print(f'Password: {user.password}')
        
        # Registration
        self.driver.get("http://localhost:8000/register/") 
        self.fill_registration_form(user)
        print("Register user")
		
  		# Dimiss messages alert
        self.dismiss_alert()
        print("Dismiss alert")

		# Registration is successful
        self.wait.until(EC.presence_of_element_located((By.ID, 'whoami')))
        print("Login after register - Index page")
        
   
    def login(self):
        
        user = self.create_user()

        # Logout
        self.driver.find_element(By.ID, 'logout').click()
        print("Logout")
        
        # Login
        self.driver.get("http://localhost:8000/login/") 
        self.fill_login_form(user.username, user.password)
        print("Login")
        
        self.dismiss_alert()
        print("Dismiss alert")
        
        self.wait.until(EC.presence_of_element_located((By.ID, 'whoami')))
        print("Index page after successful login")
        
        
    def fill_registration_form(self, user):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.driver.find_element(By.NAME, "username").send_keys(user.username)
        self.driver.find_element(By.NAME, "email").send_keys(user.email)
        self.driver.find_element(By.NAME, "password").send_keys(user.password)
        self.driver.find_element(By.NAME, "confirmation").send_keys(user.password)
        self.driver.find_element(By.NAME, "confirmation").submit()


    def fill_login_form(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()
        
    def dismiss_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.dismiss()
        except TimeoutException:
            pass
    
    # @staticmethod   
    # def generate_password(length=12):
    #     alphabet = string.ascii_letters + string.digits + string.punctuation
    #     password = ''.join(secrets.choice(alphabet) for i in range(length))
    #     return password

if __name__ == "__main__":
    unittest.main()

class NavBarLogged(TestUtilities):
    
    def test_homepage(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('Ricardo Miranda', self.driver.page_source)
        print("Homepage")

    def test_contacts(self):
        self.driver.find_element(By.ID, 'contacts')
        self.assertIn('Contacts', self.driver.page_source)
        print("Contacts Navbar")
        
    def test_messages(self):
        self.driver.find_element(By.ID, 'messagesscroll')
        self.assertIn('Messages', self.driver.page_source)
        print("Messages Navbar")
        
    def test_timelinepost(self):
        self.driver.find_element(By.ID, 'timelinePost')
        self.assertIn('Timeline Post', self.driver.page_source)
        print("Timeline Post Navbar")
        
    def test_username(self):
        self.driver.find_element(By.ID, 'username')
        #self.assertIn('username', self.driver.page_source)
        print("Username Navbar")
    
    def test_logout(self):
        self.driver.find_element(By.ID, 'logout')
        self.assertIn('Log Out', self.driver.page_source)
        print("Log Out Navbar")
        
if __name__ == "__main__":
    unittest.main()
    
    
class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'capstone/index.html')
        self.assertTemplateUsed(response, 'capstone/layout.html')
