"""Task 2 - Top-K Words
Runs Word Count (mapper emits (word, 1), reducer sums), then uses the
reducer output to find the K most frequent words.

Usage: python top_k.py [K] [data_dir]
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
    return {w: reducer(w, c) for w, c in shuffle(pairs).items()}

def top_k(counts, k):
    # highest count first; ties broken alphabetically
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

if __name__ == "__main__":
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    data_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join("..", "data")
    result = top_k(word_count(data_dir), k)
    with open("output.txt", "w") as out:
        for rank, (w, n) in enumerate(result, 1):
            out.write(f"{w} {n}\n")
            print(f"{rank:>2}. {w:<12} {n}")
