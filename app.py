import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Σκληροκωδικοποιημένος κωδικός πρόσβασης
SECRET_PASSWORD = "password123"

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Welcome to the Vulnerable App!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # SQL Injection ευπάθεια
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(query)
    result = c.fetchone()
    conn.close()

    if result:
        return "Login successful!"
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
