import random
from collections import defaultdict

text = """
Artificial intelligence is transforming the world.
Artificial intelligence helps in automation.
Machine learning is a part of artificial intelligence.
AI is used in healthcare, education, and many industries.
"""


words = text.lower().split()

markov_chain = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    markov_chain[current_word].append(next_word)

def generate_text(start_word, length=30):
    current_word = start_word.lower()
    result = [current_word]

    for _ in range(length):
        next_words = markov_chain.get(current_word)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word

    return " ".join(result)

output = generate_text("artificial", 25)
print("Generated Text:\n")
print(output)
