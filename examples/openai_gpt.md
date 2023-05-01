# Example of using PyVecDB with OpenAI GPT

This example demonstrates how to use the PyVecDB library with the OpenAI GPT language model to give it long-term memory. We will create a database of sentences and their embeddings using the `VectorDB` class and then use it to provide context to the GPT model when generating new text.

## Installation

Before running the example, you need to install the PyVecDB library and the necessary dependencies:

```bash
pip install PyVecDB transformers torch
```

## Code

```python
from PyVecDB.vector_db import VectorDB
from datetime import datetime
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Initialize the GPT model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set the device to use for running the model (CPU or GPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Create a new database
db = VectorDB()

# Add some sentences to the database
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife",
    "To be or not to be, that is the question",
    "In the beginning God created the heaven and the earth",
    "All happy families are alike; each unhappy family is unhappy in its own way",
    "A spectre is haunting Europe—the spectre of communism",
    "Once upon a time, in a faraway land, there lived a princess named Cinderella",
    "Call me Ishmael",
    "It was the best of times, it was the worst of times",
    "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer"
]

for sentence in sentences:
    input_ids = torch.tensor(tokenizer.encode(sentence)).unsqueeze(0).to(device)
    with torch.no_grad():
        last_hidden_states = model.transformer(input_ids)[0][:, -1, :]
        vector = last_hidden_states.cpu().numpy().tolist()[0]
    timestamp = datetime.now()
    entry = DataObject(timestamp=timestamp, message=sentence, vector=vector)
    db.add_entry(entry)

# Generate new text using the GPT model and the database
context_vectors = [db.search_entries(tokenizer.encode(sentence).unsqueeze(0).to(device).tolist()[0], num_results=1)[0].get_vector() for sentence in sentences]
context_vectors = torch.tensor(context_vectors).to(device)

input_ids = tokenizer.encode("In the beginning", return_tensors='pt').to(device)

for i in range(100):
    with torch.no_grad():
        output = model(input_ids=input_ids, past=None, attention_mask=None, context_vectors=context_vectors)
        logits = output.logits[:, -1, :]
        softmax_logits = torch.softmax(logits, dim=-1).squeeze()
        next_token = torch.multinomial(softmax_logits, num_samples=1)
        input_ids = torch.cat((input_ids, next_token), dim=-1)

    generated_text = tokenizer.decode(input_ids.squeeze().tolist())
    print(generated_text)
```

## Output

In the beginning God created the heaven and the earth, and the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light.

And God saw the light, that it
