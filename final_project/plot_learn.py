import matplotlib.pyplot as plt

# Provided data points
data_points_1 = {
    0.2: 0.65567,
    0.4: 0.84633,
    0.6: 0.85767,
    0.8: 0.87667,
    1: 0.90333
}
# Provided data points
data_points_2 = {
    0.2: 0.72633,
    0.4: 0.766,
    0.6: 0.80833,
    0.8: 0.82333,
    1: 0.836
}
# Provided data points
data_points_3 = {
    0.2: 0.39267,
    0.4: 0.514,
    0.6: 0.60967,
    0.8: 0.66167,
    1: 0.78933
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
plt.ylabel('accuracy')
plt.title('Learning curve')
plt.legend()
plt.grid(True)
plt.show()
