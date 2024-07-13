import matplotlib.pyplot as plt

# Points
points = [(32, 3.908618321895599),
          (64, 3.699026307582855),
          (96, 3.6276773433685303),
          (128, 3.522921464920044),
          (159, 3.5053930649757383)]

# Extract x and y coordinates from points
x = [point[0] for point in points]
y = [point[1] for point in points]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Learning Curve')
plt.xlabel('Checkpoint')
plt.ylabel('Mean perplexity')
plt.grid(True)
plt.show()
