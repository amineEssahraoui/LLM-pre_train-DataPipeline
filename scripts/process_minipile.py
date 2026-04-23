import os
from datatrove.executor import LocalPipelineExecutor
from datatrove.pipeline.readers import HuggingFaceDatasetReader
from datatrove.pipeline.writers import JsonlWriter

# General parameters 
DATASET_NAME = "JeanKaddour/minipile"
TOKENIZER_NAME = "core42/jais-13b-chat"
OUTPUT_PATH = "./output/tokenized_data"

os.makedirs(OUTPUT_PATH, exist_ok=True)

pipeline = [
    HuggingFaceDatasetReader(
        dataset=DATASET_NAME,
        dataset_options={"split": "train"},
        limit=1000,
    ),
    JsonlWriter(
        output_folder=OUTPUT_PATH,
    ),
]

if __name__ == "__main__":
    executor = LocalPipelineExecutor(
        pipeline=pipeline,
        tasks=4,
        workers=4,
        start_method="spawn",  # Windows compatible
    )
    print("Starting the Pipeline...")
    executor.run()
    print(f"Done! Check output in: {OUTPUT_PATH}")