import os
import time
from datetime import datetime
from random import random
from vector_db import VectorDB
from data_object import DataObject
from word_generator import generate_sentence

def create_stress_test_table(db):
    with db._connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vector_data (
                            id INTEGER PRIMARY KEY,
                            timestamp TEXT NOT NULL,
                            message TEXT NOT NULL,
                            vector BLOB NOT NULL)''')
        conn.commit()

def stress_test(db, num_entries, num_searches):
    start_time = time.time()

    # Add entries to the database
    for i in range(num_entries):
        sentence = generate_sentence()
        vector = [random() for _ in range(3)]
        entry = DataObject(timestamp=datetime.now(), message=sentence, vector=vector)
        db.add_entry(entry)

    print(f"Added {num_entries} entries in {time.time() - start_time:.2f} seconds")

    # Build and save the index
    db.save_index("vector_index.ann")

    # Load the index
    db.load_index("vector_index.ann")

    # Perform similarity searches
    search_start_time = time.time()
    for _ in range(num_searches):
        query_vector = [random() for _ in range(3)]
        search_results = db.search_entries(query_vector, num_results=10)

    print(f"Performed {num_searches} similarity searches in {time.time() - search_start_time:.2f} seconds")

if __name__ == "__main__":
    db_path = os.path.join(os.getcwd(), "stress_test.db")
    db = VectorDB(db_path=db_path)
    create_stress_test_table(db)
    stress_test(db, num_entries=100, num_searches=10)
