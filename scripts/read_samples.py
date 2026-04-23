import gzip
import json
import os

# Data path 
file_path = "./output/tokenized_data/00000.jsonl.gz"

# Check if file_path already exists
if not os.path.exists(path=file_path):
    print(f"Error: File {file_path} not found!")
else: 
    print(f"Reading smples from {file_path}\n")
    # Open gzip file
    with gzip.open(file_path, 'rt', encoding='utf-8') as f: 
        for i, line in enumerate(f): 
            data = json.loads(line)
            print(f"Example {i+1}")
            # Read only the first 200 characters
            print(f"Text : {data['text'][:200]}...")
            print("-" * 30)
            # Only 10 examples
            if i >= 10: 
                break 
