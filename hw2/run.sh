#! /usr/bin/env bash
#python3 transfer_train.py
python transfer_to_json.py $1 input.json
python summarization.py --model_name_or_path model_v4 --train_file train_few.json  --validation_file input.json --text_column maintext --summary_column title --output_dir model_v4  --per_device_eval_batch_size 8  --num_train_epochs 1  --learning_rate 5e-4  --num_beams 4 --max_source_length 1024 --max_target_length 128 
mv submission.jsonl $2
