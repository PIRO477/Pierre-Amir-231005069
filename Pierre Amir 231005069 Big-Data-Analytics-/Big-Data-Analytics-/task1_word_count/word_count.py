"""Task 1 - Word Count
Mapper  emits (word, 1)
Reducer sums counts per word

Usage: python word_count.py [data_dir]
"""
import os, re, sys, glob
from collections import defaultdict

def tokenize(line):
    """Lowercase and strip punctuation."""
    return re.findall(r"[a-z0-9]+", line.lower())

def shuffle(pairs):
    """Group all mapper output values by key (across all files)."""
    groups = defaultdict(list)
    for key, value in pairs:
        groups[key].append(value)
    return groups

def mapper(file_name, line):
    for word in tokenize(line):
        yield (word, 1)

def reducer(word, counts):
    return sum(counts)

def word_count(data_dir):
    pairs = []
    for path in sorted(glob.glob(os.path.join(data_dir, "book_*.txt"))):
        name = os.path.basename(path)
        with open(path) as f:
            for line in f:
                pairs.extend(mapper(name, line))
    return {w: reducer(w, c) for w, c in sorted(shuffle(pairs).items())}

if __name__ == "__main__":
    data_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "data")
    result = word_count(data_dir)
    with open("output.txt", "w") as out:
        for w, n in result.items():
            out.write(f"{w} {n}\n")
            print(w, n)
    print(f"\nUnique words: {len(result)} | Total words: {sum(result.values())}")
