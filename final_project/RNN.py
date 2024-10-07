import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the data
train_data = pd.read_csv("train_fake_less_old.csv")
test_data = pd.read_csv("test_fake_less_old.csv")

# Select specific columns
columns_to_use = ['title', 'author', 'text', 'label']
train_data = train_data[columns_to_use]
test_data = test_data[columns_to_use]

# Split data into features and target
X = train_data.drop(columns=['label'])  # Features
y = train_data['label']  # Target

# Encode categorical target labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.01, random_state=42)

# Handle NaN values without dropping all rows
X_train = X_train.fillna(0)  # Filling NaN values with 0
X_val = X_val.fillna(0)  # Filling NaN values with 0
test_data = test_data.fillna(0)  # Filling NaN values in test data with 0

# Convert all columns to numeric if they are not already
X_train = X_train.apply(pd.to_numeric, errors='coerce')
X_val = X_val.apply(pd.to_numeric, errors='coerce')
test_data = test_data.apply(pd.to_numeric, errors='coerce')

# Instead of dropping rows with NaN values, let's drop columns with all NaN values
X_train = X_train.dropna(axis=1, how='all')
X_val = X_val[X_train.columns]  # Update validation data with the same columns as X_train
test_data = test_data[X_train.columns]  # Update test data with the same columns as X_train

# Now, check the shapes
print(f"X_train shape: {X_train.shape}")
print(f"X_val shape: {X_val.shape}")
print(f"test_data shape: {test_data.shape}")

# Create a neural network model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(label_encoder.classes_), activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with the updated data
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# Evaluate the model on the training set
train_loss, train_accuracy = model.evaluate(X_train, y_train)
print(f"Ein (Training Loss): {train_loss}")
print(f"Train Accuracy: {train_accuracy}")

# Evaluate the model on the validation set
val_loss, val_accuracy = model.evaluate(X_val, y_val)
print(f"Eval (Validation Loss): {val_loss}")
print(f"Validation Accuracy: {val_accuracy}")

# Make predictions on the test set
test_predictions = model.predict(test_data)

# Get the predicted classes by finding the index of the maximum probability in each prediction
predicted_classes = test_predictions.argmax(axis=1)

# Decode predicted labels
predicted_labels = label_encoder.inverse_transform(predicted_classes)

# Calculate Eout (Test Accuracy)
test_y = pd.read_csv("test_news3.csv")['label']
test_y = label_encoder.transform(test_y)

test_loss, test_accuracy = model.evaluate(test_data, test_y)
print(f"Eout (Test Loss): {test_loss}")
print(f"Test Accuracy: {test_accuracy}")
