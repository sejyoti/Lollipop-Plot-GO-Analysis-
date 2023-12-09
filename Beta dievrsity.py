import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

# Sample data (replace with your actual data)
# Sample data (replace with your actual data)
data = {
    'C': [0, 0.057409, 0.055382],
    'T1': [0.057409, 0, 0.049808],
    'T2': [0.055382, 0.049808, 0]
}

df = pd.DataFrame(data, index=['C', 'T1', 'T2'])

# Calculate the linkage for clustering
linkage = hierarchy.linkage(df, method='average')

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, cmap='coolwarm', annot=True, fmt='.4f', linewidths=0.5, vmin=0, vmax=0.1)

# Add the dendrogram on the side
dendro = hierarchy.dendrogram(linkage, color_threshold=0, labels=df.index, orientation='left', no_plot=True)
ax = plt.gca()
ax.set_yticklabels(dendro['ivl'])

plt.title("Beta Diversity Heatmap")
plt.xlabel("Samples")
plt.ylabel("Samples")

plt.show()
