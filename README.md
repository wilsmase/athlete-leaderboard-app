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


---

## 📦 How to Run It Locally

1. Clone this repo:
    ```bash
    git clone https://github.com/YOUR_USERNAME/speed-leaderboard.git
    cd speed-leaderboard
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. Install Flask:
    ```bash
    pip install flask
    ```

4. Run the app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://localhost:5000`

---

## 📥 Sample CSV Upload Format

```csv
name,drill,score
Wilson,40-yd,4.55
Jordan,beep-test,13.2
Kai,vert,31
