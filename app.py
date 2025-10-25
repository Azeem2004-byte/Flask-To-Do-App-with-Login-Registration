from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

# Database helper
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

# ------------------------
# User Authentication
# ------------------------

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            try:
                with get_db_connection() as conn:
                    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                    conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "Username already exists!"
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with get_db_connection() as conn:
            user = conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password)).fetchone()
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            return "Invalid username or password!"
    return render_template('login.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ------------------------
# To-Do Routes (Protected)
# ------------------------
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with get_db_connection() as conn:
        tasks = conn.execute('SELECT * FROM tasks WHERE user_id=?', (user_id,)).fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = request.form.get('task')
    if task:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO tasks (name, user_id) VALUES (?, ?)', (task, session['user_id']))
            conn.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    with get_db_connection() as conn:
        conn.execute('DELETE FROM tasks WHERE id=? AND user_id=?', (task_id, session['user_id']))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
