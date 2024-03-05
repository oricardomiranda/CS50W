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
