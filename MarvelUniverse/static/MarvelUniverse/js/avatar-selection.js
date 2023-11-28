document.addEventListener('DOMContentLoaded', function () {
    const avatarModal = document.getElementById('avatar-modal');
    const closeBtn = document.getElementById('close-avatar-modal');
    const selectedAvatarContainer = document.getElementById('selected-avatar-container');
    const secondAvatarContainer = document.getElementById('second-avatar-container');



    const updateProfileImage = function (avatarUrl) {
        const csrfTokenElement = document.getElementsByName('csrfmiddlewaretoken')[0];
        const csrfToken = csrfTokenElement ? csrfTokenElement.value : null;

        // Update the second avatar container before making the fetch request
        updateSecondAvatar(avatarUrl);

        fetch('/marvel-universe/update_profile_image/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ avatarUrl: avatarUrl }),
        })
        .then(response => response.json())
        .then(data => {
            avatarModal.style.display = 'none';
            window.location.reload();
        });
    };

    const updateSecondAvatar = function (avatarUrl) {
        // Update second avatar container based on the selected avatar

    };

    document.getElementById('select-avatar-btn').addEventListener('click', function () {
        avatarModal.style.display = 'flex';
    });

    closeBtn.addEventListener('click', function () {
        avatarModal.style.display = 'none';
    });

    document.querySelectorAll('.avatar-option').forEach(function (avatarOption) {
        avatarOption.addEventListener('click', function () {
            const avatarUrl = avatarOption.getAttribute('data-avatar');
            updateProfileImage(avatarUrl);
        });
    });

    document.getElementById('select-default-avatar').addEventListener('click', function () {
        selectedAvatarContainer.innerHTML = `
            <svg class="fallback-svg" xmlns="http://www.w3.org/2000/svg" height="150" viewBox="0 -960 960 960" width="150">
                <path d="M234-276q51-39 114-61.5T480-360q69 0 132 22.5T726-276q35-41 54.5-93T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 59 19.5 111t54.5 93Zm246-164q-59 0-99.5-40.5T340-580q0-59 40.5-99.5T480-720q59 0 99.5 40.5T620-580q0 59-40.5 99.5T480-440Zm0 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q53 0 100-15.5t86-44.5q-39-29-86-44.5T480-280q-53 0-100 15.5T294-220q39 29 86 44.5T480-160Zm0-360q26 0 43-17t17-43q0-26-17-43t-43-17q-26 0-43 17t-17 43q0 26 17 43t43 17Zm0-60Zm0 360Z"/>
            </svg>`;
        updateProfileImage('');
    });
});
