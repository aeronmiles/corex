from typing import Dict, List, Union
import numpy as np
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
    df.columns = pd.Index(cols)
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

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    if not isinstance(max_k, int) or max_k <= 0:
        raise ValueError("max_k must be a positive integer.")

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

    # Determine the elbow point algorithmically (optional)
    def find_elbow_point(wcss):
        deltas = np.diff(wcss)
        accelerations = np.diff(deltas)
        elbow_point = np.argwhere(accelerations > 0)[0, 0] + 2  # +2 due to double np.diff
        return elbow_point

    elbow_point = find_elbow_point(wcss)
    logger.info(f"Suggested optimal number of clusters based on elbow detection: {elbow_point}")

    # Allow visual check
    try:
        optimal_k = int(input("Enter the optimal number of clusters: "))
    except ValueError:
        logger.error("Invalid input. Using the suggested optimal number of clusters.")
        optimal_k = elbow_point

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

    return optimal_k, labels  # Return the optimal number of clusters and labels

  
def plot_columns(df: pd.DataFrame, columns: Union[List[str], str]):
  """
  Plots the specified columns from a DataFrame with a time-based index.

  Parameters:
  df (pd.DataFrame): DataFrame with a time-based index.
  columns (list): List of column names to plot.

  Returns:
  None
  """
  for c in df.columns:
    if c not in df.columns:
      raise ValueError(f"{c} not in the DataFrame")
  
  plt.figure(figsize=(14, 7))

  for column in columns:
      plt.plot(df.index, df[column], label=column)

  plt.xlabel('Time')
  plt.ylabel('Value')
  plt.title('Time Series Data')
  plt.legend()
  plt.grid(True)
  plt.show()

# matplotlib dark background decorator
def matplotlib_dark(func):
    def wrapper(*args, **kwargs):
        with plt.style.context('dark_background'):
            func(*args, **kwargs)

    return wrapper