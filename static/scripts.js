function fetchLeaderboard() {
  fetch('/api/leaderboard')
    .then(response => response.json())
    .then(data => {
      // For each drill category in the JSON data
      for (const drill in data) {
        const leaderboardDiv = document.getElementById(`leaderboard-${drill}`);
        if (!leaderboardDiv) continue; // Skip if no div for this drill

        const tbody = leaderboardDiv.querySelector('tbody');
        tbody.innerHTML = ''; // Clear old rows

        data[drill].forEach((entry, index) => {
          const tr = document.createElement('tr');

          // Create and append rank cell
          const rankTd = document.createElement('td');
          rankTd.textContent = index + 1;
          tr.appendChild(rankTd);

          // Create and append name cell
          const nameTd = document.createElement('td');
          nameTd.textContent = entry.name;
          tr.appendChild(nameTd);

          // Create and append score cell
          const scoreTd = document.createElement('td');
          scoreTd.textContent = entry.score;
          tr.appendChild(scoreTd);

          tbody.appendChild(tr);
        });
      }
    })
    .catch(error => {
      console.error('Error fetching leaderboard:', error);
    });
}

setInterval(fetchLeaderboard, 5000); // Runs fetchLeaderboard every 5000 ms = 5 seconds
