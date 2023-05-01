# database.py
import sqlite3
from data_object import DataObject

def create_database():
    conn = sqlite3.connect("src/vector_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vector_data (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME,
        message TEXT,
        vector BLOB
    );
    """)

    conn.commit()
    conn.close()

def delete_database():
    conn = sqlite3.connect("src/vector_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    DROP TABLE vector_data;
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    #create_database()
    delete_database()
