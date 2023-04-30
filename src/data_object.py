# data_object.py
from datetime import datetime
from typing import List

class DataObject:
    def __init__(self, timestamp: datetime, message: str, vector: List[float], id: int = None):
        self.id=id
        self.timestamp = timestamp
        self.message = message
        self.vector = vector

    def __repr__(self):
        return f"<DataObject id={self.id} timestamp={self.timestamp} message={self.message} vector={self.vector}>"

    def __str__(self):
        return f"DataObject(\n  id={self.id},\n  timestamp={self.timestamp},\n  message='{self.message}',\n  vector={self.vector}\n)"
