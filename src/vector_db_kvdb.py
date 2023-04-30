from datetime import datetime
from typing import List
import msgpack
from annoy import AnnoyIndex
from data_object import DataObject

VECTOR_DIMENSION = 3

class VectorDB:
    def __init__(self, index_path: str = "vector_index.ann", data_path: str = "vector_data.bin"):
        self.index_path = index_path
        self.data_path = data_path
        self.index = AnnoyIndex(VECTOR_DIMENSION, metric="angular")
        self.id_map = {}

    def save_index(self):
        self.index.build(10)  # Number of trees, higher values give better accuracy but longer build time
        self.index.save(self.index_path)

    def load_index(self):
        self.index.load(self.index_path)

    def add_entry(self, entry: DataObject):
        with open(self.data_path, "ab") as f:
            serialized_vector = msgpack.packb(entry.vector)
            f.write(serialized_vector)
            entry.id = f.tell() - len(serialized_vector)  # Get the offset of the serialized vector as the ID
            integer_id = len(self.id_map)
            self.id_map[entry.id] = integer_id
            self.index.add_item(integer_id, entry.vector)

    def get_entry(self, id: int) -> DataObject:
        with open(self.data_path, "rb") as f:
            f.seek(id)
            serialized_vector = f.read()
        if serialized_vector:
            vector = msgpack.unpackb(serialized_vector)
            return DataObject(id=id, vector=vector)
        else:
            return None

    def delete_entry(self, id: int):
        raise NotImplementedError

    def update_entry(self, entry: DataObject):
        raise NotImplementedError

    def search_entries(self, vector: List[float], num_results: int = 10) -> List[DataObject]:
        nearest_integer_ids = self.index.get_nns_by_vector(vector, num_results)
        nearest_ids = [list(self.id_map.keys())[list(self.id_map.values()).index(integer_id)] for integer_id in nearest_integer_ids]

        entries = []
        for entry_id in nearest_ids:
            entry = self.get_entry(entry_id)
            if entry:
                entries.append(entry)

        return entries
    
if __name__ == "__main__":
    # Test the API
    db = VectorDB()

    # Add some entries
    db.add_entry(DataObject(timestamp=datetime.now(), message="Hello", vector=[1, 2, 3]))
    db.add_entry(DataObject(timestamp=datetime.now(), message="World", vector=[4, 5, 6]))
    db.add_entry(DataObject(timestamp=datetime.now(), message="Foo", vector=[7, 8, 9]))

    # Save the index
    db.save_index()


    # Load the index
    db.load_index()

    # Search for entries
    results = db.search_entries([1, 2, 3])
    print(results)
    results = db.search_entries([4, 5, 6])
    print(results)

    # Get an entry by ID
    entry = db.get_entry(0)
    print(entry)

    # Delete an entry
    db.delete_entry(0)
    entry = db.get_entry(0)
    print(entry)

    # Update an entry
    entry = db.get_entry(1)
    entry.message = "Updated message"
    db.update_entry(entry)
    entry = db.get_entry(1)
    print(entry)

    
