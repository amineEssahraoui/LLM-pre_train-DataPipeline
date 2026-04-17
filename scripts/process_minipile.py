import os
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.readers import HuggingFaceDatasetReader
from datatrove.pipeline.tokenizers import DocumentTokenizer
from datatrove.pipeline.writers import JsonlWriter

DATASET_NAME = "JeanKaddour/minipile"   # Miniple dataset
TOKENIZER_NAME = "core42/jais-13b-chat" # Jais tokenizer
OUTPUT_PATH = "./output/tokenized_data" # Folder to store tokenized data 

