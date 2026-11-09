import sqlite3

def get_user_by_username(db_path, username):
    """
    Look up a user by username and return their row.

    Args:
        db_path (str): Path to the SQLite database file.
        username (str): Username to search for.

    Returns:
        tuple or None: The matching row, or None if no user is found.
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()

        # Use a parameterized query to prevent SQL injection
        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        return cursor.fetchone()
    finally:
        conn.close()