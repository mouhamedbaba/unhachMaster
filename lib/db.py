import sqlite3


DATABASE = 'database.sqlite3'
def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS hashed_passwords
                 (password_hash text unique, password text unique)''')
    conn.commit()
    conn.close()

def insert_into_db(hash, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO hashed_passwords VALUES (?, ?)", (hash, password))
    conn.commit()
    conn.close()

def check_in_db(hash):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM hashed_passwords WHERE password_hash=?", (hash,))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_db_data():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM hashed_passwords")
    db_data = c.fetchall()
    conn.close()

    formatted_data = [{'hash': row[0], 'password': row[1]} for row in db_data]
    return {'data': formatted_data}