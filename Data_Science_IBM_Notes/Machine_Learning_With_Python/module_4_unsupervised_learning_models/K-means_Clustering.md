# 📊 K-Means Clustering

Welcome to this module on **K-Means Clustering**.

After completing this, you will be able to:

- ✅ Describe what K-Means Clustering is  
- ✅ Explain how the K-Means algorithm works  
- ✅ Understand how to determine the best value for **K**

---

## 🔹 What is K-Means?

- K-Means is an **iterative, centroid-based clustering algorithm**.
- It **partitions a dataset into k non-overlapping clusters** based on **similarity (distance from centroid)**.
- The goal is to:
  - Minimize **within-cluster variance** (tight, compact clusters)
  - Maximize **between-cluster dissimilarity** (distinct clusters)

---

## 📍 How It Works

1. **Initialization**  
   - Choose the number of clusters **k**
   - Randomly initialize **k centroids** (from data points or feature space)

2. **Assignment Step**  
   - Compute distances between each point and each centroid
   - Assign each point to the **nearest centroid**

3. **Update Step**  
   - For each cluster, update the centroid as the **mean of the assigned points**

4. **Repeat**  
   - Continue assigning and updating until:
     - Centroids stabilize **(convergence)**
     - Or max iterations are reached

---

## 📉 Performance & Limitations

- ✅ **Performs well** when:
  - Clusters are **convex**
  - Cluster sizes are roughly **equal**
  - No significant **outliers or noise**
  
- ❌ **Performs poorly** when:
  - Clusters are **imbalanced** (e.g., 200 vs 10 points)
  - Clusters are **non-convex**
  - Presence of **noise or outliers**

---

## 📊 Visual Example (Experiment)

- Starts with two clusters and random centroids.
- With each iteration:
  - Centroids **move closer** to optimal positions.
  - After convergence, cluster assignments stabilize.
- Even though **a few points may be misclassified**, the algorithm effectively separates clusters.

---

## 🔄 K and the Shape of Data

- A **higher k** → more, smaller, detailed clusters  
- A **lower k** → fewer, larger, less detailed clusters

- When **k ≠ true number of classes**, misgrouping can occur:
  - Example: With 3 blobs but k=2, K-Means merges two blobs into one.

---

## 📈 Standard Deviation and Clustering

- As **standard deviation increases**:
  - Blobs **overlap more**
  - Clustering becomes **less accurate**
  - Centroids **move closer together**

- For high std dev (e.g., 15):
  - K-Means struggles, as clusters are no longer distinguishable

---

## ❓ Choosing the Right K

When true **K is unknown**, try:

1. **Silhouette Score**  
   - Measures **cohesion** (similarity within a cluster) vs **separation** (difference from other clusters)

2. **Elbow Method**  
   - Plot the **K-Means objective function** (within-cluster sum of squares) for various K values  
   - Look for the "elbow point" where improvement drops off

3. **Davies-Bouldin Index**  
   - Evaluates **similarity between clusters**; lower scores are better

---

## 🧠 Key Takeaways

- **K-Means** partitions data into clusters by minimizing distances from centroids.
- It assumes:
  - Clusters are **convex**
  - Clusters are **balanced in size**
- Sensitive to **initial centroid placement**, **outliers**, and **standard deviation**
- Use heuristic methods to **choose optimal K**

---