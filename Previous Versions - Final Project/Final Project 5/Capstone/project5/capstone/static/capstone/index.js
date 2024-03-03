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



mainContainer.appendChild(whoAmI);
mainContainer.appendChild(aboutMe);
mainContent.appendChild(mainContainer);

containerFluid.appendChild(mainContent);

// Timeline
const timelineContent = document.createElement('div');
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
        if (!timelineLoaded) {
            fetch('/timeline_fetch/')
            .then(response => response.json())
            .then(data => {
                const sortedTimelineItems = data.timeline_items.sort((a, b) => b.year - a.year);

                sortedTimelineItems.forEach(item => {
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

                const timelineTitle = document.createElement('div');
                timelineTitle.textContent = 'Timeline';
                timelineTitle.classList.add('animated-text');
                timelineTitle.innerHTML = '<p>My Timeline: My journey into IT</p>';
                timelineContent.appendChild(timelineTitle);

                timelineContent.appendChild(timelineList);
                timelineContent.classList.remove('invisible');
                timelineContent.classList.add('animate');

                timelineLoaded = true;
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
referralsContent.classList.add('second-container', 'invisible', 'fade-in');

const referralsTitle = document.createElement('div');
referralsTitle.textContent = 'Referrals';

const referralsList = document.createElement('div');
referralsList.classList.add('all_post_view');

let referralsLoaded = false; // Flag to track if referrals are loaded

function loadReferrals() {
    if (!referralsLoaded) {
        fetch('/referral_fetch/')
            .then(response => response.json())
            .then(data => {
                const sortedReferrals = data.referral_items.sort((a, b) => a.name.localeCompare(b.name));

                sortedReferrals.forEach(referral => {
                    const referralItem = document.createElement('div');
                    referralItem.classList.add('all_post_view');
                    referralItem.innerHTML = `
                        <h7>${referral.name}</h7>
                        <div class="animated-text">
                            <p>${referral.subject}</p>
                            <p>${referral.message}</p>
                        </div>
                    `;
                    referralsList.appendChild(referralItem);
                });

                const referralsTitle = document.createElement('div');
                referralsTitle.textContent = 'Timeline';
                referralsTitle.classList.add('animated-text');
                referralsTitle.innerHTML = '<p>My Referrals</p>';
                referralsContent.appendChild(referralsTitle);

                referralsContent.appendChild(referralsList);
                referralsContent.classList.remove('invisible');
                referralsContent.classList.add('animate');

                referralsLoaded = true;
            })
            .catch(error => {
                console.error('Error fetching referrals data:', error);
            });
    }
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
