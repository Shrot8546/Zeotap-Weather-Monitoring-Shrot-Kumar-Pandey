import sqlite3

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            max_temp REAL,
            min_temp REAL,
            condition TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            average_temperature REAL,
            maximum_temperature REAL,
            minimum_temperature REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()
