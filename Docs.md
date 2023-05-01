# PyVecDB Documentation

Welcome to the PyVecDB documentation! Here, you will find a detailed guide on how to use the PyVecDB library for storing and searching high-dimensional vectors using the Annoy approximate nearest neighbors search library.

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [API Reference](#api-reference)
  - [VectorDB Class](#vectordb-class)
  - [DataObject Class](#dataobject-class)
- [Examples](#examples)
  - [Using PyVecDB with Text Data](#using-pyvecdb-with-text-data)
  - [Using PyVecDB with Image Data](#using-pyvecdb-with-image-data)
- [Advanced Topics](#advanced-topics)
  - [Customizing Annoy Parameters](#customizing-annoy-parameters)
  - [Performance Tuning](#performance-tuning)

## Getting Started

### Installation

You can install PyVecDB using pip:

```bash
pip install pyvecdb
```

### Basic Usage

Here's a simple example that demonstrates how to use PyVecDB:

```python
from datetime import datetime
from random import random
from pyvecdb import VectorDB, DataObject

# Initialize the database
db = VectorDB(db_path="vector_data.db")

# Create a new entry
entry = DataObject(timestamp=datetime.now(), message="Example message", vector=[random() for _ in range(3)])
db.add_entry(entry)

# Save the Annoy index
db.save_index("vector_index.ann")

# Load the Annoy index
db.load_index("vector_index.ann")

# Search for similar entries
entries = db.search_entries(vector=entry.vector, num_results=10)
```

## API Reference

### VectorDB Class

The `VectorDB` class is the main interface for working with PyVecDB. It provides methods for adding, updating, deleting, and searching entries in the database.

#### `__init__(self, db_path: str = "vector_data.db")`

Constructor for the `VectorDB` class. Initializes the database and Annoy index.

Parameters:

- `db_path` (str): Path to the SQLite database file. Default is `"vector_data.db"`.

#### `add_entry(self, entry: DataObject)`

Adds a new entry to the database and the Annoy index.

Parameters:

- `entry` (DataObject): The `DataObject` to add to the database.

#### `get_entry(self, id: int) -> DataObject`

Retrieves an entry from the database by its ID.

Parameters:

- `id` (int): The ID of the entry to retrieve.

Returns:

- DataObject: The `DataObject` corresponding to the given ID, or `None` if the ID is not found.

#### `delete_entry(self, id: int)`

Deletes an entry from the database.

Parameters:

- `id` (int): The ID of the entry to delete.

#### `update_entry(self, entry: DataObject)`

Updates an existing entry in the database.

Parameters:

- `entry` (DataObject): The updated `DataObject` with the same ID as the entry to update.

#### `search_entries(self, vector: List[float], num_results: int = 10) -> List[DataObject]`

Performs a nearest neighbor search in the Annoy index and returns the corresponding `DataObject` entries.

Parameters:

- `vector` (List[float]): The query vector.
- `num_results` (int): The number of nearest neighbors to return. Default is 10

#### `save_index(self, file_name: str)`

Saves the Annoy index to a file.

Parameters:

- `file_name` (str): The path to the file where the index should be saved.

#### `load_index(self, file_name: str)`

Loads a previously saved Annoy index from a file.

Parameters:

- `file_name` (str): The path to the file containing the saved index.

### DataObject Class

The `DataObject` class represents an entry in the PyVecDB database. It contains a unique ID, timestamp, message, and high-dimensional vector.

#### `__init__(self, id: int = None, timestamp: Union[str, datetime] = None, message: str = None, vector: List[float] = None)`

Constructor for the `DataObject` class.

Parameters:

- `id` (int, optional): The unique ID of the entry. Default is `None`.
- `timestamp` (str or datetime, optional): The timestamp of the entry. Default is `None`.
- `message` (str, optional): A message associated with the entry. Default is `None`.
- `vector` (List[float], optional): The high-dimensional vector of the entry. Default is `None`.

## Examples

### Using PyVecDB with Text Data

To use PyVecDB with text data, you can generate high-dimensional vectors for your text documents using any text embedding method, such as Word2Vec, GloVe, or BERT. Then, create a `DataObject` for each document and add it to the database using the `add_entry` method.

### Using PyVecDB with Image Data

To use PyVecDB with image data, you can generate high-dimensional vectors for your images using any image embedding method, such as ResNet, Inception, or VGG. Then, create a `DataObject` for each image and add it to the database using the `add_entry` method.

## Advanced Topics

### Customizing Annoy Parameters

The default Annoy parameters provided in the `VectorDB` class may not be suitable for all applications. You can customize the Annoy parameters by modifying the `VECTOR_DIMENSION` and `METRIC` variables in the `VectorDB` class. Additionally, you can change the number of trees used when building the Annoy index in the `save_index` method.

### Performance Tuning

The performance of PyVecDB depends on various factors, such as the size of the dataset, the dimensionality of the vectors, and the number of trees used in the Annoy index. To optimize the performance of PyVecDB, you can try the following:

1. Increase the number of trees in the Annoy index to improve search accuracy at the cost of increased build time and memory usage.
2. Reduce the dimensionality of the input vectors using dimensionality reduction techniques, such as PCA or t-SNE.
3. Optimize the SQLite database by using appropriate indexes and tuning the cache size, journal mode, and other parameters.

Always test the performance of PyVecDB with your specific use case to determine the optimal configuration.
