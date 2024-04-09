import sqlite3
import os

# Get the absolute path of the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data/watchlist.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS anime (id INTEGER PRIMARY KEY, name TEXT, status INTEGER)")

def create_anime(name):
    c.execute("INSERT INTO anime (name, status) VALUES (?, 0)", (name,))
    conn.commit()

def get_watchlist():
    c.execute("SELECT * FROM anime")
    return c.fetchall()

def update_anime_status(anime_id, status):
    c.execute("UPDATE anime SET status=? WHERE id=?", (status, anime_id))
    conn.commit()

def delete_anime(anime_id):
    c.execute("DELETE FROM anime WHERE id=?", (anime_id,))
    conn.commit()

create_table()
