import matplotlib.pyplot as plt

# Your loss data
loss_values = [
    5.9845, 4.1975, 1.6588, 2.6923, 1.3439, 1.3010, 1.9429, 1.1633, 0.8789, 0.5329,
    0.6044, 1.9406, 0.3239, 1.3532, 0.6317, 0.2204, 0.6231, 0.7880, 0.9640, 3.3500,
    0.4356, 0.4654, 2.5928, 0.2424, 1.2374, 0.6126, 0.9042, 0.5579, 1.2894, 0.4941,
    0.8017, 0.1306, 1.0221, 0.6604, 1.3481, 1.5840, 0.6055, 0.7300, 0.6438, 1.4894,
    1.0603, 1.0888, 0.8790, 0.2143, 2.6064, 0.3686, 0.1274, 0.8368, 0.1194, 0.3959,
    0.2709, 1.8396, 0.4311, 0.6958, 0.2488, 0.6511, 0.5347, 0.0531, 0.7297, 0.0825,
    0.3294, 0.3543, 0.9863, 0.4210, 0.0962, 0.1473, 0.0355, 2.2197, 0.9001, 1.9690
]

# Create a list of step numbers (assuming 100 steps per row)
step_numbers = [i * 100 for i in range(len(loss_values))]

# Plot the loss curve
plt.figure(figsize=(10, 5))
plt.plot(step_numbers, loss_values, marker='o', linestyle='-')
plt.title("Loss Curve")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.grid(True)
plt.show()
