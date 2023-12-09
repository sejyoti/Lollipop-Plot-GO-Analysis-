# importing the modules
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dictionary for the data
data_dict = {
    "Sample": ["RuL1", "RuL2", "RuL3", "RuL4", "RuL5", "RuL6"],
    "RuL1": [0, 0.4735, 0.41959, 0.43652, 0.45983, 0.40434],
    "RuL2": [0.4735, 0, 0.38167, 0.36471, 0.39355, 0.44046],
    "RuL3": [0.41959, 0.38167, 0, 0.36486, 0.38667, 0.42262],
    "RuL4": [0.43652, 0.36471, 0.36486, 0, 0.35459, 0.40227],
    "RuL5": [0.45983, 0.39355, 0.38667, 0.35459, 0, 0.39665],
    "RuL6": [0.40434, 0.44046, 0.42262, 0.40227, 0.39665, 0]
}

# generating 2-D 10x10 matrix of random numbers
# from 1 to 100
data = np.random.randint(low=1,
                         high=100,
                         size=(10, 10))

# setting the parameter values
cmap = "tab20"

# plotting the heatmap
hm = sns.heatmap(data=data,
                cmap=cmap)

# displaying the plotted heatmap
plt.show()
