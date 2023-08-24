library(ggplot2)
library(dplyr)

# Your Group9_UP_MF data
group9_up_mf_data <- data.frame(
  Enrichment_FDR = c(
    0.03581173503, 0.03581173503, 0.03581173503,
    0.03581173503, 0.03581173503, 0.03581173503,
    0.03581173503, 0.03581173503, 0.03581173503,
    0.04141916955
  ),
  nGenes = c(
    4, 2, 6, 2, 4, 3, 8, 2, 3, 12
  ),
  Pathway_Genes = c(
    74, 8, 208, 4, 79, 35, 359, 6, 27, 794
  ),
  Fold_Enrichment = c(
    10.10013292, 46.71311475, 5.389974779, 93.42622951,
    9.460884001, 16.01592506, 4.163843098, 62.28415301,
    20.76138434, 2.823966635
  ),
  Pathway = c(
    "Protein kinase inhibitor activity",
    "NMDA glutamate receptor activity",
    "Calmodulin binding", "Inositol-1,4,5-trisphosphate 3-kinase activity",
    "Kinase inhibitor activity",
    "Protein serine/threonine kinase inhibitor activity",
    "Ubiquitin-like protein ligase binding",
    "Inositol trisphosphate kinase activity",
    "Phosphatidylinositol-3,5-bisphosphate binding",
    "Kinase binding"
  )
)

# Create the lollipop chart with gene count labels next to circular points
group9_up_mf_lollipop <- ggplot(group9_up_mf_data, aes(x = reorder(Pathway, -log10(Enrichment_FDR)), y = -log10(Enrichment_FDR), color = Fold_Enrichment)) +
  geom_segment(aes(xend = reorder(Pathway, -log10(Enrichment_FDR)), yend = 0), color = "lightgrey") +
  geom_point(aes(label = paste("n =", nGenes), size = nGenes), shape = 16, color = "red") +
  scale_size_continuous(range = c(3, 6)) +
  scale_color_gradient(low = "blue", high = "red") +
  coord_flip() +
  labs(x = "Pathway", y = "Fold Enrichment", title = "Group9 UP MF") +
  theme_minimal() +
  theme(
    axis.text.y = element_text(hjust = 1),
    plot.background = element_rect(fill = "lightgrey"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  )

# Print the modified Group9 UP MF lollipop chart
print(group9_up_mf_lollipop)

# Save the modified Group9 UP MF lollipop chart
setwd("/home/sejyoti/Downloads/GO Analysis/GO Analysis/Group 9")
dev.new(width = 12, height = 8, bg = "white")
print(group9_up_mf_lollipop)
ggsave("Group9_UP_MF.png", width = 12, height = 5, dpi = 300, bg = "white")

