import random

# List of words to use in sentences
nouns = ["dog", "cat", "bird", "fish", "computer", "book"]
verbs = ["runs", "jumps", "eats", "sleeps", "reads"]
adjectives = ["happy", "sad", "angry", "funny", "silly"]
adverbs = ["quickly", "slowly", "easily", "hardly", "happily"]

# Function to generate a random sentence
def generate_sentence():
    sentence = []
    sentence.append(random.choice(nouns))
    sentence.append(random.choice(verbs))
    sentence.append(random.choice(adverbs))
    sentence.append(random.choice(adjectives))
    sentence.append(random.choice(nouns))
    return " ".join(sentence)

# Test the function by generating 5 random sentences
for i in range(5):
    print(f"Sentence {i}: {generate_sentence()}")
