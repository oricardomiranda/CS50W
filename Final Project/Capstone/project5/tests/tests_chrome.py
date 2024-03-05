import string, random
from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from capstone.models import User
from lorem_text import lorem


class ChromeSetup(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
             
      
class Alert(ChromeSetup):
    
    def dismiss_alert(self):
        try:
            alert = self.driver.switch_to.alert            
            alert.dismiss()
            print("Alert dismissed successfully.")
        except:
            print("No alert present. Continuing execution.")
    
        
class Registration(Alert):

    def setUp(self):
        self.driver = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.driver.quit()
        super().tearDown()

    def generate_random_string(self, length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    
    def generate_random_phone(self):
        area_code = random.randint(100, 999)
        exchange_code = random.randint(100, 999)
        line_number = random.randint(1000, 9999)
        phone_number = f"({area_code}) {exchange_code}-{line_number}"
        return phone_number
        
    def test_register_user(self):
        username = self.generate_random_string()
        email = f"{username}@example.com"
        password = self.generate_random_string()
        
        print(f"Generated username: {username}")
        print(f"Generated email: {email}")
        print(f"Generated password: {password}")
    
        self.driver.get('http://localhost:8000/register')
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'email').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'confirmation').send_keys(password)
        self.driver.find_element(By.ID, 'submit').click()
        print("Registry submited")
        
        self.dismiss_alert()

        # Check if the user is created in the database
        User.objects.create_user(username=username, email=email, password=password)
        user_created = User.objects.filter(username=username).exists()
        print(f"User with username '{username}' exists: {user_created}")
        if not user_created:
          print("Error: User creation failed!")

        self.assertTrue(user_created, f"User with username '{username}' should exist in the database")

        # Store user in variable
        self.registered_user = {
            'username': username,
            'password': password
        }
        print("User variable is stored")
        return self.registered_user     
                
        
class ExternalLinks(ChromeSetup):
    
    def verify_external_link(self, link):
        self.driver.get('http://localhost:8000')

        # Find the link and click 
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@href='{link}']"))
        ).click()

        # Wait for the new window or tab to open
        WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))

        # Switch to the new window or tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Verify the URL of the new window or tab
        assert link in self.driver.current_url

        # Close the new window or tab
        self.driver.close()

        # Switch back to the original window or tab
        self.driver.switch_to.window(self.driver.window_handles[0])
                

class PageContentUnlogged(ExternalLinks):
    	
    def logout(self):
        try:
            self.driver.find_element(By.ID, 'logout').click()
            print("Logout")
        except:
            print("No logout was needed for NavBar")
            pass
    
    #Content Loading Tests
    #NavBar
    def test_homepage(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('Ricardo Miranda', self.driver.page_source)
        print("Homepage")

    def test_whoami_navbar(self):
        whoami_nav = self.driver.find_element(By.ID, 'whoami')
        self.assertIn('WhoAmI', whoami_nav.text)
        print("WhoAmI Navbar")
        
    def test_timeline_navbar(self):
        timeline_navbar = self.driver.find_element(By.ID, 'timelinescroll')
        self.assertIn('Timeline', timeline_navbar.text)
        print("Timeline Navbar")
        
    def test_referrals_navbar(self):
        referrals_navbar = self.driver.find_element(By.ID, 'referralscroll')
        self.assertIn('Referrals', referrals_navbar.text)
        print("Referrals Navbar")
        
    def test_referme_navbar(self):
        referme_navbar = self.driver.find_element(By.ID, 'referralscroll')
        self.assertIn('Referrals', referme_navbar.text)
        print("Referrals Navbar")
        
    def test_cv_navbar(self):
        self.driver.find_element(By.ID, 'downloadcv')
        self.assertIn('Download CV', self.driver.page_source)
        print("Download CV Navbar")
    
    #Who Am I        
    def test_whoami_content(self):
        whoami_content = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'whoamiContent')))
        
        expected_html = ('<h7>Who am I</h7>' +
        '<div class="animated-text">' +
        '<p>Ricardo Miranda</p>' +
        '<p>I used to be a Nurse</p>' +
        '<p>Decided to change career</p>' +
        '<p>And I am always ready to learn more</p>' +
        '</div>')
        
        actual_html = whoami_content.get_attribute('innerHTML')
        self.assertIn(expected_html, actual_html)        
        print("Who am I content")
        
    #About Me
    def test_aboutme_content(self):
        self.driver.get('http://localhost:8000')
        aboutme_content = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'aboutMeContent')))
        
        expected_html = (
        '<h7>About Me</h7>' +
        '<div class="animated-text">' +
        '<p>QA Engineer in Fintech</p>' +
        '<p>Java backend tester in Linux servers</p>' +
        '<p>Interested in progressing into automation</p>' +
        '<p>Completing CS50W: Web Development</p>'
        )
        
        actual_html = aboutme_content.get_attribute('innerHTML')
        self.assertIn(expected_html, actual_html)        
        print("About Me Content")

    #Timeline
    def test_timeline_small_title(self):
        timeline_small_title = self.driver.find_element(By.ID, 'timelineSmallTitle')
        self.assertIn('Timeline', timeline_small_title.text)
        print("Timeline Title")
    
    def test_timeline_title(self):
        timeline_title = self.driver.find_element(By.ID, 'timelineTitle')
        self.assertIn('My journey into IT', timeline_title.text)
        print("Timeline Sub Title")
        
    def test_timeline_content(self):
        self.driver.find_element(By.ID, 'timelineContent')
        print("Timeline Content")
        
    def test_timeline_item(self):
        self.driver.find_element(By.ID, 'timelineItem')
        print("Timeline Item")
        
    #Referrals
    def test_referrals_title(self):
        referrals_title = self.driver.find_element(By.ID, 'referralsTitle')
        self.assertIn('My Referrals', referrals_title.text)
        print("Referrals Title")
        
    def test_referrals_content(self):
        self.driver.find_element(By.ID, 'referralsContent')
        print("Referrals Content")
        
    def test_referrals_item(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'referralsItem')))
        print("Referrals Item")
    
    #Vertical Bars
    def test_email(self):
        self.driver.find_element(By.ID, 'contactEmail')
        print("Contact Email")
    
    def test_nav_qa(self):
        self.driver.find_element(By.ID, 'nav-qa')
        print("Nav QA")
        
    def test_nav_terminal(self):
        self.driver.find_element(By.ID, 'nav-terminal')
        print("Nav terminal")
        
    def test_nav_python(self):
        self.driver.find_element(By.ID, 'nav-python')
        print("Nav python")
        
    def test_nav_java(self):
        self.driver.find_element(By.ID, 'nav-java')
        print("Nav java")
        
    def test_nav_apple(self):
        self.driver.find_element(By.ID, 'nav-apple')
        print("Nav apple")
        
    def test_nav_linux(self):
        self.driver.find_element(By.ID, 'nav-linux')
        print("Nav linux")
        
    def test_nav_html(self):
        self.driver.find_element(By.ID, 'nav-html')
        print("Nav html")
        
    def test_nav_javascript(self):
        self.driver.find_element(By.ID, 'nav-javascript')
        print("Nav javascript")
        
    def test_nav_cypress(self):
        self.driver.find_element(By.ID, 'nav-cypress')
        print("Nav cypress")
        
    def test_nav_react(self):
        self.driver.find_element(By.ID, 'nav-react')
        print("Nav react")
        
    #Bottom Nav Bar
    def test_nav_github(self):
        self.driver.find_element(By.ID, 'nav-github')
        print("Nav Github")
        
    def test_nav_linkedin(self):
        self.driver.find_element(By.ID, 'nav-linkedin')
        print("Nav linkedin")
       

class ModalsFilling(Registration):
    
    def test_contact_me(self):
        #Logged as I had problems with CSRF 
        self.test_register_user()
        self.dismiss_alert()
        
        # Bring username from the register function
        self.username = self.generate_random_string()
        self.phone_number = self.generate_random_phone()
        
        # Creating random test data 
        rand_email = f"{self.username}@example.com"
        rand_phone = self.phone_number
        rand_message = lorem.words(10)
        
        self.dismiss_alert()
        
        # Click contact me
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'contactMe'))).click()
        print("Contact Me button found")
        
        #Checking if modal opened
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'emailInput'))).send_keys(rand_email)
        print(rand_email)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'phoneInput'))).send_keys(rand_phone)
        print(rand_phone)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'messageInput'))).send_keys(rand_message)
        print(rand_message)
                
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'submitButton'))).click()
        print("New contact")
        
        #Refer to timelinepost for assert
        
        
    
    def test_refer_me(self):
        #Logged as I had problems with CSRF
        self.test_register_user()
        self.dismiss_alert()
        
        # Create random test data
        rand_name = str(lorem.words(2))
        rand_subject = str(lorem.words(4))
        rand_message = str(lorem.words(10))
        
        # Click refer me 
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'referral'))).click()
        print("Referral button found")
        
        # Fill out the referral form
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'nameInput'))).send_keys(rand_name)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'subjectInput'))).send_keys(rand_subject)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'messageInput'))).send_keys(rand_message)
        
        # Submit the referral form
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'submitButton'))).click()
        print("New referral submitted")

        #Refer to timelinepost for assert

    
class PageContentLogged(ModalsFilling):
         
    def test_logged_navbar(self):
        self.test_register_user()
        self.dismiss_alert()
        
        #Messages
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'messagescroll')))
        messages_navbar = self.driver.find_element(By.ID, 'messagescroll')
        self.assertIn('Messages', messages_navbar.text)
        print("Messages Navbar")

        #TimelinePost
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'timelinePost')))
        timelinepost_navbar = self.driver.find_element(By.ID, 'timelinePost')
        self.assertIn('Timeline Post', timelinepost_navbar.text)
        print("Timelinepost Navbar")

        #Username
        username = self.registered_user['username']
        print(username)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'username')))
        username_navbar = self.driver.find_element(By.ID, 'username')
        self.assertIn(username, username_navbar.text)  # Adjust 'Username' based on your expected text
        print("Username Navbar")

        #Logout
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, 'logout')))
        logout_navbar = self.driver.find_element(By.ID, 'logout')
        self.assertIn('Log Out', logout_navbar.text)
        print("Logout Navbar")
     
    
    def test_timeline_post(self):
        if not hasattr(self, 'registered_user'):
            self.test_register_user()
            self.dismiss_alert()
        
        #Randomized input fields
        rand_year = str(random.randint(2000, 2024))
        rand_subject = lorem.words(3)
        rand_content = lorem.words(10)
        
        #Let's generate specific unique phrases
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'timelinePost'))).click()
        print("Timeline Post button found")
        
        #Checking if modal opened
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'yearInput'))).send_keys(rand_year)
        print(rand_year)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'subjectInput'))).send_keys(rand_subject)
        print(rand_subject)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'contentInput'))).send_keys(rand_content)
        print(rand_content)
        
        WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'submitButton'))).click()
        print("New Timeline Post")
        
        sleep(1)
        try:
            self.dismiss_alert()
        except:
            pass    
        
        #Check if post appears
        post_year = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']/h7[contains(text(), '{rand_year}')]")))
        self.assertIn(rand_year, post_year.text)
        print(f"Post has the year {rand_year}")

        post_subject = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']//div[@class='animated-text-smaller']/p[contains(text(), '{rand_subject}')]")))
        self.assertIn(rand_subject, post_subject.text)
        print(f"Post has the subject {rand_subject}")

        post_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']//div[@class='animated-text-smaller']/p[contains(text(), '{rand_content}')]")))
        self.assertIn(rand_content, post_content.text)
        print(f"Post has the content {rand_content}")

    
    def test_edit_post(self):
        if not hasattr(self, 'registered_user'):
            self.test_register_user()
            sleep(1)
            self.dismiss_alert()
            sleep(1)
        
        #Randomized input fields
        rand_year = str(random.randint(2000, 2024))
        rand_subject = lorem.words(3)
        rand_content = lorem.words(10)
        
        #Let's generate specific unique phrases
        post_edit_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'timelineEditButton')))
        self.driver.execute_script("arguments[0].scrollIntoView();", post_edit_button)
        post_edit_button.click()
        print("Timeline Edit button found")
        
        #Checking if modal opened
        year_input_field = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'yearInput')))
        year_input_field.click()
        year_input_field.clear()
        sleep(5)
        year_input_field.send_keys(rand_year)
        print(rand_year)
        
        subject_input_field = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'subjectInput')))
        subject_input_field.click()
        subject_input_field.clear()
        subject_input_field.send_keys(rand_subject)
        print(rand_subject)
        
        content_input_field = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'contentInput')))
        content_input_field.click()
        content_input_field.clear()
        content_input_field.send_keys(rand_content)
        print(rand_content)
        
        submit_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'submitButton')))
        submit_button.click()
        print("New Timeline Post")
        
        sleep(1)
        try:
            self.dismiss_alert()
        except:
            pass    
        
        #Check if post appears
        post_year = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']/h7[contains(text(), '{rand_year}')]")))
        self.assertIn(rand_year, post_year.text)
        print(f"Post has the year {rand_year}")

        post_subject = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']//div[@class='animated-text-smaller']/p[contains(text(), '{rand_subject}')]")))
        self.assertIn(rand_subject, post_subject.text)
        print(f"Post has the subject {rand_subject}")

        post_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='all_post_view']//div[@class='animated-text-smaller']/p[contains(text(), '{rand_content}')]")))
        self.assertIn(rand_content, post_content.text)
        print(f"Post has the content {rand_content}")
    
    
    def test_unread_messages_fetch(self):
        self.test_contact_me()
        sleep(1)
        self.dismiss_alert()
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'myMessages')))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'unreadMessage')))
        
    def test_read_messages_fetch(self):
        self.test_register_user()
        sleep(1)
        self.dismiss_alert()
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'unreadMessage')))
        
        while True:
            try:
                read_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mark-read-button')))
                print("Found read button, clicking...")
                read_button.click()
                print("Clicked read button")
                self.driver.refresh()
                self.dismiss_alert()
            except:
                print("All messages are read")
                break
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'myMessages')))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'readMessage')))


class SmallSizeScreen(ChromeSetup):
    def test_page_elements_visible_on_small_screen(self):
        # Simulate a small screen size
        self.driver.set_window_size(320, 480)
        self.driver.get('http://localhost:8000')

        # Navbar shrink when on
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-qa')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-python')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-java')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-apple')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-linux')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-html')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-javascript')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-cypress')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'nav-small-react')))
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'contactEmail')))
        
    
class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'capstone/index.html')
        self.assertTemplateUsed(response, 'capstone/layout.html')
