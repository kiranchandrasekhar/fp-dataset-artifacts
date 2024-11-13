import json
from pathlib import Path
from functools import cmp_to_key

# Path to the input file and base directory for output files
input_file_path = "./eval_output/eval_predictions.jsonl"
output_dir = Path("./eval_output/mismatched_examples_sorted")

# Ensure the output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

# Dictionary to keep file handlers for each mismatch type
file_handlers = {}

# Function to get or create a file handler for a specific mismatch type
def get_file_handler(label, predicted_label):
    # Define the filename based on the label and predicted_label
    filename = f"label_{label}_predicted_{predicted_label}.jsonl"
    # Open the file in append mode if not already open
    if (label, predicted_label) not in file_handlers:
        file_handlers[(label, predicted_label)] = open(output_dir / filename, 'a')
    return file_handlers[(label, predicted_label)]

def compare(item1):
    return abs(item1["predicted_scores"][item1["predicted_label"]] - item1["predicted_scores"][item1["label"]])

# Open the input file and process each line
with open(input_file_path, 'r') as infile:
    examples = [json.loads(line) for line in infile]
    examples.sort(key=compare, reverse=False)

    for example in examples:
        # Load each line as a JSON object        
        # Check for mismatched label and predicted_label
        if example["label"] != example["predicted_label"]:
            # Get the file handler for the specific mismatch type
            outfile = get_file_handler(example["label"], example["predicted_label"])
            # Write the mismatched example to the appropriate output file
            outfile.write(json.dumps(example) + '\n')


# Close all file handlers
for handler in file_handlers.values():
    handler.close()

print(f"Mismatched examples have been written to files in {output_dir}")
