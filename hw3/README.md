## prepare the file

modify the hyper-parameters in qlora.yml


## train
train in the directory "axolotl" (https://github.com/OpenAccess-AI-Collective/axolotl/tree/main) mentioned by TA
```bash
python -m axolotl.cli.train qlora.yml
```

## evaluate the score using the model I trained
using ppl.py to check the score

```bash
python ppl.py --base_model_path Taiwan-LLM-7B-v2.0-chat --peft_path adapter_checkpoint --test_data_path public_test.json
```

## predict
generate predictions.json

```bash
python predict.py --base_model_path $1 --peft_path $2 --test_data_path $3 --output_path $4
```