import sqlite3

def create_table():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              drill TEXT NOT NULL,
              score REAL NOT NULL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_entry(name, drill, score):
    conn = sqlite3.connect('leaderboard.db') #opens database file
    c = conn.cursor() #creates a cursor to send SQL commands

    c.execute('''
        INSERT INTO leaderboard (name, drill, score)
        VALUES (?, ?, ?)
    ''', (name, drill, score)) #tells SQLite to add a new row, the tuple (name, drill, score) fills the place holders in the table in that specific order

    conn.commit()
    conn.close()

def get_entries_grouped_by_drill():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()

    c.execute('SELECT * FROM leaderboard')
    rows = c.fetchall()

    conn.close()

    drills = {}
    for row in rows:
        drill = row[2]
        drills.setdefault(drill, []).append(row)

     # Sorting logic by drill type
    for drill_name, entries in drills.items():
        if drill_name in ['beep-test', 'vert']:
            # Higher is better
            drills[drill_name] = sorted(entries, key=lambda x: float(x[3]), reverse=True)
        else:
            # Lower is better (default for sprints)
            drills[drill_name] = sorted(entries, key=lambda x: float(x[3]))

    return drills

def reset_leaderboard():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()
    c.execute('DELETE FROM leaderboard')
    conn.commit()
    conn.close()