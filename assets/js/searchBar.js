// Get the search input element
const searchInput = document.getElementById('searchInput');

// Get the item elements
const items = document.getElementsByClassName('nav-item');

// Add an event listener to the search input
searchInput.addEventListener('input', function() {
    // Get the search query
    const query = searchInput.value.toLowerCase();

    // Loop through the items
    for (let i = 0; i < items.length; i++) {
        // Get the name of the item
        const itemName = items[i].getAttribute('data-name').toLowerCase();

        // If the item name includes the query, show the item, otherwise hide it
        if (itemName.includes(query)) {
            items[i].style.display = '';
        } else {
            items[i].style.display = 'none';
        }
    }
});