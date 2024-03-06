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

function likeHandler(id, user_liked) {
    const like = document.getElementById(`${id}`);
    console.log("Current like count:", like.innerText);
    like.classList.remove('fa-thumbs-up');
    like.classList.remove('fa-thumbs-down');

    // Get the current liked status from the data attribute
    let liked = like.dataset.liked === "true";

    // Disable the button during the fetch request
    like.disabled = true;

    if (liked) {
        fetch(`/remove_like/${id}`)
            .then(response => response.json())
            .then(result => {
                like.classList.add('fa-thumbs-up');
                liked = !liked;
            })
            .catch(error => console.error('Error:', error))
            .finally(() => {
                // Enable the button after the fetch request is completed
                like.disabled = false;
                // Update the data attribute with the new liked status
                like.dataset.liked = liked.toString();

                fetchLikeCount(id);

            });
    } else {
        fetch(`/add_like/${id}`)
            .then(response => response.json())
            .then(result => {
                like.classList.add('fa-thumbs-down');
                liked = !liked;
            })
            .catch(error => console.error('Error:', error))
            .finally(() => {
                // Enable the button after the fetch request is completed
                like.disabled = false;
                // Update the data attribute with the new liked status
                like.dataset.liked = liked.toString();

                fetchLikeCount(id);
            });
    }
}

function fetchLikeCount(id) {
    console.log("Fetching like count for post ID:", id);
    fetch(`/count_like/${id}`)
        .then(response => response.json())
        .then(result => {
            console.log("Received like count:", result.likes_count);
            // Update the like count in your UI
            const likesCountElement = document.getElementById(`count_like_${id}`);
            likesCountElement.innerText = `${result.likes_count} like${result.likes_count !== 1 ? 's' : ''}`;
        })
        .catch(error => console.error('Error fetching like count:', error));
}



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

            // Make an AJAX request to send form data to the server
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/contact/', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
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
