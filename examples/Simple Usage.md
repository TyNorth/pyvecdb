# Simple Usage Example

This example demonstrates the basic usage of the PyVecDB library.

## Installation

Before you can run this example, you need to install the PyVecDB library:

```bash
pip install PyVecDB
```

## Code

```python
from PyVecDB.vector_db import VectorDB
from PyVecDB.data_object import DataObject
from datetime import datetime
from random import random

# Create a new database
db = VectorDB()

# Create some new entries
for i in range(10):
    timestamp = datetime.now()
    message = f"Entry {i}"
    vector = [random() for _ in range(3)]

    entry = DataObject(timestamp=timestamp, message=message, vector=vector)
    db.add_entry(entry)

# Search for entries
query_vector = [0.1, 0.2, 0.3]
search_results = db.search_entries(query_vector, num_results=10)

print("Search Results:")
for entry in search_results:
    print(f"  ID: {entry.get_id()}")
    print(f"  Timestamp: {entry.get_timestamp()}")
    print(f"  Message: {entry.get_message()}")
    print(f"  Vector: {entry.get_vector()}")
```

## Output

```yaml
Search Results:
  ID: 2
  Timestamp: 2023-05-01 16:05:12.412748
  Message: Entry 2
  Vector: [0.27330326714879486, 0.8401535163540257, 0.8445818767827713]
  ID: 7
  Timestamp: 2023-05-01 16:05:12.422913
  Message: Entry 7
  Vector: [0.6660317286313857, 0.42228458098278225, 0.8073470886181337]
  ID: 0
  Timestamp: 2023-05-01 16:05:12.407703
  Message: Entry 0
  Vector: [0.15647496334598193, 0.2701583922362499, 0.3593262792592265]
  ID: 5
  Timestamp: 2023-05-01 16:05:12.420580
  Message: Entry 5
  Vector: [0.8534412151064184, 0.4320915762822669, 0.16010098116464045]
  ID: 3
  Timestamp: 2023-05-01 16:05:12.416183
  Message: Entry 3
  Vector: [0.1535748597276914, 0.8770818147559194, 0.24303339434625936]
  ID: 1
  Timestamp: 2023-05-01 16:05:12.408717
  Message: Entry 1
  Vector: [0.9313735993060893, 0.5344316010234419, 0.05586543813522563]
  ID: 6
  Timestamp: 2023-05-01 16:05:12.421496
  Message: Entry 6
  Vector: [0.09715483325327616, 0.1263097068314791, 0.9688645842852787]
  ID: 8
  Timestamp: 2023-05-01 16:05:12.424074
  Message: Entry 8
  Vector: [0.06290250030776791, 0.1687643945161295, 0.6964769785305176]
ID: 9
Timestamp: 2023-05-01 16:05:12.425407
Message: Entry 9
Vector: [0.3540737286306674, 0.2442843714708023, 0.4310152066974993]
```

In this example, we created a new `VectorDB` object and added 10 entries to it. We then searched for entries using a randomly generated query vector and printed out the results.

Note that the exact output will vary each time you run this example due to the random nature of the data.
