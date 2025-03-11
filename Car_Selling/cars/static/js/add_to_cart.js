document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent default button action

        let carId = this.getAttribute('data-car-id');  // Get car ID

        fetch(`/add-to-cart/${carId}/`, {  // AJAX request to Django view
            method: "GET",
            headers: { "X-Requested-With": "XMLHttpRequest" }
        })
        .then(response => response.json())
        .then(data => {
            // Show success message
            let messageBox = document.getElementById("cart-message");
            messageBox.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
        })
        .catch(error => console.error('Error:', error));
    });
});
