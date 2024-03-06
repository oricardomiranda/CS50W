# Capstone

Final Project of [CS50 Web Programming with Python and JavaScript](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/)
[Full project specification](https://cs50.harvard.edu/web/2020/projects/final/capstone/)

The main idea implemented in this project was to create a personal portfolio that would allow recruiters, colleagues and other coders to be able to reach me and check my work

## Setup
First, clone this repository:

```bash
git clone https://github.com/oricardomiranda/CS50W/tree/34dedce4af8e1cba0112960b6c1939c4cf67d32a/Final%20Project/

cd Capstone/project5
```

Install dependencies:
```bash
pip3 install -r requirements.txt
```

To run the development server:
```bash
python manage.py runserver
```

## Requirements
This website was built using [Django](https://github.com/django/django)
The backend of this website is coded in Python
The frontend of this website is codd in Javascript
The application must be mobile-responsive


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

![Messages](https://github.com/oricardomiranda/CS50W/blob/main/Final%20Project/Capstone/project5/extras/Captura%20de%20ecrã%202024-03-05,%20às%2017.10.41.png?raw=true)

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


