## prepare the file

use transfer_to_json.py convert input.jsonl to intput.json in order to fit the format

```bash
python3 transfer_to_json.py $1 input.json
```
## train
```bash
python train_sum.py \
  --model_name_or_path google/mt5-small \
  --train_file data/train.json \
  --text_column maintext\
  --summary_column title\
  --output_dir /tmp2/b10902027/ADL/hw2/model_v4 \
  --per_device_train_batch_size 8 \
  --num_train_epochs 5 \
  --learning_rate 5e-4 \
  --overwrite_output_dir \
  --predict_with_generate \
  --max_source_length 1024\
  --max_target_length 128\
  --do_train
```

## predict

use model_v4 to predict save the result in submission.jsonl

```bash
python summarization.py --model_name_or_path model_v4 --train_file train_few.json  --validation_file input.json --text_column maintext --summary_column title --output_dir model_v4  --per_device_eval_batch_size 8  --num_train_epochs 1  --learning_rate 5e-4  --num_beams 4 --max_source_length 1024 --max_target_length 128 
```

## output


```bash
mv submission.jsonl $2
```