## prepare the file (download.sh)

copy two data files context.json and test.json to the current path

```bash
cp $1 $2 .
```

use transfer_test.py convert test.json to test_data.json in order to fit the format of phase 1

```bash
python3 transfer_test.py
```

## phase 1

use p1_model_1 to predict the selected paragraph and save the result in test_data_2_input

```bash
python3 run_swag_no_trainer.py --train_file train_predict_1.json --validation_file test_data.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1  --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path p1_model_1
```

use transfer_test_2.py to transfer the test.json file to test_data_2.json in order to fit the format of phase 2

```bash
python3 transfer_test_2.py
```

## phase 2

use p2_model_1_649 to predict and save the result in data_649.csv  
use p2_model_1_9487 to predict and save the result in data_9487.csv  
use p2_model_1_34595 to predict and save the result in data_34595.csv  
use p2_model_1_592081 to predict and save the result in data_592081.csv  
use p2_model_1_10902027 to predict and save the result in data_10902027.csv  
use p2_model_1_59487666 to predict and save the result in data_59487666.csv

```bash
models=("p2_model_1_649" "p2_model_1_9487" "p2_model_1_34595" "p2_model_1_592081" "p2_model_1_10902027" "p2_model_1_59487666")
for model in "${models[@]}"; do
    python3 run_qa_no_trainer.py --train_file train_predict_2.json --validation_file test_data_2.json --per_device_train_batch_size 4 --per_device_eval_batch_size 1 --learning_rate 1e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path "$model"
    python3 txt_to_csv.py 
    mv "data.csv" "data_$(echo $model | cut -d'_' -f4).csv"
done
```

## blending

blend (select the most common answer of each id) six results (csv files) and save the final result in prediction.csv in the given path

```bash
python3 blend_csv.py
python3 save_pred_to_path.py $3
```
