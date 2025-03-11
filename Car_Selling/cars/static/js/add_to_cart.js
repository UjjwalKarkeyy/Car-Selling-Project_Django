document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();  // Prevents page reload

        let carId = this.getAttribute('data-car-id');

        fetch(`/cart/add/${carId}/`, { 
            method: "GET",
            headers: { "X-Requested-With": "XMLHttpRequest" }
        })
        .then(response => response.json())
        .then(data => {
            showPopupMessage(data.message, data.status);
        })
        .catch(error => console.error('Error:', error));
    });
});

// Function to Show a Temporary Popup Message with Animation
function showPopupMessage(message, status) {
    let popupContainer = document.getElementById("popup-container");

    // Create a popup div
    let popup = document.createElement("div");
    popup.className = `popup-message ${status}`;
    popup.innerHTML = `<strong>${message}</strong>`;

    // Append to popup container
    popupContainer.appendChild(popup);

    // Animate fade-in
    setTimeout(() => {
        popup.style.opacity = "1";
    }, 100);

    // Remove the popup smoothly after 3 seconds
    setTimeout(() => {
        popup.style.opacity = "0";
        setTimeout(() => {
            popup.remove();
        }, 500);  // Extra time for smooth fade-out
    }, 3000);
}
