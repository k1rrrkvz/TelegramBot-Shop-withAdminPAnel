import sqlite3
from aiogram.types import User

class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT,
                username TEXT
            )
        """)

    def add_user(self, user: User):
        self.cursor.execute("INSERT INTO users (id, first_name, last_name, username) VALUES (?, ?, ?, ?)",
                            (user.id, user.first_name, user.last_name, user.username))
        self.connection.commit()

    def close(self):
        self.connection.close()
