import json

# Paths to the input and output files
input_file_path = "/Users/tarun1/NLP_Final_Project/fp-dataset-artifacts/eval_output/eval_predictions.jsonl"
output_file_path = "/Users/tarun1/NLP_Final_Project/fp-dataset-artifacts/eval_output/mismatched_examples.jsonl"

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        # Load each line as a JSON object
        example = json.loads(line)
        
        # Check for mismatched label and predicted_label
        if example["label"] != example["predicted_label"]:
            # Write the mismatched example to the output file in JSONL format
            outfile.write(json.dumps(example) + '\n')

print(f"Mismatched examples have been written to {output_file_path}")
