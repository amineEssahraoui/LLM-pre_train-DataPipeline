import os
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.readers import JsonlReader
from datatrove.pipeline.tokens import DocumentTokenizer

os.environ["PYTHONIOENCODING"] = "utf-8"

# Configuration 
DATASET_NAME = "minipile" # Our dataset 
TOKENIZER_NAME = "core42/jais-13b-chat" # Our tokenizer
tokenizer_short_name = TOKENIZER_NAME.split("/")[-1]

# Path to the raw JSONL files we created earlier
INPUT_PATH = "./output/samples_data"
# Path to store tokenized data
OUTPUT_PATH = f"./output/data_tokenized_{tokenizer_short_name}"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Pipeline definition 
pipeline = [
    # Read the local JSONL files
    JsonlReader(
        data_folder=INPUT_PATH,
        file_encoding="utf-8",
    ),
    
    # Tokenize the text using Jais and save as Binary Indexed files
    DocumentTokenizer(
        output_folder=OUTPUT_PATH,
        tokenizer_name_or_path=TOKENIZER_NAME,
        # max_tokens_per_file: splits data into chunks (for example 100M tokens)
        max_tokens_per_file=100_000_000, 
    )
]

# Execution 
if __name__ == "__main__":
    # LocalPipelineExecutor manages the multi-processing
    executor = LocalPipelineExecutor(
        pipeline=pipeline,
        tasks=4,    # Number of parallel tasks
        workers=4,  # Number of CPU cores to use
        start_method="spawn" # Required for Windows compatibility
    )
    
    print(f"Starting Tokenization with {TOKENIZER_NAME}...")
    print(f"Output will be saved in: {OUTPUT_PATH}")
    
    executor.run()
    
    print(f"Tokenization complete! Check the .ds and .index files in {OUTPUT_PATH}")