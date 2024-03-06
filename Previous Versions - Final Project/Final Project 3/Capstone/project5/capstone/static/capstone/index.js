// Creating the container elements
const containerFluid = document.createElement('div');
containerFluid.classList.add('container-fluid');

const row = document.createElement('div');
row.classList.add('row');

// Another div for main content
const mainContent = document.createElement('div');
mainContent.classList.add('body');

const mainContainer = document.createElement('div');
mainContainer.classList.add('main-container');

// Who am I title div
const whoAmI = document.createElement('div');
whoAmI.classList.add('all_post_view');
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
aboutMe.innerHTML = '<h7>About Me</h7>' +
    '<div class="animated-text">' +
    '<p>QA Engineer in Fintech</p>' +
    '<p>Java backend tester in Linux servers</p>' +
    '<p>Interested in progressing into automation</p>' +
    '<p>Completing CS50W: Web Development</p>';

// Append elements to the DOM
mainContainer.appendChild(whoAmI);
mainContainer.appendChild(aboutMe);
mainContent.appendChild(mainContainer);
row.appendChild(mainContent);

// Timeline
const timelineContent = document.createElement('div');
timelineContent.classList.add('second-container', 'invisible', 'fade-in');

const timelineContainer = document.createElement('div');
timelineContainer.classList.add('timeline');

const timelineTitle = document.createElement('div');
timelineTitle.textContent = 'Timeline';

const timelineList = document.createElement('div');
timelineList.classList.add('all_post_view');

// Function to check if timelineContent is within the viewport.
function isElementInViewport(el, threshold = 0) {
    const rect = el.getBoundingClientRect();
    const windowHeight = (window.innerHeight || document.documentElement.clientHeight);
    return (
        (rect.top + rect.height * threshold >= 0) &&
        (rect.bottom - rect.height * threshold <= windowHeight)
    );
}

// Add event listener to the scroll event.
window.addEventListener('scroll', function () {
    if (isElementInViewport(timelineContent, 0.7)) {
        timelineContent.classList.remove('invisible');
        timelineContent.classList.add('animate');
    }
});

// Load the timeline data from the server
fetch('/timeline_data/')
    .then(response => response.json())
    .then(data => {
        // Generate HTML code for the timeline
        const timelineItems = data.timeline_items;

        timelineItems.forEach(item => {
            const timelineItem = document.createElement('div');
            timelineItem.classList.add('all_post_view');
            timelineItem.innerHTML = `
                <h7>${item.year}</h7>
                <div class="animated-text">
                    <p>${item.subject}</p>
                    <p>${item.event}</p>
                </div>
            `;
            timelineList.appendChild(timelineItem);
        });

        // Append timelineList to timelineContent
        timelineContent.appendChild(timelineList);
    })
    .catch(error => {
        console.error('Error fetching timeline data:', error);
    });

// Append timelineContent to row
row.appendChild(timelineContent);

// Append row to containerFluid
containerFluid.appendChild(row);

// Append containerFluid to document body
document.body.appendChild(containerFluid);
