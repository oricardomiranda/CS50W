// Creating the container elements
const containerFluid = document.createElement('div');
containerFluid.classList.add('container-fluid');

// Main Content
const mainContent = document.createElement('div');
mainContent.classList.add('body');

const mainContainer = document.createElement('div');
mainContainer.classList.add('main-container');

// Who am I title div
const whoAmI = document.createElement('div');
whoAmI.classList.add('all_post_view');
whoAmI.id = 'whoamiContent';
whoAmI.innerHTML = '<h7>Who am I</h7>' +
    '<div class="animated-text">' +
    '<p>Ricardo Miranda</p>' +
    '<p>I used to be a Nurse</p>' +
    '<p>Decided to change career</p>' +
    '<p>And I am always ready to learn more</p>' +
    '</div>';

// About me title div
const aboutMe = document.createElement('div');
aboutMe.classList.add('all_post_view');
aboutMe.id = 'aboutMeContent'
aboutMe.innerHTML = '<h7>About Me</h7>' +
    '<div class="animated-text">' +
    '<p>QA Engineer in Fintech</p>' +
    '<p>Java backend tester in Linux servers</p>' +
    '<p>Interested in progressing into automation</p>' +
    '<p>Completing CS50W: Web Development</p>';

mainContainer.appendChild(whoAmI);
mainContainer.appendChild(aboutMe);
mainContent.appendChild(mainContainer);
containerFluid.appendChild(mainContent);

// Timeline
const timelineContent = document.createElement('div');
timelineContent.id = 'timelineContent';
timelineContent.classList.add('second-container', 'invisible', 'fade-in');
const timelineList = document.createElement('div');
timelineList.classList.add('all_post_view');
let timelineLoaded = false; // Flag to track if timeline is loaded

function isElementInViewport(el, threshold = 0) {
    const rect = el.getBoundingClientRect();
    const windowHeight = (window.innerHeight || document.documentElement.clientHeight);
    return (
        (rect.top + rect.height * threshold >= 0) &&
        (rect.bottom - rect.height * threshold <= windowHeight)
    );
}

function loadTimeline() {
    console.log('Loading timeline...');
    if (!timelineLoaded) {
        fetch('/timeline_fetch/')
            .then(response => response.json())
            .then(data => {
                const idItemMap = {};
                console.log('Timeline data received:', data);

                // Create a mapping of id to item objects
                data.timeline_items.forEach(item => {
                    idItemMap[item.id] = item;
                });

                // Sort the items based on some criteria (e.g., year)
                const sortedTimelineItems = data.timeline_items.sort((a, b) => b.year - a.year);

                sortedTimelineItems.forEach(item => {
                    console.log('Processing timeline item:', item);
                    const timelineItem = document.createElement('div');
                    timelineItem.classList.add('all_post_view');
                    timelineItem.id = 'timelineItem'
                    timelineItem.innerHTML = `
                        <h7>${item.year}</h7>
                        <div class="animated-text-smaller">
                            <p>${item.subject}</p>
                            <p>${item.content}</p>
                        </div>
                    `;
                    console.log('Timeline item created:', timelineItem);

                    // Edit button
                    if (isUserAuthenticated) {
                        console.log('User is authenticated, adding edit button...');
                        const editButton = document.createElement('button');
                        editButton.classList.add('btn');
                        editButton.classList.add('btn-primary');
                        editButton.id = "timelineEditButton";
                        editButton.textContent = 'Edit';
                        editButton.addEventListener('click', () => {
                            displayPostModal(item.id, item.year, item.subject, item.content);
                        });
                        console.log('Edit button added:', editButton);

                        timelineItem.appendChild(editButton);
                    }

                    // Delete button
                    if (isUserAuthenticated) {
                        console.log('User is authenticated, adding delete button...');
                        const deleteButton = document.createElement('button');
                        deleteButton.textContent = 'Delete';
                        deleteButton.classList.add('btn');
                        deleteButton.classList.add('btn-primary');
                        deleteButton.addEventListener('click', () => {
                            console.log('Delete button clicked, sending DELETE request...');
                            fetch(`/timeline_delete/${item.id}/`, {
                                    method: 'DELETE',
                                    headers: {
                                        'Content-Type': 'application/json',
                                        'X-CSRFToken': getCookie('csrftoken')
                                    }
                                })
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Failed to delete the timeline post');
                                    }
                                    // Remove the post from the UI
                                    timelineItem.remove();
                                    console.log('Post deleted successfully');
                                    loadTimeline()
                                })
                                .catch(error => {
                                    console.error('Error deleting timeline post:', error);
                                });
                        });
                        console.log('Delete button added:', deleteButton);

                        timelineItem.appendChild(deleteButton);
                    }

                    timelineList.appendChild(timelineItem);
                });

                console.log('Timeline items added to the list.');
                const timelineSmallTitle = document.createElement('div');
                timelineSmallTitle.innerHTML = '<h7>Timeline</h7>';
                timelineSmallTitle.id = 'timelineSmallTitle'

                const timelineTitle = document.createElement('div');
                timelineTitle.textContent = 'Timeline';
                timelineTitle.id = 'timelineTitle';
                timelineTitle.classList.add('animated-text');
                timelineTitle.innerHTML = '<p>My journey into IT</p>';

                timelineContent.appendChild(timelineSmallTitle);
                timelineContent.appendChild(timelineTitle);
                timelineContent.appendChild(timelineList);
                timelineContent.classList.remove('invisible');
                timelineContent.classList.add('animate');

                timelineLoaded = true;
                console.log('Timeline loaded successfully.');
            })
            .catch(error => {
                console.error('Error fetching timeline data:', error);
            });
    }
}

window.addEventListener('DOMContentLoaded', () => {
    if (isElementInViewport(timelineContent, 0.7)) {
        loadTimeline();
    }
});

window.addEventListener('scroll', () => {
    if (!timelineLoaded && isElementInViewport(timelineContent, 0.7)) {
        loadTimeline();
    }
});

containerFluid.appendChild(timelineContent);

// Referrals
const referralsContent = document.createElement('div');
referralsContent.id = 'referralsContent';
referralsContent.classList.add('second-container', 'invisible', 'fade-in');
const referralsList = document.createElement('div');
referralsList.classList.add('all_post_view');
let referralsLoaded = false; // Flag to track if referrals are loaded

function loadReferrals() {
    if (!referralsLoaded) {
        fetch('/referral_fetch/')
            .then(response => response.json())
            .then(data => {
                //const sortedReferrals = data.referral_items.sort((a, b) => a.name.localeCompare(b.name)); //RAMDOM SORT THIS
                const referralItems = data.referral_items;

                for (let i = referralItems.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [referralItems[i], referralItems[j]] = [referralItems[j], referralItems[i]];
                }

                referralItems.forEach(referral => {
                    const referralItem = document.createElement('div');
                    referralItem.classList.add('all_post_view');
                    referralItem.id = 'referralsItem'
                    referralItem.innerHTML = `
                        <h7>${referral.name}</h7>
                        <div class="animated-text-smaller">
                            <p>${referral.subject}</p>
                            <p>${referral.message}</p>
                        </div>
                    `;


                    // Delete button
                    if (isUserAuthenticated) {
                        const deleteButton = document.createElement('button');
                        deleteButton.textContent = 'Delete';
                        deleteButton.classList.add('btn');
                        deleteButton.classList.add('btn-primary');
                        deleteButton.addEventListener('click', () => {
                            fetch(`/referral_delete/${referral.id}/`, {
                                    method: 'DELETE',
                                    headers: {
                                        'Content-Type': 'application/json',
                                        'X-CSRFToken': getCookie('csrftoken')
                                    }
                                })
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Failed to delete the referral post');
                                    }
                                    // Remove the post from the UI
                                    referralItem.remove();
                                    console.log('Referral post deleted successfully');
                                })
                                .catch(error => {
                                    console.error('Error deleting referral post:', error);
                                });
                        });

                        referralItem.appendChild(deleteButton);
                    }

                    referralsList.appendChild(referralItem);
                });

                const referralsTitle = document.createElement('div');
                referralsTitle.id = 'referralsTitle';
                referralsTitle.textContent = 'Timeline';
                referralsTitle.classList.add('animated-text');
                referralsTitle.innerHTML = '<p>My Referrals</p>';
                referralsContent.appendChild(referralsTitle);

                referralsContent.appendChild(referralsList);
                referralsContent.classList.remove('invisible');
                referralsContent.classList.add('animate');

                referralsLoaded = true;

                // Check if additional spacing is needed
                if (!isNearBottom(referralsContent)) {
                    const additionalSpacing = document.createElement('div');
                    additionalSpacing.classList.add('additional-spacing');
                    referralsContent.appendChild(additionalSpacing);
                }

            })
            .catch(error => {
                console.error('Error fetching referrals data:', error);
            });
    }
}

// Function to check if an element is near the bottom of the viewport
function isNearBottom(element) {
    const rect = element.getBoundingClientRect();
    return rect.bottom <= window.innerHeight;
}


window.addEventListener('DOMContentLoaded', () => {
    if (isElementInViewport(referralsContent, 0.7)) {
        loadReferrals();
    }
});

window.addEventListener('scroll', () => {
    if (!referralsLoaded && isElementInViewport(referralsContent, 0.7)) {
        loadReferrals();
    }
});

containerFluid.appendChild(referralsContent);

document.body.appendChild(containerFluid);


// Edit timeline event modal
function displayPostModal(itemId, year, subject, content) {
    // Create modal container
    var modalContainer = document.createElement('div');
    modalContainer.className = 'modal fade';
    modalContainer.id = 'postModal';
    modalContainer.tabIndex = '-1';
    modalContainer.setAttribute('aria-labelledby', 'postModalLabel');
    modalContainer.setAttribute('aria-hidden', 'true');

    // Create modal dialog
    var modalDialog = document.createElement('div');
    modalDialog.className = 'modal-dialog modal-lg';

    // Create modal content
    var modalContent = document.createElement('div');
    modalContent.className = 'modal-content';

    // Create modal header
    var modalHeader = document.createElement('div');
    modalHeader.className = 'modal-header';
    var modalTitle = document.createElement('h5');
    modalTitle.className = 'modal-title';
    modalTitle.id = 'postModalLabel';
    modalTitle.textContent = 'Post Timeline Event';
    var closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.className = 'btn-close';
    closeButton.setAttribute('data-bs-dismiss', 'modal');
    closeButton.setAttribute('aria-label', 'Close');
    modalHeader.appendChild(modalTitle);
    modalHeader.appendChild(closeButton);

    // Create modal body
    var modalBody = document.createElement('div');
    modalBody.className = 'modal-body';
    var form = document.createElement('form');
    form.id = 'postForm';
    var yearInput = document.createElement('input');
    yearInput.type = 'text';
    yearInput.className = 'form-control';
    yearInput.id = 'yearInput';
    yearInput.placeholder = 'Year';
    yearInput.required = true;
    yearInput.value = year;
    var subjectInput = document.createElement('input');
    subjectInput.type = 'text';
    subjectInput.className = 'form-control';
    subjectInput.id = 'subjectInput';
    subjectInput.placeholder = 'Subject';
    subjectInput.value = subject;
    var contentInput = document.createElement('textarea');
    contentInput.className = 'form-control';
    contentInput.id = 'contentInput';
    contentInput.placeholder = 'Content';
    contentInput.rows = '5';
    contentInput.required = true;
    contentInput.value = content;
    var submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.className = 'btn btn-primary';
    submitButton.id = 'submitButton';
    submitButton.textContent = 'Submit';
    form.appendChild(yearInput);
    form.appendChild(subjectInput);
    form.appendChild(contentInput);
    form.appendChild(submitButton);
    modalBody.appendChild(form);

    // Append modal elements to each other
    modalContent.appendChild(modalHeader);
    modalContent.appendChild(modalBody);
    modalDialog.appendChild(modalContent);
    modalContainer.appendChild(modalDialog);

    // Append modal container to the body
    document.body.appendChild(modalContainer);

    // Show the modal
    var modal = new bootstrap.Modal(document.getElementById('postModal'));
    modal.show();

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        // Get values from form fields
        var year = document.getElementById('yearInput').value;
        var subject = document.getElementById('subjectInput').value;
        var content = document.getElementById('contentInput').value;

        // Make an AJAX request to send form data to the server
        fetch(`/timeline_edit/${itemId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    itemId: itemId, // Pass itemId to the server
                    year: year,
                    subject: subject,
                    content: content
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log('Timeline data saved successfully');
                // Close the modal
                modal.hide();
                // Clear values after input
                yearInput.value = '';
                subjectInput.value = '';
                contentInput.value = '';
                location.reload();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
}


// Event listener to trigger modal display
document.addEventListener('click', function(event) {
    // Check if the clicked element is the timelineEdit button
    if (event.target && event.target.classList.contains('timelineEdit')) {
        event.preventDefault(); // Prevent default link behavior
        // Extract the data attributes from the button
        const itemId = event.target.dataset.itemId;
        const year = event.target.dataset.year;
        const subject = event.target.dataset.subject;
        const content = event.target.dataset.content;
        displayPostModal(itemId, year, subject, content); // Call the displayPostModal function with extracted data
    }
});

