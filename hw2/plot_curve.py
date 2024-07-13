import matplotlib.pyplot as plt

# Data for different time points
time_points = [0, 600, 1200, 1800, 2400]

# ROUGE-1 f values
rouge_1_f = [0.05939489464225601, 0.1958470009269481, 0.22709377167725078, 0.2416567733163725, 0.23748093591794067]

# ROUGE-2 f values
rouge_2_f = [0.016306337410703683, 0.06981066863493067, 0.08442821862753393, 0.09332345888185146, 0.09408852803454719]

# ROUGE-L f values
rouge_l_f = [0.0552409542125922, 0.18048705425240846, 0.20675033626903502, 0.21904804846097048, 0.21562581375969808]

# Plot the curves
plt.figure(figsize=(10, 6))
plt.plot(time_points, rouge_1_f, marker='o', label='ROUGE-1')
plt.plot(time_points, rouge_2_f, marker='s', label='ROUGE-2')
plt.plot(time_points, rouge_l_f, marker='^', label='ROUGE-L')

# Add labels and title
plt.xlabel('Training Steps')
plt.ylabel('f1 Score')
plt.title('Learning Curves')
plt.legend()

# Show the plot
plt.grid()
plt.show()
