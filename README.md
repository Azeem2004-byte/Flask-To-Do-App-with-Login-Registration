
## 🔹 `README.md`

```markdown
# Flask To-Do App with Login & Registration

A simple **Flask To-Do web application** with **user authentication** and **personal task management** using **SQLite**.

---

## Features

- User Registration & Login
- Add, Delete, and View personal tasks
- Each user's tasks are private
- Simple, clean interface with CSS
- Easy to setup and run locally

---

## Project Structure

```

todo-flask-app/
│
├── todo_web/                   # Main project folder
│   ├── app.py                  # Flask application
│   ├── todo.db                 # SQLite database
│   ├── templates/              # HTML templates
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   └── static/                 # Optional: CSS, JS, images
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Azeem2004-byte/Flask-To-Do-App-with-Login-Registration.git
cd Flask-To-Do-App-with-Login-Registration
````

2. Create a virtual environment (recommended):

```bash
python -m venv venv
# Activate the virtual environment:
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

1. Open **DB Browser for SQLite** or Python shell.
2. Create the database `todo.db` and tables:

```sql
-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id INTEGER
);
```

---

## Running the App

```bash
python todo_web/app.py
```

Open browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Usage

1. **Register** a new user
2. **Login** with your credentials
3. **Add, view, and delete** tasks
4. **Logout** when done


## License

This project is **free to use and modify**.



