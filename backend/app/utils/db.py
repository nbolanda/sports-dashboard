import sqlite3

def init_db():
    conn = sqlite3.connect("data/sports.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            sport TEXT,
            stat_type TEXT,
            value REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_stat(player_name, sport, stat_type, value, date):
    conn = sqlite3.connect("data/sports.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stats (player_name, sport, stat_type, value, date) VALUES (?, ?, ?, ?, ?)",
                   (player_name, sport, stat_type, value, date))
    conn.commit()
    conn.close()

def get_player_stats(sport, player_name):
    conn = sqlite3.connect("data/sports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats WHERE sport=? AND player_name=?", (sport, player_name))
    result = cursor.fetchall()
    conn.close()
    return result
