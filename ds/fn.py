from typing import Dict, List, Union
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from corex.logging import logger


def to_df(
    data: Union[List, Dict],
    time_unit: str,
    index: str,
    cols: List[str],
    numeric_cols: List[str],
    time_cols: List[str],
) -> pd.DataFrame:
    """Converts a list or dict to a pandas DataFrame."""
    df = pd.DataFrame(data)
    df.columns = cols
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
    for col in time_cols:
        df[col] = pd.to_datetime(df[col], unit=time_unit)
    df.set_index(index, inplace=True)
    return df


def optimal_clusters(data, max_k):
    """
    Determine the optimal number of clusters for K-means clustering
    using the Elbow Method.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the time series data.
    max_k (int): Maximum number of clusters to test.

    Returns:
    int: Optimal number of clusters.
    """

    # Normalize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Calculate WCSS for different numbers of clusters
    wcss = []
    for i in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
        kmeans.fit(scaled_data)
        wcss.append(kmeans.inertia_)

    # Plot the Elbow graph
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_k + 1), wcss, marker="o", linestyle="--")
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.show()

    # Determine the elbow point
    # This can be done visually from the plot, or by using an algorithmic approach
    # Here we are choosing visually, but you can implement additional methods
    # to find the elbow point algorithmically if desired.

    logger.info("Check the plot to determine the elbow point.")

    # Choose an optimal k based on the Elbow Method visually
    optimal_k = int(input("Enter the optimal number of clusters: "))

    # Run K-means with the optimal number of clusters
    kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
    kmeans.fit(scaled_data)
    labels = kmeans.labels_

    # Dimensionality Reduction with PCA
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(scaled_data)

    # Visualization
    plt.figure(figsize=(10, 8))
    for i in range(optimal_k):
        plt.scatter(reduced_data[labels == i, 0], reduced_data[labels == i, 1], label=f'Cluster {i}')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('Time Series Data Clusters')
    plt.legend()
    plt.show()

    return None  # Returns None as the elbow point is determined visually
