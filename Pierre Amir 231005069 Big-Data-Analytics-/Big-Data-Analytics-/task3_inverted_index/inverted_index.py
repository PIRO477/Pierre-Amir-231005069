"""Task 3 - Inverted Index
Mapper  emits (word, file_name)
Reducer builds a unique list of files per word

Usage: python inverted_index.py [data_dir]
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
        yield (word, file_name)

def reducer(word, file_names):
    return sorted(set(file_names))

def inverted_index(data_dir):
    pairs = []
    for path in sorted(glob.glob(os.path.join(data_dir, "book_*.txt"))):
        name = os.path.basename(path)
        with open(path) as f:
            for line in f:
                pairs.extend(mapper(name, line))
    return {w: reducer(w, f) for w, f in sorted(shuffle(pairs).items())}

if __name__ == "__main__":
    data_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "data")
    result = inverted_index(data_dir)
    with open("output.txt", "w") as out:
        for w, files in result.items():
            out.write(f"{w}\t{', '.join(files)}\n")
            print(f"{w:<15} {files}")
