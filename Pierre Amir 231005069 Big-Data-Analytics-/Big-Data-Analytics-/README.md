# Big-Data-Analytics-

**Student name:** YOUR NAME HERE
**Student ID:** YOUR STUDENT ID HERE

## Student Instructions
1. Fork this repository to your GitHub account.
2. Complete each programming task in its own folder in your fork, and push your work there.
3. Add your name and student ID to this README in your fork.

## Repository layout
| Folder | Contents |
|---|---|
| `data/` | The five sample text files (`book_01.txt` to `book_05.txt`) |
| `task1_word_count/` | Word Count |
| `task2_top_k/` | Top-K Words |
| `task3_inverted_index/` | Inverted Index |
| `notebook/` | Google Colab notebook that runs all three tasks |

Each task folder has its own script, README and `output.txt`. Run from inside the task folder, for example `cd task1_word_count && python word_count.py`.

---

# Sample Dataset for MapReduce Testing
This directory contains multiple plain-text files that students can use to test their own Map-Reduce implementations (for example, Word Count, Inverted Index, and simple frequency analysis).

## Files
* `book_01.txt`
* `book_02.txt`
* `book_03.txt`
* `book_04.txt`
* `book_05.txt`

## Suggested Exercises
1. Word Count
   * Mapper emits `(word, 1)`
   * Reducer sums counts per word
2. Top-K Words
   * Use reducer output to find the most frequent words
3. Inverted Index
   * Mapper emits `(word, file_name)`
   * Reducer builds a unique list of files per word

## Notes
* Files are intentionally small so they can run quickly in local and educational setups.
* Content overlaps across files so reducers can be validated for key aggregation across multiple mapper outputs.
