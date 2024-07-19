# Capstone

Final Project of [CS50 Web Programming with Python and JavaScript](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/)
[Full project specification](https://cs50.harvard.edu/web/2020/projects/final/capstone/)

The main idea implemented in this project was to create a personal portfolio that would allow recruiters, colleagues and other coders to be able to reach me and check my work


# Distinctiveness and Complexity:

My project satisfies the distinctiveness and complexity requirements by offering a unique and innovative approach to building a personal portfolio website. Here's why:

1. **Unique Design Inspired by Linux Terminal:** The layout of my portfolio website is inspired by the Linux terminal, giving it a distinct and memorable aesthetic. This unique design sets it apart from traditional portfolio websites and makes it stand out to visitors.

2. **Interactive Features:** I have implemented various interactive features such as clickable icons, dynamic navigation bars, and modal forms for contact and referral submissions. These features enhance user engagement and provide a modern and immersive browsing experience.

3. **Dynamic Content Management:** Users can register, log in, and perform actions such as adding, editing, and deleting timeline posts and referrals. This dynamic content management system adds complexity to the project and allows users to customize their experience on the website.

4. **Automated Testing:** To ensure the robustness of my application, I have implemented automated testing using Selenium WebDriver. This demonstrates a commitment to quality assurance and adds a layer of complexity to the project's development process.

Overall, my project combines unique design elements, interactive features, dynamic content management, and automated testing to create a distinct and complex personal portfolio website.

**Contents of Each File:**

- **`README.md`:** Contains project writeup, including distinctiveness and complexity analysis, file descriptions, instructions for running the application, and additional information.

- **`requirements.txt`:** Lists all Python packages required to run the web application.

- **`Capstone/`:** Main directory containing the Django project files.

- **`Capstone/project5/`:** Django app directory containing application-specific files.

- **`Capstone/project5/static/` and `Capstone/project5/templates/`:** Directories for static files (e.g., CSS, JavaScript) and HTML templates used in the application.

- **`Capstone/project5/tests.py`:** Python script containing automated tests using Selenium WebDriver to ensure the functionality and reliability of the application.

- **Other files:** Various Django-related files such as `models.py`, `views.py`, `urls.py`, and `forms.py` for defining models, views, URLs, and forms, respectively.



# How to run the application
First, clone this repository:

```bash
git clone https://github.com/oricardomiranda/CS50W/tree/34dedce4af8e1cba0112960b6c1939c4cf67d32a/Final%20Project/

cd capstone
```

Install dependencies:
```bash
pip3 install -r requirements.txt
```

To run the development server:
```bash
python manage.py runserver
```

Access the application in your web browser at http://localhost:8000

## Requirements
This website was built using [Django](https://github.com/django/django)
The backend of this website is coded in Python
The frontend of this website is codd in Javascript
The application must be mobile-responsive


# Additional Information

## Specifications

### Register and Login
Both actions are only accessible by url to the layout can be kept clean

### Layout
This project's layout is based on my day to day work tool which is the Linux terminal.
I took inspiration from my terminal customisation which was taken from [Pixegami](https://github.com/pixegami/terminal-profile)

![Pixegami's terminal inspired](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/layout.png?raw=true)

The projects layout in considered minimalistic, leading to a quick and nice reading

- On the top we have a navigation bar

- To the left we have a bunch of clickable icons, representing some learned hardskills

- At the bottom we have the socials, containing my Linkedin and Github accounts

- To the right we have my contact email

This layout is also mobile compatible

- The top bar becomes a dropdown menu and the left and right bars go to the top

### Color palette

| Color          | Hex                                                                |
| -------------- | ------------------------------------------------------------------ |
| Navy           | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) `#0a192f` |
| Light Navy     | ![#172a45](https://via.placeholder.com/10/0a192f?text=+) `#172a45` |
| Lightest Navy  | ![#303C55](https://via.placeholder.com/10/303C55?text=+) `#303C55` |
| Slate          | ![#8892b0](https://via.placeholder.com/10/8892b0?text=+) `#8892b0` |
| Light Slate    | ![#a8b2d1](https://via.placeholder.com/10/a8b2d1?text=+) `#a8b2d1` |
| Lightest Slate | ![#ccd6f6](https://via.placeholder.com/10/ccd6f6?text=+) `#ccd6f6` |
| White          | ![#e6f1ff](https://via.placeholder.com/10/e6f1ff?text=+) `#e6f1ff` |
| Green          | ![#64ffda](https://via.placeholder.com/10/64ffda?text=+) `#64ffda` |

### Top Navigation Bar
With two options for logged or unlogged, this bar allows the user to navigate and interact with the page

#### Unlogged view
![Unlogged](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2018.33.06.png?raw=true)

#### Logged view
![Logged](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.07.44.png?raw=true)

- WhoAmI - Scrolls to the top where we can view the Who Am I and About Me sections

- Timeline - Scrolls to the Timeline area

- Referrals - Scrolls to the Referrals area

- Contact Me - Opens a modal to enter a contact form

- Refer Me - Opens a modal that allows any viewer to create a referral to the page owner

- Download CV - Links to a pdf CV file

- Messages - Scrolls to the Messages area

- Timeline Post - Opens a modal to create a new Timeline post

- Username - Displays the logged user

- Log Out - Logs out of the current session

### Left Navigation Bar
![Left Nav Bar](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.07.18.png?raw=true)

Every link is clickable and allows to check the content related to the icon

### Bottom Navigation Bar
![Bottom Nav Bar](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.07.28.png?raw=true)

These two links are clickable and link to the social networks

### Right nav bar
![Right Nav Bar](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2018.57.36.png?raw=true)

Non clickable. Just allows to know the email contact

### Who am I and About Me

Area where the name is present in a bigger and brighter letter
A small introduction is presented

Catch phrase in bigger and brighter letter
A small tech bio in described

![Who am I](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.07.59.png?raw=true)

### Timeline

![Journey](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2018.33.22.png?raw=true)

#### My journey into IT
In this area I present all my job and school episodes

Added by using the Timeline Post button. Each post contains:
- Year

- Subject

- Content

Year is presented in a small green font
Subject is presented in a bigger and brighter font
Content is presented in a small and duller font

All posts are ordered by descending year

#### Logged view

![Logged journey](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.08.15.png?raw=true)

For logged users, we have an additional view with two buttons
- Edit - Opens a modal that loads the current data and allows to edit and save

- Delete - Deletes the current post

### Referrals

![Referrals](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2018.33.30.png?raw=true)

In this area any viewer can post a referral about the page owner. Random order is applied

- Year is presented in a small green font

- Subject is presented in a bigger and brighter font

- Content is presented in a small and duller font

#### Logged view

To prevent bad intentions, the owner has a way to remove any referrals using the delete button

![Logged Referrals](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.08.58.png?raw=true)

### Messages

- The viewer is able to send a message to the owner with the Contact Me button

- The received messages are only visible when logged in

- The messages as displayed by ID

- The unread messages are presented with brighter font

- Unread messages have a Mark As Read button

- After clicking the Mark As Read button, the text becomes duller

![Messages](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.10.41.png?raw=true)

When loading the logged page, if there are unread messages, an alert is displayed

## Testing

As suggested in the Lecture, I opted for Selenium webdriver to create the automation testing.

### Test Coverage
#### Browser setup
- The chosen browser was Chromium due to its fixed versioning that aids when automating with GitHub Actions

- Other test suites were created for Chrome, Firefox and Edge. Safari is on hold due to issues with sessioning

#### Alert
- Alert dismiss function created

#### Registration
- User register

- Random creation of test data for username, email, password, phone

- Login testing after register

- Variable storing for reusing the data

#### External links
- Asserts all links present in the nav bars

#### Page content when unlogged
- Logout if needed

- Nav Bar links asserted by the External Links class

- Who am I content asserted

- About me content asserted

- Timeline title and items asserted

- Referrals title and items asserted

#### Modals filling
- Filling and submiting the contact form

- Filling and submiting the referral form

#### Page content when logged
- Register user

- Dismiss alerts

- Assert specific items in nav bar that only appear when logged

- Post in timeline by filling and submiting the post form

- Asserting the newly created post

- Edit post. Searches for one edit button, opens a modal and updates the post

- Fetching unread messages

- Marking message as read

#### Small size tests
- Simulates a smaller screen

- Checks the presence of the nav bars

#### Unit Tests
- Checks the presence of index and layout html


