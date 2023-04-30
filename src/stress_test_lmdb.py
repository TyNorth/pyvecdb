from datetime import datetime
from random import random
import time
from word_generator import generate_sentence
from data_object import DataObject
from vector_db_lmdb import VectorDB

def stress_test(num_entries: int, num_searches: int):
    db = VectorDB()
    
    # Add entries
    start_time = time.time()
    for _ in range(num_entries):
        new_sentence = generate_sentence()
        entry = DataObject(timestamp=datetime.now(), message=new_sentence, vector=[random() for _ in range(3)])
        db.add_entry(entry)
    end_time = time.time()
    add_duration = end_time - start_time
    
    # Save and load the index
    db.save_index("vector_index.ann")
    db.load_index("vector_index.ann")
    
    # Perform searches
    start_time = time.time()
    for _ in range(num_searches):
        query_vector = [random() for _ in range(3)]
        db.search_entries(query_vector)
    end_time = time.time()
    search_duration = end_time - start_time
    
    return add_duration, search_duration

if __name__ == "__main__":
    num_entries = 1000
    num_searches = 100
    
    add_duration, search_duration = stress_test(num_entries, num_searches)
    
    print(f"Added {num_entries} entries in {add_duration:.2f} seconds.")
    print(f"Performed {num_searches} searches in {search_duration:.2f} seconds.")
