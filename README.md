# 🏃‍♂️ Speed Leaderboard App

A full-stack Flask web app designed for coaches and athletes to log, track, and visualize performance data from speed and conditioning drills in real time.

---

## 🚀 Features

- 🔹 Submit athlete drill results via web form
- 🔹 Separate live-updating leaderboards for each drill type
- 🔹 Store and retrieve data using SQLite
- 🔹 Upload CSV files to bulk-import athlete data
- 🔹 Auto-refresh leaderboard using JavaScript (no page reload)
- 🔹 Clean, responsive UI with polished CSS styling
- 🔹 Scrollable, ranked leaderboard tables with drill-based sorting

---

## 🛠️ Built With

- **Flask** – lightweight backend framework
- **SQLite** – local relational database for storing entries
- **HTML + CSS** – structure and styling
- **JavaScript (Fetch API)** – live leaderboard updates
- **Python CSV Module** – parsing uploaded files

---

## 📊 Supported Drills

- 40-yard dash  
- 10-yard fly  
- 20-yard fly  
- Beep test  
- Vertical jump

---

## 🧠 What I Learned

- Routing, templating, and form handling with Flask  
- Structuring databases and writing SQL queries  
- Connecting frontend and backend using JavaScript and JSON  
- Working with files and parsing CSVs  
- Organizing full-stack projects with clean folder structure  
- Thinking like a backend developer (data flow, validation, performance)

---

## 📂 Project Structure

speed-leaderboard/
│
├── app.py # Main Flask app
├── database.py # SQLite helper functions
├── leaderboard.db # Auto-created database
│
├── templates/
│ └── index.html # UI with form + leaderboard
│
├── static/
│ ├── style.css # CSS styles
│ └── script.js # JavaScript for live updates
