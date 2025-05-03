from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Initialize database with password field
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            email TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    mode = request.form['mode']  # register or login
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE name = ? AND email = ?', (name, email))
    user = c.fetchone()

    if mode == "register":
        if user:
            conn.close()
            return "<h3>User already exists!</h3><a href='/'>Back</a>"
        hashed_password = generate_password_hash(password)
        c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))
        conn.commit()
        conn.close()
        return "<h3>Registered successfully!</h3><a href='/'>Back to login</a>"

    elif mode == "login":
        if user:
            stored_password = user[2]
            if check_password_hash(stored_password, password):
                conn.close()
                return redirect(url_for('test'))
            else:
                conn.close()
                return "<h3>Incorrect password. Try again.</h3><a href='/'>Back</a>"
        else:
            conn.close()
            return "<h3>User not found. Please register.</h3><a href='/'>Back</a>"

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
