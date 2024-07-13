import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]["instruction"]
        tokens = self.tokenizer.encode(text, return_tensors='pt', padding='max_length', truncation=True, max_length=128)
        return tokens

def train_model(train_data, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Create DataLoader
    train_dataset = CustomDataset(train_data, tokenizer)
    train_loader = DataLoader(train_dataset, batch_size=1, shuffle=False)

    # Define optimizer and training parameters
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    num_epochs = 3

    # Training loop
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    

    for epoch in range(num_epochs):
        model.train()
        for batch in train_loader:
            inputs = batch.to(device)

            optimizer.zero_grad()
            outputs = model(inputs, labels=inputs)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            torch.cuda.empty_cache()
            # Optionally, log the loss or perform validation during training

    # Save the trained model
    model.save_pretrained("model_v1")

# Load and preprocess your JSON data
with open('train.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    train_data = json_data["data"] if isinstance(json_data, dict) else json_data

num_subsets = 10
subset_size = len(train_data) // num_subsets

# Split the data into smaller subsets
subsets = [train_data[i*subset_size:(i+1)*subset_size] if i < num_subsets - 1 else train_data[i*subset_size:] for i in range(num_subsets)]

# Train the model on each subset
model_name = 'Taiwan-LLM-7B-v2.0-chat'
for i, subset in enumerate(subsets, 1):
    train_model(subset, model_name)
