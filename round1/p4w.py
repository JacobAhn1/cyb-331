import sqlite3
import hashlib

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password before storing it
password_hash = hashlib.sha256(password.encode()).hexdigest()

try:
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    conn.commit()
    print("User registered successfully!")
except sqlite3.IntegrityError:
    print("Username already exists.")

conn.close()