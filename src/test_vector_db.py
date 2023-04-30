import pytest
from datetime import datetime
from random import random
from vector_db import VectorDB
from data_object import DataObject

@pytest.fixture
def vector_db():
    db = VectorDB(db_path=":memory:")
    return db

def test_add_retrieve_entry(vector_db):
    entry = DataObject(timestamp=datetime.now(), message="Test message", vector=[random() for _ in range(3)])
    vector_db.add_entry(entry)

    retrieved_entry = vector_db.get_entry(entry.id)
    assert entry == retrieved_entry

def test_delete_entry(vector_db):
    entry = DataObject(timestamp=datetime.now(), message="Test message", vector=[random() for _ in range(3)])
    vector_db.add_entry(entry)

    vector_db.delete_entry(entry.id)
    deleted_entry = vector_db.get_entry(entry.id)
    assert deleted_entry is None

def test_update_entry(vector_db):
    entry = DataObject(timestamp=datetime.now(), message="Test message", vector=[random() for _ in range(3)])
    vector_db.add_entry(entry)

    entry.message = "Updated message"
    vector_db.update_entry(entry)

    updated_entry = vector_db.get_entry(entry.id)
    assert entry == updated_entry

def test_search_entries(vector_db):
    for _ in range(50):
        entry = DataObject(timestamp=datetime.now(), message="Test message", vector=[random() for _ in range(3)])
        vector_db.add_entry(entry)

    query_vector = [random() for _ in range(3)]
    search_results = vector_db.search_entries(query_vector, num_results=10)
    
    assert len(search_results) == 10
    assert isinstance(search_results[0], DataObject)
