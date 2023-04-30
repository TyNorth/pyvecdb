# file_handler.py

import pickle

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, bplus_tree):
        with open(self.file_path, 'wb') as f:
            pickle.dump(bplus_tree, f)

    def load(self):
        with open(self.file_path, 'rb') as f:
            bplus_tree = pickle.load(f)
        return bplus_tree
