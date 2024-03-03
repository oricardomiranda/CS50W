function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);

    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}


function submitChanges(id) {
    const text = document.getElementById(`textarea_${id}`).value;
    const message = document.getElementById(`message_${id}`);
    const modal = document.getElementById(`modal_edit_post_${id}`)

    fetch(`/edit/${id}`, {
            method: "POST",
            headers: {
                "Content-type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                message: text
            })
        })
        .then(response => response.json())
        .then(result => {
            message.innerHTML = result.data;

            // Hide the modal and perform other actions
            modal.classList.remove('show');
            modal.setAttribute('aria-hidden', 'true');
            modal.setAttribute('style', 'display: none');

            // get modal backdrops
            const modalsBackdrops = document.getElementsByClassName('modal-backdrop');

            // remove every modal backdrop
            for (let i = 0; i < modalsBackdrops.length; i++) {
                document.body.removeChild(modalsBackdrops[i]);
            }

            location.reload();
        })
        .catch(error => {
            // Handle errors appropriately, e.g., display an error message
            console.error('Error:', error);
        });
}

//Contact Modal
document.addEventListener('DOMContentLoaded', function () {
    // Function to create and display the modal
    function displayContactModal() {
        // Create modal container
        var modalContainer = document.createElement('div');
        modalContainer.className = 'modal fade';
        modalContainer.id = 'contactModal';
        modalContainer.tabIndex = '-1';
        modalContainer.setAttribute('aria-labelledby', 'contactModalLabel');
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
        modalTitle.id = 'contactModalLabel';
        modalTitle.textContent = 'Contact Me';
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
        form.id = 'contactForm';
        var emailInput = document.createElement('input');
        emailInput.type = 'email';
        emailInput.className = 'form-control';
        emailInput.id = 'emailInput';
        emailInput.placeholder = 'Email address';
        emailInput.required = true;
        var phoneInput = document.createElement('input');
        phoneInput.type = 'text';
        phoneInput.className = 'form-control';
        phoneInput.id = 'phoneInput';
        phoneInput.placeholder = 'Phone number (optional)';
        var messageInput = document.createElement('textarea');
        messageInput.className = 'form-control';
        messageInput.id = 'messageInput';
        messageInput.placeholder = 'Message';
        messageInput.rows = '5';
        messageInput.required = true;
        var submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.className = 'btn btn-primary';
        submitButton.textContent = 'Submit';
        form.appendChild(emailInput);
        form.appendChild(phoneInput);
        form.appendChild(messageInput);
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
        var modal = new bootstrap.Modal(document.getElementById('contactModal'));
        modal.show();

        // Add event listener for form submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            // Get values from form fields
            var email = document.getElementById('emailInput').value;
            var phone = document.getElementById('phoneInput').value;
            var message = document.getElementById('messageInput').value;

            // Log input field values
            console.log('Email:', email);
            console.log('Phone:', phone);
            console.log('Message:', message);

            // Make an AJAX request to send form data to the server
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/contact/', true);
            xhr.setRequestHeader('Content-Type', 'application/json');

            var csrfToken = getCookie('csrftoken');
            if (csrfToken) {
                xhr.setRequestHeader('X-CSRFToken', csrfToken);
            } else {
                console.error('CSRF token is missing');
            }

            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    // Optionally handle success response from the server
                    console.log('Contact data saved successfully');
                    // Close the modal
                    var modal = bootstrap.Modal.getInstance(document.getElementById('contactModal'));
                    modal.hide();
                }
            };
            xhr.send(JSON.stringify({
                email: email,
                phone: phone,
                message: message
            }));
        });
    }

    // Event listener to trigger modal display
    document.getElementById('contactMe').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        displayContactModal(); // Call function to display modal
    });
});



//New timeline event modal
document.addEventListener('DOMContentLoaded', function () {
    // Function to create and display the modal
    function displayPostModal() {
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
        var subjectInput = document.createElement('input');
        subjectInput.type = 'text';
        subjectInput.className = 'form-control';
        subjectInput.id = 'subjectInput';
        subjectInput.placeholder = 'Subject';
        var contentInput = document.createElement('textarea');
        contentInput.className = 'form-control';
        contentInput.id = 'contentInput';
        contentInput.placeholder = 'Content';
        contentInput.rows = '5';
        contentInput.required = true;
        var submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.className = 'btn btn-primary';
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

            // Log input field values
            console.log('Year:', year);
            console.log('Subject:', subject);
            console.log('Content:', content);

            // Make an AJAX request to send form data to the server
            fetch('/timeline_post/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
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
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    // Event listener to trigger modal display
    document.getElementById('timelinePost').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        displayPostModal(); // Call function to display modal
    });
});


// Referral Modal
document.addEventListener('DOMContentLoaded', function () {
    // Function to create and display the modal
    function displayReferralModal() {
        // Create modal container
        var modalContainer = document.createElement('div');
        modalContainer.className = 'modal fade';
        modalContainer.id = 'referralModal';
        modalContainer.tabIndex = '-1';
        modalContainer.setAttribute('aria-labelledby', 'referralModalLabel');
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
        modalTitle.id = 'referralModalLabel';
        modalTitle.textContent = 'Refer Me';
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
        form.id = 'referralForm';
        var nameInput = document.createElement('input');
        nameInput.type = 'text';
        nameInput.className = 'form-control';
        nameInput.id = 'nameInput';
        nameInput.placeholder = 'Your Name (optional)';
        var subjectInput = document.createElement('input');
        subjectInput.type = 'text';
        subjectInput.className = 'form-control';
        subjectInput.id = 'subjectInput';
        subjectInput.placeholder = 'Subject';
        subjectInput.required = true;
        var messageInput = document.createElement('textarea');
        messageInput.className = 'form-control';
        messageInput.id = 'messageInput';
        messageInput.placeholder = 'Message';
        messageInput.rows = '5';
        messageInput.required = true;
        var submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.className = 'btn btn-primary';
        submitButton.textContent = 'Submit';
        form.appendChild(nameInput);
        form.appendChild(subjectInput);
        form.appendChild(messageInput);
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
        var modal = new bootstrap.Modal(document.getElementById('referralModal'));
        modal.show();

        // Add event listener for form submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            // Get values from form fields
            var name = document.getElementById('nameInput').value || 'Anonymous';
            var subject = document.getElementById('subjectInput').value;
            var message = document.getElementById('messageInput').value;

            // Log input field values
            console.log('Name:', name);
            console.log('Subject:', subject);
            console.log('Message:', message);

            // Make an AJAX request to send form data to the server
            fetch('/referral/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    name: name,
                    subject: subject,
                    message: message
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log('Referral data saved successfully');
                // Close the modal
                modal.hide();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    // Event listener to trigger modal display
    document.getElementById('referral').addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        displayReferralModal(); // Call function to display modal
    });
});
