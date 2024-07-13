#! /usr/bin/env bash
#python3 transfer_train.py
cp $1 $2 .
python3 transfer_test.py

python3 run_swag_no_trainer.py --train_file train_predict_1.json --validation_file test_data.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1  --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path p1_model_1

python3 transfer_test_2.py

python3 run_qa_no_trainer.py --train_file train_predict_2.json --validation_file test_data_2.json --per_device_train_batch_size 4 --per_device_eval_batch_size 1 --learning_rate 1e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path p2_model_1_9487

python3 txt_to_csv.py $3
