import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a DataFrame with the provided values
data = pd.DataFrame({
    'group': ['Upregulated', 'Upregulated', 'Downregulated', 'Downregulated', 'Downregulated'],
    'FDR': [3.50e-02, 3.50e-02, 7.32e-05, 1.32e-04, 1.32e-04],
    'nGenes': [3, 6, 7, 7, 7],
    'PathwaySize': [20, 138, 102, 126, 131],
    'FoldEnriched': [21.5210526315789, 6.23798627002288, 13.0519835841313, 10.5658914728682, 10.1626131723771],
    'Pathway': ['Steroid biosynthesis', 'Fluid shear stress and atherosclerosis', 'Progesterone-mediated oocyte maturation', 'Cell cycle', 'Oocyte meiosis']
})

# Set up the plot using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(-np.log10(data['FDR']), data['Pathway'], s=data['nGenes'] * 10, c=data['group'].map({'Upregulated': 'red', 'Downregulated': 'blue'}), marker='o', alpha=0.7)

# Customize plot aesthetics
ax.set_xlabel('-log₁₀(FDR)')
ax.set_ylabel('Pathway')
ax.set_title('KEGG Pathway Enrichment\nUpregulated and Downregulated Pathways')
legend = ax.legend(handles=scatter.legend_elements()[0], title='Group', loc='upper left')
legend.get_title().set_fontsize(10)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Add text annotations for nGenes and FoldEnriched
for idx, row in data.iterrows():
    ax.text(-np.log10(row['FDR']) - 0.2, idx, f'nGenes: {row["nGenes"]}', verticalalignment='center', fontsize=10)
    ax.text(-np.log10(row['FDR']) - 0.2, idx + 0.25, f'FoldEnriched: {row["FoldEnriched"]:.2f}', verticalalignment='center', fontsize=10)

# Annotate color meanings
ax.text(0.95, 0.05, 'Red: Upregulated\nBlue: Downregulated', transform=ax.transAxes, fontsize=10, ha='right')

plt.tight_layout()
plt.show()
