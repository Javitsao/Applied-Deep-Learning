#! /usr/bin/env bash
rm train_data.json test_data.json train_data_2.json test_data_2.json test_data_2_input
python3 transfer_train.py
python3 transfer_test.py

CUDA_VISIBLE_DEVICES=1 python3 run_swag_no_trainer.py --train_file train_data.json --validation_file test_data.json --per_device_train_batch_size 1 --per_device_eval_batch_size 1 --gradient_accumulation_steps 2 --learning_rate 3e-5 --num_train_epochs 1 --max_seq_length 512 --model_name_or_path bert-base-chinese

python3 transfer_train_2.py 
python3 transfer_test_2.py

CUDA_VISIBLE_DEVICES=1 python3 run_qa_no_trainer.py --train_file train_data_2.json --validation_file test_data_2.json --per_device_train_batch_size 4 --per_device_eval_batch_size 1 --learning_rate 1e-5 --num_train_epochs 5 --max_seq_length 512 --seed 10902027 --model_name_or_path shibing624/text2vec-base-chinese --output_dir p2_model_1_10902027

CUDA_VISIBLE_DEVICES=3 python3 run_qa_no_trainer.py --train_file train_data_2.json --validation_file test_data_2.json --per_device_train_batch_size 4 --per_device_eval_batch_size 1 --learning_rate 1e-5 --num_train_epochs 5 --max_seq_length 512 --seed 592081 --model_name_or_path shibing624/text2vec-base-chinese --output_dir p2_model_1_592081

python3 txt_to_csv.py





