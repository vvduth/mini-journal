import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, content TEXT, date TEXT)")


def add_entry(entry_content, entry_date):
    try:
        with connection:
            connection.execute("INSERT INTO entries (content, date) VALUES (?, ?)", (entry_content, entry_date))
    except:
        raise  Exception("Error adding entry to the database.")


def get_entries():
    cursor = connection.cursor()
    entries =  cursor.execute("SELECT * FROM entries")
    return  entries
