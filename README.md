# PyVecDB

PyVecDB is a Python library that provides a simple way to store and search high-dimensional vectors using the Annoy approximate nearest neighbors search library. This library is useful for various applications, such as searching for similar items, clustering, or reducing search spaces in machine learning problems.

## Features

- Store high-dimensional vectors with associated metadata in an SQLite database
- Perform fast, approximate nearest neighbor searches using Annoy
- Easily add, update, and delete entries
- Serialize and deserialize vector data using MessagePack

## Installation

You can install PyVecDB using pip:

```bash
pip install pyvecdb
```

## Usage

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

## Documentation

For detailed documentation and examples, please visit the [official documentation](https://example.com/docs).

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) to get started.

## License

PyVecDB is released under the [MIT License](LICENSE).

## Support

If you like my work consider buying me a coffee ☕ Support my work on Patreon or PayPal!

[![Support me on Patreon](https://img.shields.io/badge/patreon-support-%23e85b46.svg?logo=patreon&style=for-the-badge)](https://www.patreon.com/SimulatedDev)

