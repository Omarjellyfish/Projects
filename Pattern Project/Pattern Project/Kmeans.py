import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("Data.csv")



x = data.drop(columns=['Exercise Recommendation Plan', 'Gender', 'BMIcase'])
y = data["Exercise Recommendation Plan"]


lda = LinearDiscriminantAnalysis(n_components=2)
X_train_lda = lda.fit_transform(x, y)


kmeans = KMeans(n_clusters=7) #clusters for each excersie plan
kmeans.fit(X_train_lda)

cluster_labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize=(10, 6))
plt.scatter(
    X_train_lda[:500, 0],
    X_train_lda[:500, 1],
    c=cluster_labels[:500],
    cmap="viridis",
    marker="o",
    label="Data Points",
)
plt.scatter(
    centroids[:, 0], centroids[:, 1], c="red", marker="X", s=200, label="Centroids"
)

plt.title("Clustered Data with K-Means and LDA")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.legend(loc="best")
plt.grid(True)
plt.colorbar(label="Class")

plt.show()

