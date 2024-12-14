#!/bin/bash

# arg1 = Model

mkdir -p data
touch data/data_space_$1.jsonl
> data/data_space_$1.jsonl
for i in $(seq 0 4);
do
    python3 run.py --do_eval --task nli --dataset snli --model ../models/$1 --output_dir ./eval_output_auto/ --remove_spaces $i | tail -n 1 | tr "'" '"' >> data/data_space_$1.jsonl;
done