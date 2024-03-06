// Main Container
const mainContainer = document.createElement('div');
mainContainer.classList.add('main-container');

// Contact List Container
const contactListContainer = document.createElement('div');
contactListContainer.id = 'contact-list'; // Set an ID for easier retrieval
contactListContainer.classList.add('all_post_view');

let contactLoaded = false; // Flag to track if contact is loaded

function loadContact() {
    console.log('Attempting to fetch contact data...');
    if (!contactLoaded) {
        fetch('/contact_fetch/', {
            method: 'POST',  // Specify the request method
            headers: {
                'Content-Type': 'application/json'  // Specify the content type
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

            // Manipulate the DOM to display contact data
            const contactListContainer = document.getElementById('contact-list');

            sortedContactItems.forEach(item => {
                const contactItem = document.createElement('div');
                contactItem.classList.add('all_post_view');
                contactItem.innerHTML = `
                    <h7>${item.email}</h7>
                    <div class="animated-text">
                        <p>${item.phone}</p>
                        <p>${item.message}</p>
                    </div>
                `;
                contactListContainer.appendChild(contactItem);
            });

            console.log('Contact data loaded successfully.');
            contactLoaded = true;
        })
        .catch(error => {
            console.error('Error fetching contact data:', error);
        });
    }
}


// Call the loadContact function when the DOM content is loaded
document.addEventListener('DOMContentLoaded', loadContact);

// Append contactListContainer to contactContent
contactContent.appendChild(contactListContainer);

// Append contactContent to mainContainer
mainContainer.appendChild(contactContent);

// Append mainContainer to the document body or any other desired element
document.body.appendChild(mainContainer);
