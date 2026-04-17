import os
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.readers import HuggingFaceDatasetReader
from datatrove.pipeline.tokenizers import DocumentTokenizer
from datatrove.pipeline.writers import JsonlWriter

# General parameters 
DATASET_NAME = "JeanKaddour/minipile"   # Miniple dataset
TOKENIZER_NAME = "core42/jais-13b-chat" # Jais tokenizer
OUTPUT_PATH = "./output/tokenized_data" # Folder to store tokenized data 

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Piplene 
pipeline = [
    # Read data 
    HuggingFaceDatasetReader(
        dataset = DATASET_NAME, 
        dataset_options = {"split" : "train"}, 
        limit = 1000,   # Use 1000 lines for faster testing
    ),

    # Tokenizer parameters
    DocumentTokenizer(
        output_folder = OUTPUT_PATH,
        tokenizer_name_or_path = TOKENIZER_NAME, 
        max_tokens_per_file = 100 * 1024 * 1024, 
    ),
]

if __name__ == "__main__": 
    executor = LocalPipelineExecutor(
        pipeline = pipeline, # Pipepline
        tasks = 4,           # CPU cores 
        workers = 4
    )
    print("Starting the Pipeline...")
    executor.run()
    print(f"Done! Check your tokens in: {OUTPUT_PATH}")