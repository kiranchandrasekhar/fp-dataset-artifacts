#!/bin/bash

# arg1 = Model

mkdir -p data
touch data/data_$1.jsonl
> data/data_$1.jsonl
for i in $(seq 0 5);
do
    python3 run.py --do_eval --task nli --dataset snli --model ./$1 --output_dir ./eval_output/ --remove_letters $i | tail -n 1 | tr "'" '"' >> data/data_$1.jsonl;
done