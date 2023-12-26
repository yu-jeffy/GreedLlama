import json
import os
import sys
from collections import Counter

# USAGE: python tally.py <path-to-your-jsonl-file>

def tally_results(jsonl_file):
    tally_counter = Counter()

    with open(jsonl_file, 'r') as file:
        for line in file:
            entry = json.loads(line)
            answer = entry.get("answer", "Error Retrieving Answer")
            tally_counter[answer] += 1

    return tally_counter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tally.py <path-to-jsonl-file>")
        sys.exit(1)

    jsonl_file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.isfile(jsonl_file_path):
        print(f"The file {jsonl_file_path} does not exist.")
        sys.exit(1)

    results = tally_results(jsonl_file_path)
    print(f"Tally of answers in {jsonl_file_path}:")
    for answer, count in results.items():
        print(f"{answer}: {count}")