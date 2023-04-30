import pickle
from .b_plus_tree import BPlusTree


class CustomKVStore:
    def __init__(self, db_file):
        self.db_file = db_file
        self.tree = self.load_tree()

    def load_tree(self):
        try:
            with open(self.db_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return BPlusTree(order=4)

    def save_tree(self):
        with open(self.db_file, 'wb') as f:
            pickle.dump(self.tree, f)

    def put(self, key, value):
        self.tree.insert(key, value)
        self.save_tree()

    def get(self, key):
        return self.tree.get(key)

    def delete(self, key):
        self.tree.delete(key)
        self.save_tree()
