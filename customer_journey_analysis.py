# customer_journey_analysis.py

import pandas as pd
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load customer journey data
data = pd.read_csv('Wholesale customer data.csv')

# Normalize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(data_scaled)

# Apply Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(data_scaled)

# Visualize clusters
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=dbscan_labels, label='DBSCAN')
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=hierarchical_labels, label='Hierarchical')
plt.legend()
plt.show()