English fake news detection
===
# same dataset for training and testing(english)
## prepare dataset
split dataset to train and test data with ratio 8:2
```bash
python drop_fake_split.py train.csv --split-ratio 0.8 id text label
```
train data: train_fake_less_old.csv \
test data: test_fake_less_old.csv

## train the model
(using accuracy)
```bash
python run_classification.py --model_name_or_path bert-base-uncased --train_file train_fake_less_old.csv --validation_file test_fake_less_old.csv --metric_name accuracy --text_column_name "title,text" --text_column_delimiter "," --label_column_name label --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 1 --learning_rate 2e-5 --num_train_epochs 4 --output_dir old_fake_less/
```

(using f1 score)
```bash
python run_classification.py --model_name_or_path bert-base-uncased --train_file train_fake_less_old.csv --validation_file test_fake_less_old.csv --metric_name accuracy --text_column_name "title,text" --text_column_delimiter "," --label_column_name label --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 1 --learning_rate 2e-5 --num_train_epochs 4 --output_dir old_fake_less/
```

# different dataset for training and testing
## prepare dataset
choose all true news and 10% fake data for both dataset
```bash
python fake_less.py WELFake_Dataset.csv train_fake_less.csv id text label
```
```bash
python fake_less.py train.csv test_fake_less.csv id text label
```
train data: train_fake_less.csv \
test data: test_fake_less.csv

## train the model
(using accuracy)
```bash
python run_classification.py --model_name_or_path bert-base-uncased --train_file train_fake_less.csv --validation_file test_fake_less.csv --metric_name accuracy --text_column_name "text" --text_column_delimiter "," --label_column_name label --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 2e-5 --num_train_epochs 1 --output_dir new_train_old_test_fake_less/
```

(using f1 score)
```bash
python run_classification.py --model_name_or_path bert-base-uncased --train_file train_fake_less.csv --validation_file test_fake_less.csv --metric_name f1 --text_column_name "text" --text_column_delimiter "," --label_column_name label --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 2e-5 --num_train_epochs 1 --output_dir new_train_old_test_fake_less_f1/
```

# RNN
## prepare dataset
split dataset to train and test data with ratio 8:2
```bash
python drop_fake_split.py train.csv --split-ratio 0.8 id title author text label
```
train data: train_fake_less_old.csv \
test data: test_fake_less_old.csv

```bash
python RNN.py
```

Japanese GPT2 fake news detection
===
## prepare dataset
split the dataset into 10000 news and 3000 news
```bash
python split.py
```
preparing for three cases 
1. label 0, 1 regarded as true and 2 regarded as fake 
2. label 0 regarded as true and 1, 2 regarded as fake 
3. original label 0, 1, 2
```bash
python label_012.py
```
run run_classification.py for all three cases \
case 1(label 0, 1 regarded as true and 2 regarded as fake)
```bash
python run_classification.py --model_name_or_path ku-nlp/bart-base-japanese --train_file news_tm_10000.csv --validation_file news_tm_3000.csv --metric_name accuracy --text_column_name "context" --text_column_delimiter "," --label_column_name isfake --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 2e-5 --num_train_epochs 1 --output_dir news_tm/
```
case 2(label 0 regarded as true and 1, 2 regarded as fake)
```bash
python run_classification.py --model_name_or_path ku-nlp/bart-base-japanese --train_file news_fm_10000.csv --validation_file news_fm_3000.csv --metric_name accuracy --text_column_name "context" --text_column_delimiter "," --label_column_name isfake --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 2e-5 --num_train_epochs 1 --output_dir news_fm/
```
case 3(original label 0, 1, 2)
```bash
python run_classification.py --model_name_or_path ku-nlp/bart-base-japanese --train_file news_10000.csv --validation_file news_3000.csv --metric_name accuracy --text_column_name "context" --text_column_delimiter "," --label_column_name isfake --do_train --do_eval --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 2e-5 --num_train_epochs 1 --output_dir news/
```