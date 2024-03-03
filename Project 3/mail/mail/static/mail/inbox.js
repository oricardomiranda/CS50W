document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#details-view').style.display = 'none';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    // Submit email form
    document.querySelector('#compose-form').addEventListener('submit', send_email);
}

function open_email(id, mailbox) {
    console.log(id);

    let archiveButton;

    fetch(`/emails/${id}`)
        .then(response => response.json())
        .then(email => {
            // Select detail view
            document.querySelector('#emails-view').style.display = 'none';
            document.querySelector('#compose-view').style.display = 'none';
            document.querySelector('#details-view').style.display = 'block';

            // Create email info section
            const infoDiv = document.createElement('div');
            infoDiv.className = 'email-info';
            infoDiv.innerHTML = `
              <p><strong>From:</strong> ${email.sender}</p>
              <p><strong>To:</strong> ${email.recipients}</p>
              <p><strong>Subject:</strong> ${email.subject}</p>
              <p><strong>Timestamp:</strong> ${email.timestamp}</p>
              `;

            // Create button for replying
            const replyButton = Object.assign(document.createElement('button'), {
                innerText: 'Reply',
                className: 'btn btn-sm btn-outline-primary'
            });

            // Create button for archiving/unarchiving
            if (mailbox !== 'sent') {
                // Create button for archiving/unarchiving
                archiveButton = document.createElement('button');
                archiveButton.innerHTML = email.archived ? 'Unarchive' : 'Archive';
                archiveButton.className = email.archived ? 'btn btn-sm btn-outline-primary' : 'btn btn-sm btn-outline-danger';
                archiveButton.style.marginLeft = '4px';

                // Append buttons to the email info section
                infoDiv.appendChild(replyButton);
                infoDiv.appendChild(archiveButton);
            } else {
                // Append only the reply button
                infoDiv.appendChild(replyButton);
            }

            // Append email info section and body to the details view
            document.querySelector('#details-view').innerHTML = '';
            document.querySelector('#details-view').appendChild(infoDiv);

            const bodyDiv = document.createElement('div');
            bodyDiv.className = 'email-body';
            bodyDiv.innerHTML = `<hr><p>${email.body}</p>`;
            document.querySelector('#details-view').appendChild(bodyDiv);

            // Read status to true
            if (!email.read) {
                fetch(`/emails/${email.id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        read: true
                    })
                });
            }

            // Archive email
            if (archiveButton) {
                archiveButton.addEventListener('click', function() {
                    fetch(`/emails/${email.id}`, {
                        method: 'PUT',
                        body: JSON.stringify({
                            archived: !email.archived
                        })
                    }).then(() => {
                        setTimeout(() => {
                            if (email.archived) {
                                load_mailbox('inbox');
                            } else {
                                load_mailbox('archive');
                            }
                        }, 500);
                    });
                });
            }

            // Reply email
            replyButton.addEventListener('click', function() {
                compose_email();
                document.querySelector('#compose-recipients').value = email.sender;
                let subject = email.subject;
                if (subject.split(' ', 1)[0] != "Re:") {
                    document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
                } else {
                    document.querySelector('#compose-subject').value = subject;
                }
                document.querySelector('#compose-body').value = `On ${email.timestamp}  ${email.sender} wrote: ${email.body}`;
            })
        })
        .catch(error => console.error('Error fetching email:', error));
}

function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#details-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Show loaded emails
    fetch(`/emails/${mailbox}`)
        .then(response => response.json())
        .then(emails => {
            // Print emails
            emails.forEach(email => {
                const emailDiv = document.createElement('div');
                emailDiv.className = 'email';
                emailDiv.style.backgroundColor = email.read ? '#dddddd' : 'white';
                emailDiv.innerHTML = `
                <div class="email-info border" style="display: flex; flex-direction: row; justify-content: space-between; padding: 10px;">
                <p>${email.sender}</p>
                <p><strong>${email.subject}</strong></p>
                <p>${email.timestamp}</p></div>`;
                emailDiv.addEventListener('click', () => open_email(email.id));
                document.querySelector('#emails-view').append(emailDiv);
            });
            console.log(emails);
        });
}

function send_email(event) {
    event.preventDefault();

    // Sending email
    fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: document.querySelector('#compose-recipients').value,
                subject: document.querySelector('#compose-subject').value,
                body: document.querySelector('#compose-body').value
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);
        });

    // Redirect to send
    setTimeout(() => {load_mailbox('sent')}, 500);

    document.querySelector('#compose-form').removeEventListener('submit', send_email);

}
