// Get the table
const table = document.getElementById('leagueTable');

// Convert the table rows to an array
let rows = Array.from(table.rows);

// Remove the header row
rows.shift();

// Sort the rows based on the points
rows.sort((a, b) => {
    const pointsA = parseInt(a.cells[5].textContent);
    const pointsB = parseInt(b.cells[5].textContent);
    return pointsB - pointsA;
});

// Append the sorted rows back into the table and update the position number
for (let i = 0; i < rows.length; i++) {
    // Update the position number
    rows[i].cells[0].textContent = i + 1;

    // Append the row to the table
    table.tBodies[0].appendChild(rows[i]);
}