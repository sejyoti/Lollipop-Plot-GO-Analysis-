import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = np.array([
    [0, 0.4382, 0.43262, 0.44397, 0.42629, 0.44231],
    [0.4382, 0, 0.42429, 0.3913, 0.41538, 0.41449],
    [0.43262, 0.42429, 0, 0.42424, 0.41243, 0.44363],
    [0.44397, 0.3913, 0.42424, 0, 0.37853, 0.42606],
    [0.42629, 0.41538, 0.41243, 0.37853, 0, 0.43365],
    [0.44231, 0.41449, 0.44363, 0.42606, 0.43365, 0]
])

# Sample labels
sample_labels = ["RuL7", "RuL8", "RuL9", "RuL10", "RuL11", "RuL12"]

# Create a heatmap with the "viridis" colormap
plt.figure(figsize=(8, 6))
sns.set(font_scale=1)
sns.heatmap(data, cmap='viridis', annot=False, linewidths=0.5, vmin=0, vmax=1)

# Set x and y labels
plt.xticks(np.arange(len(sample_labels)) + 0.5, sample_labels)
plt.yticks(np.arange(len(sample_labels)) + 0.5, sample_labels)

plt.xlabel("Samples")
plt.ylabel("Samples")
plt.title("Beta Diversity Heatmap")

plt.show()
