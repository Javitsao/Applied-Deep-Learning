import matplotlib.pyplot as plt

# Provided data points
data_points_1 = {
    0.2: 0.6523,
    0.4: 0.4893,
    0.6: 0.419,
    0.8: 0.374,
    1: 0.327
}
# Provided data points
data_points_2 = {
    0.2: 0.645,
    0.4: 0.554,
    0.6: 0.5605,
    0.8: 0.5025,
    1: 0.5059
}
# Provided data points
data_points_3 = {
    0.2: 1.0908,
    0.4: 0.9094,
    0.6: 0.7079,
    0.8: 0.6624,
    1: 0.5833
}

# Extracting x and y values from the data points
x_values_1 = list(data_points_1.keys())
y_values_1 = list(data_points_1.values())
# Extracting x and y values from the data points
x_values_2 = list(data_points_2.keys())
y_values_2 = list(data_points_2.values())
# Extracting x and y values from the data points
x_values_3 = list(data_points_3.keys())
y_values_3 = list(data_points_3.values())

# Plotting the loss curve
plt.figure(figsize=(8, 6))
plt.plot(x_values_1, y_values_1, marker='o', color='b', linestyle='-', label='Case 1')
plt.plot(x_values_2, y_values_2, marker='o', color='r', linestyle='-', label='Case 2')
plt.plot(x_values_3, y_values_3, marker='o', color='g', linestyle='-', label='Case 3')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss vs Epoch')
plt.legend()
plt.grid(True)
plt.show()
