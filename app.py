from flask import Flask, render_template, request, redirect, jsonify, flash
from database import create_table, insert_entry, get_entries_grouped_by_drill, reset_leaderboard
import csv

app = Flask(__name__)
create_table()

@app.route('/')
def home():
    leaderboard_by_drill = get_entries_grouped_by_drill()
    return render_template('index.html', leaderboards=leaderboard_by_drill)

@app.route('/submit', methods=['POST'])
def log_drill_result(): #This function will now receive the order from the form, extract it, send it to the kitchen (DB), and return the customer to the homepage where they’ll soon see their data on the leaderboard.
    name = request.form['a-name']
    drill = request.form['drill']
    score = request.form['a-data']

    insert_entry(name, drill, score)

    return redirect('/')

@app.route('/reset')
def reset():
    reset_leaderboard()
    return redirect('/')

@app.route('/api/leaderboard')
def api_leaderboard():
    grouped = get_entries_grouped_by_drill()

    leaderboard_data = {}
    for drill, entries in grouped.items():
        leaderboard_data[drill] = []
        for row in entries:
            leaderboard_data[drill].append({
                "id": row[0],
                "name": row[1],
                "score": row[3]
            })

    return jsonify(leaderboard_data)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'csv_file' not in request.files:
        return "No file part", 400

    file = request.files['csv_file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.csv'):
        # Read the file stream and decode it
        file_stream = file.stream.read().decode("UTF8").splitlines()
        reader = csv.DictReader(file_stream)

        for row in reader:
            name = row.get('name')
            drill = row.get('drill')
            score = row.get('score')

            # Here, you can add validation if you want before inserting
            insert_entry(name, drill, score)

        return redirect('/')
    else:
        return "Invalid file type", 400

if __name__ == '__main__':
    app.run(debug=True)