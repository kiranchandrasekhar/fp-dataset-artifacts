import json

# with open('./eval_output/mismatched_examples.jsonl', 'r') as file:
#     data1 = file.read()

# with open('./eval_output/mismatched_examples_og.jsonl', 'r') as file:
#     data2 = file.read()

output_file_path = "./eval_output/id_diff.jsonl"

# Open the input file for reading and the output file for writing
with open("./eval_output/mismatched_examples.jsonl", 'r') as infile1, open("./eval_output/mismatched_examples_og.jsonl", 'r') as infile2, open(output_file_path, 'w') as outfile:
    i = 0
    j = 0
    f1_exs = {}
    f2_exs = {}

    for line in infile1:
        j1 = json.loads(line)
        f1_exs[j1['id']] = j1
    
    for line in infile2:
        j2 = json.loads(line)
        f2_exs[j2['id']] = j2

    mutually_exclusive = f1_exs.keys() - f2_exs.keys()
    mutually_exclusive = mutually_exclusive | (f2_exs.keys() - f1_exs.keys())

    for id in mutually_exclusive:
        if id in f1_exs.keys():
            f1_exs[id]['mispredicted'] = 'changed'
            outfile.write(json.dumps(f1_exs[id]) + '\n')
        elif id in f2_exs.keys():
            f2_exs[id]['mispredicted'] = 'og'
            outfile.write(json.dumps(f2_exs[id]) + '\n')


print(f"Mismatched examples have been written to {output_file_path}")