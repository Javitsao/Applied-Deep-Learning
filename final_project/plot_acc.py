import matplotlib.pyplot as plt
#01, 2
data1 = {
    64: 0.81767,
    128: 0.865,
    256: 0.84667,
    512: 0.90333,
    1024: 0.77433
}
#01, 2 train loss
# data1 = {
#     64: 0.4331,
#     128: 0.4376,
#     256: 0.4639,
#     512: 0.2877,
#     1024: 0.5165
# }

#0, 12
data2 = {
    64: 0.836,
    128: 0.814,
    256: 0.80033,
    512: 0.75867,
    1024: 0.79533
}
#0, 12 train loss
# data2 = {
#     64: 0.4052,
#     128: 0.44409,
#     256: 0.4696,
#     512: 0.4129,
#     1024: 0.4101
# }

#0, 1, 2
data3 = {
    64: 0.74267,
    128: 0.751,
    256: 0.77467,
    512: 0.78933,
    1024: 0.781
}
#0, 1, 2 train loss
# data2 = {
#     64: 0.6422,
#     128: 0.632,
#     256: 0.6111,
#     512: 0.5975,
#     1024: 0.78851
# }



# Extract x and y values for data1
x_values1 = list(data1.keys())
y_values1 = list(data1.values())

# Extract x and y values for data2
x_values2 = list(data2.keys())
y_values2 = list(data2.values())

# Extract x and y values for data3
x_values3 = list(data3.keys())
y_values3 = list(data3.values())

# Plotting the lines for data1 and data2
plt.figure(figsize=(8, 6))
plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='b', label='Case 1')
plt.plot(x_values2, y_values2, marker='o', linestyle='-', color='r', label='Case 2')
plt.plot(x_values3, y_values3, marker='o', linestyle='-', color='g', label='Case 3')
plt.xlabel('Max Sequence Length')
plt.ylabel('Ratio')
plt.title('Accuracy vs Max Sequence Length')
plt.xticks([64, 128, 256, 512, 1024])
#plt.ylim(0.5, 0.85)
plt.legend()
plt.grid(True)
plt.show()
