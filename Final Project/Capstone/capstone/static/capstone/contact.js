// Main Container
const secondaryContainer = document.createElement('div');
secondaryContainer.classList.add('secondary-container');

// Define contactListContainer
const contactListContainer = document.createElement('div');
contactListContainer.id = 'messageContent'; // Set an ID for easier retrieval
contactListContainer.classList.add('all_post_view');

let contactLoaded = false; // Flag to track if contact is loaded

let unreadMessages = 0;

// Function to get CSRF token from cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function loadContact() {
    console.log('Attempting to fetch contact data...');
    if (!contactLoaded) {
        fetch('/contact_fetch/', {
                method: 'POST', // Specify the request method
                headers: {
                    'Content-Type': 'application/json', // Specify the content type
                    'X-CSRFToken': getCookie('csrftoken') // Include CSRF token in the headers
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Received contact data:', data);
                const sortedContactItems = data.contact_items;

                const messagesTitle = document.createElement('div');
                messagesTitle.textContent = 'Messages';
                messagesTitle.classList.add('animated-text');
                messagesTitle.id = 'myMessages'
                messagesTitle.innerHTML = '<p>My Messages</p>';
                contactListContainer.appendChild(messagesTitle);

                // Manipulate the DOM to display contact data
                sortedContactItems.forEach(item => {
                    const contactItem = document.createElement('div');
                    contactItem.classList.add('all_post_view');

                    // Create a button to mark the contact as read
                    const readButton = document.createElement('button');
                    readButton.classList.add('btn');
                    readButton.classList.add('btn-primary');
                    readButton.classList.add('mark-read-button');
                    readButton.textContent = 'Mark as Read';
                    readButton.addEventListener('click', function() {
                        // Make a POST request to mark the contact as read
                        fetch(`/contact_read/${item.id}/`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': getCookie('csrftoken')
                            }
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Failed to mark contact as read');
                            }
                            // Remove the 'unread' class and disable the button
                            contactItem.classList.remove('unread');
                            readButton.disabled = true;
                            console.log('Contact marked as read successfully');
                            // location.reload();
                        })
                        .catch(error => {
                            console.error('Error marking contact as read:', error);
                        });
                    });


                    // Add a separator element
                    const separator = document.createElement('div');
                    separator.classList.add('separator');
                    const spacing = document.createElement('hr');


                    if (item.read) {
                        console.log("Read item");
                        contactItem.classList.add('read');
                        contactItem.id = 'readMessage'
                        contactItem.innerHTML = `
                        <div class="animated-text">
                        <p></p>
                        <p>Email: ${item.email}</p>
                        <p>Contact: ${item.phone}</p>
                        <p>Message: ${item.message}</p>
                        </div>
                        `;
                    } else {
                        unreadMessages++;
                        console.log("Unread item");
                        contactItem.classList.add('unread');
                        contactItem.id = 'unreadMessage'
                        contactItem.innerHTML = `
                        <div class="animated-text-light">
                        <p></p>
                        <p>Email: ${item.email}</p>
                        <p>Contact: ${item.phone}</p>
                        <p>Message: ${item.message}</p>
                        </div>
                        `;
                        contactItem.appendChild(readButton);

                    }
                    contactItem.appendChild(separator);
                    contactItem.appendChild(spacing);
                    contactListContainer.appendChild(contactItem);
                });
                //Retrieve unread count
                console.log("Unread messages count: " + unreadMessages);
                if (unreadMessages > 1) {
                    alert(`You have ${unreadMessages} unread messages.`);
                }
                else if (unreadMessages > 0) {
                    alert(`You have ${unreadMessages} unread message.`);
                }

                // Check if additional spacing is needed
                if (!isNearBottom(contactListContainer)) {
                    const additionalSpacing = document.createElement('div');
                    additionalSpacing.classList.add('additional-spacing');
                    contactListContainer.appendChild(additionalSpacing);
                }

                console.log('Contact data loaded successfully.');
                contactLoaded = true;
            })
            .catch(error => {
                console.error('Error fetching contact data:', error);
            });
    }
}

// Function to check if an element is near the bottom of the viewport
function isNearBottom(element) {
    const rect = element.getBoundingClientRect();
    return rect.bottom <= window.innerHeight;
}



// Call the loadContact function when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    loadContact();
    const contactContent = document.getElementById('messageContent');
    // Append contactListContainer to contactContent
    contactContent.appendChild(contactListContainer);

    // Append contactContent to secondaryContainer
    secondaryContainer.appendChild(contactContent);

    // Append secondaryContainer to the document body or any other desired element
    document.body.appendChild(secondaryContainer);
});
