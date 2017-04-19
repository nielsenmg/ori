#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('frequencies.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS word_frequencies (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        word VARCHAR(255) NOT NULL,
        document VARCHAR(255) NOT NULL
);
""")

print('Database created sucessfully.')
conn.close()