# genomic_analysis.py

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load genomic data
data = pd.read_csv('genomic_data.csv')

# Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)

# Apply t-SNE
tsne = TSNE(n_components=2, perplexity=30, n_iter=300)
tsne_result = tsne.fit_transform(data)

# Visualize results
plt.scatter(pca_result[:, 0], pca_result[:, 1], label='PCA')
plt.scatter(tsne_result[:, 0], tsne_result[:, 1], label='t-SNE')
plt.legend()
plt.show()