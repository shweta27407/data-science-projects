# 📍 DBSCAN and HDBSCAN Clustering

Welcome to this module on **DBSCAN** and **HDBSCAN**.

After this, you’ll be able to:

- ✅ Describe DBSCAN and explain how it works
- ✅ Describe HDBSCAN and understand its improvements over DBSCAN

---

## 🔹 What is DBSCAN?

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** is a **density-based clustering algorithm** that:

- Forms clusters based on **density of data points**
- Can find **clusters of arbitrary shape, size, or density**
- Distinguishes between:
  - **Core points**: Dense points (with at least *n* neighbors within radius *ε*)
  - **Border points**: Near core points but not dense enough themselves
  - **Noise points**: Isolated and not in any cluster

### ✅ Key Advantages

- Works well when **number of clusters is unknown**
- Handles **noise and outliers**
- Not iterative – clusters are formed in a **single pass**

### ❌ Limitations

- Requires setting two parameters: **ε (radius)** and **minPts (min neighbors)**
- Not adaptive to **varying densities**

---

## 🧪 DBSCAN Simulation Summary

- Starts with all points as noise
- Clusters are grown from **core points**
- Points near core points are added as **border**
- Remaining points are labeled as **noise**
- Example: Used on **Scikit-learn’s half-moons dataset** – successfully separates curved clusters and detects noise

---

## 🔸 What is HDBSCAN?

**HDBSCAN (Hierarchical DBSCAN)** is an advanced version of DBSCAN with **no fixed radius requirement**:

- Combines **density-based clustering** and **agglomerative clustering**
- Builds a **hierarchical tree** of clusters by lowering the density threshold
- Extracts **stable clusters** by measuring **cluster persistence** across varying radii

### ✅ Benefits over DBSCAN

- **No need to manually set ε**
- **Adapts to local density variations**
- **More robust to noise and outliers**
- Finds **better-defined and more coherent clusters**

---

## 🗺️ Real-World Example

- Dataset: **Lat/Long of Canadian museums**
- DBSCAN with fixed radius created **fewer clusters**, missed detail in dense regions
- HDBSCAN identified:
  - More **distinct clusters**
  - **Curved structures** and **dense areas** more effectively
  - **Higher resolution** in dense eastern regions

---

## 🧠 Key Takeaways

- **DBSCAN** forms clusters based on fixed density and distance thresholds.
- **HDBSCAN** builds on DBSCAN by:
  - Removing the need for a fixed radius
  - Adapting to different densities
  - Measuring **cluster stability**
- Both are powerful for **clustering real-world, noisy, and irregular datasets**.
