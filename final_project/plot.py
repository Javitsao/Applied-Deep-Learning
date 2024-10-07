import matplotlib.pyplot as plt

data_set1 = [
    {'loss': 0.1505, 'learning_rate': 1.802839116719243e-05, 'epoch': 0.1},
    {'loss': 0.0648, 'learning_rate': 1.605678233438486e-05, 'epoch': 0.2},
    {'loss': 0.0439, 'learning_rate': 1.4085173501577287e-05, 'epoch': 0.3},
    {'loss': 0.0458, 'learning_rate': 1.2113564668769717e-05, 'epoch': 0.39},
    {'loss': 0.0371, 'learning_rate': 1.0141955835962144e-05, 'epoch': 0.49},
    {'loss': 0.0355, 'learning_rate': 8.170347003154575e-06, 'epoch': 0.59},
    {'loss': 0.0291, 'learning_rate': 6.198738170347004e-06, 'epoch': 0.69},
    {'loss': 0.0379, 'learning_rate': 4.227129337539433e-06, 'epoch': 0.79},
    {'loss': 0.0225, 'learning_rate': 2.2555205047318616e-06, 'epoch': 0.89},
    {'loss': 0.0288, 'learning_rate': 2.8391167192429027e-07, 'epoch': 0.99}
]

data_set2 = [
    {'loss': 0.3534, 'learning_rate': 1.7812294902647124e-05, 'epoch': 0.11},
{'loss': 0.1012, 'learning_rate': 1.562458980529425e-05, 'epoch': 0.22},
{'loss': 0.0325, 'learning_rate': 1.3436884707941372e-05, 'epoch': 0.33},
{'loss': 0.0188, 'learning_rate': 1.1249179610588494e-05, 'epoch': 0.44},
{'loss': 0.0241, 'learning_rate': 9.061474513235616e-06, 'epoch': 0.55},
{'loss': 0.0127, 'learning_rate': 6.8737694158827395e-06, 'epoch': 0.66},
{'loss': 0.0147, 'learning_rate': 4.686064318529863e-06, 'epoch': 0.77},
{'loss': 0.0017, 'learning_rate': 2.4983592211769857e-06, 'epoch': 0.88},
{'loss': 0.0229, 'learning_rate': 3.1065412382410855e-07, 'epoch': 0.98}
]

epochs_set1 = [entry['epoch'] for entry in data_set1 if 'epoch' in entry]
train_loss_set1 = [entry['loss'] for entry in data_set1 if 'loss' in entry]

epochs_set2 = [entry['epoch'] for entry in data_set2 if 'epoch' in entry]
train_loss_set2 = [entry['loss'] for entry in data_set2 if 'loss' in entry]

plt.plot(epochs_set1, train_loss_set1, marker='o', label='different dataset')
plt.plot(epochs_set2, train_loss_set2, marker='o', label='same dataset')

plt.title('Training Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Training Loss')
plt.legend()
plt.grid(True)
plt.show()
