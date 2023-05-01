# data_object.py
from datetime import datetime
from typing import List

class DataObject:
    def __init__(self, timestamp: datetime, message: str, vector: List[float], id: int = None):
        self.id=id
        self.timestamp = timestamp
        self.message = message
        self.vector = vector

    def __repr__(self) -> str:
        return f"<DataObject(id={self.id}, timestamp={self.timestamp.isoformat()}, message={self.message}, vector={self.vector})>"

    def __str__(self) -> str:
        return f"DataObject:\n" \
               f"  ID: {self.id}\n" \
               f"  Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n" \
               f"  Message: {self.message}\n" \
               f"  Vector: {self.vector}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, DataObject):
            return False
        return self.id == other.id and self.vector == other.vector and self.message == other.message and self.timestamp == other.timestamp
    
    def __hash__(self) -> int:
        return hash((self.id, self.vector, self.message, self.timestamp))
    

    
    def get_id(self):
        return self.id
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_message(self):
        return self.message
    
    def get_vector(self):
        return self.vector
    
    def set_id(self, id):
        self.id = id

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp


    def set_message(self, message):
        self.message = message
