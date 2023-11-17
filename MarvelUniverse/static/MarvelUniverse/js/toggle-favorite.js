document.addEventListener('DOMContentLoaded', function() {
    const favoriteButton = document.getElementById('favoriteButton');

    if (favoriteButton) {
        favoriteButton.addEventListener('click', function() {
            const model = favoriteButton.getAttribute('data-model');
            const objectId = favoriteButton.getAttribute('data-object-id');

            const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
            const csrftoken = csrfTokenElement ? csrfTokenElement.value : null;

            fetch(`/marvel-universe/${model}s/${objectId}/toggle_favorite/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken, //
                },
                body: JSON.stringify({}),
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    if ('is_favorite' in data) {
                        favoriteButton.classList.toggle('is-favorite', data.is_favorite);
                    }
                })
        });
    }
});