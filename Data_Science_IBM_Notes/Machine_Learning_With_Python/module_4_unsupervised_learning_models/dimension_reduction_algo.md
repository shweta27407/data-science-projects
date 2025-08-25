# 📉 Dimension Reduction Algorithms

Welcome to the video on **Dimension Reduction Algorithms**.  
After watching this video, you will be able to:

- Explain what dimensionality reduction algorithms are.
- Describe key types: **PCA**, **t-SNE**, and **UMAP**.
- Understand how these algorithms simplify high-dimensional datasets without losing important information.

---

## 🚀 What Is Dimensionality Reduction?

Dimensionality reduction refers to techniques that reduce the number of features (dimensions) in a dataset while **preserving important patterns**.  
It is useful for:

- Simplifying analysis and visualization
- Reducing computational cost
- Improving model performance on high-dimensional data

---

## 🔷 PCA – Principal Component Analysis

- **Type**: Linear algorithm
- **Goal**: Reduce dimensionality while retaining variance
- **How it works**:
  - Transforms original features into new, uncorrelated variables called **principal components**
  - These components are **orthogonal** and ranked by how much variance they explain
  - The first few components usually contain most of the information

✅ **Best for**: Linearly correlated datasets  
📉 **Reduces noise**, simplifies data, and improves interpretability

---

## 🔶 t-SNE – T-Distributed Stochastic Neighbor Embedding

- **Type**: Non-linear algorithm
- **Goal**: Map high-dimensional data to 2D or 3D for **visualization**
- **How it works**:
  - Preserves **local structure** (similar points remain close)
  - Less focus on distant relationships
  - Measures proximity using pairwise distances

⚠️ **Drawbacks**:
- Doesn't scale well
- Sensitive to hyperparameters
- Mainly used for **visual clustering**

✅ **Best for**: Text, image data, or datasets with hidden clusters

---

## 🔷 UMAP – Uniform Manifold Approximation and Projection

- **Type**: Non-linear algorithm
- **Goal**: Preserve both **local and global structures** of data
- **How it works**:
  - Assumes data lies on a **manifold**
  - Builds a high-dimensional graph and optimizes it to a low-dimensional space
  - Finds the best representation of relationships between data points

✅ **Benefits over t-SNE**:
- **Better scalability**
- **Faster computation**
- Often provides **more meaningful clustering results**

---

## 🧪 Visual Example (MakeBlobs 3D Simulation)

- The original dataset: 3D points generated with `make_blobs()` from Scikit-learn.
- Two clusters have slight overlap, others are well-separated.

### 📊 Comparison of Algorithms:

| Algorithm | Result |
|----------|--------|
| **PCA** | Effectively separated the linearly distributed blobs. |
| **t-SNE** | Found 4 distinct clusters, some mixing in overlapping regions. |
| **UMAP** | Slight overlap in yellow/green/purple clusters, but handled global structure well. Performed slightly better than t-SNE overall. |

---

## 🧠 Summary

- **Dimensionality Reduction** simplifies data without major information loss.
- Three popular techniques:
  - **PCA**: Linear, preserves variance, removes noise.
  - **t-SNE**: Non-linear, great for visualization of local clusters.
  - **UMAP**: Non-linear, balances local and global structure, scalable and fast.
- These methods are essential for data exploration, visualization, and preprocessing in machine learning pipelines.