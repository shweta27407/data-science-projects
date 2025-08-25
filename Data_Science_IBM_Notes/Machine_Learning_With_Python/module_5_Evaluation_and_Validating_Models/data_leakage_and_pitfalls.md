
# 📘 Data Leakage and Other Pitfalls

## 🎯 Learning Objectives

After watching this video, you will be able to:

- Define **data leakage** and explain how to **mitigate it**.
- Interpret **feature importance**.
- Identify and avoid **common modeling pitfalls**.

---

## 💡 What is Data Leakage?

Data leakage occurs when a model’s training data includes information that would **not be available** in real-world prediction scenarios.

### Example:

You train a model to predict house prices using historical features like square footage and a **leaked feature**:  
> Average home prices over the entire dataset.

✅ Performance looks great on test data  
❌ But fails in production (due to **leaked future info**)

---

## 🔍 Data Snooping

**Data snooping** happens when:

- The training set contains **test information**.
- Future info is used to predict present outcomes.
- Feature engineering is done using the **entire dataset**.
- Pipelines are not **separated** between train/test sets.

🛠️ Prevention:
- Keep **train**, **validation**, and **test sets** fully isolated.

---

## ✅ Mitigating Data Leakage

- ❌ Avoid features based on full dataset statistics (like global averages).
- ✅ Ensure clear separation between **training**, **validation**, and **test**.
- ✅ Verify that **real-world predictions** will have access to the same features.
- ✅ Use **cross-validation** properly — no leakage between folds.

### ⏳ Special Case: Time-Series Data

- Use `TimeSeriesSplit` instead of random split.
- Ensure training set **precedes** the test set chronologically.

---

## 🧪 Example: Scikit-learn Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('knn', KNeighborsClassifier())
])

param_grid = {
    'pca__n_components': [2, 3, 5],
    'knn__n_neighbors': [3, 5, 7]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

✅ Grid search applies the pipeline **separately** to each fold.

---

## ⏱ Time-Series Cross-Validation

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=4)
grid_search = GridSearchCV(pipeline, param_grid, cv=tscv)
```

- Maintains **temporal order**.
- Each fold uses past data for training and future data for validation.

---

## 📊 Feature Importance Pitfalls

### ❗ Watch Out For:

- **Redundant features** dilute importance.
- Algorithms like linear regression are **sensitive to scale**.
- Importance indicates **correlation**, not causation.
- Models may **miss interactions** between features.

### 🧠 Example

- Two weak features may look useless individually.
- But their **product** may be highly predictive.
- Linear models miss this, but Random Forest may capture it.

---

## ⚠️ Modeling Pitfalls

- ❌ Using raw data without transformation or selection.
- ❌ Choosing wrong or misleading metrics.
- ❌ Ignoring **class imbalance** in classification problems.
- ❌ Blind trust in **AutoML tools** without understanding results.
- ❌ Building “what-if” simulations on **non-causal** features.

---

## 🧾 Summary

| Concept                 | Key Insight |
|------------------------|-------------|
| **Data Leakage**        | Training set includes future/unreal info. |
| **Data Snooping**       | Model sees data it shouldn’t. |
| **Prevention**          | Keep datasets isolated, avoid full-data features. |
| **Time-Series**         | Use `TimeSeriesSplit`. |
| **Feature Importance**  | Correlation ≠ Causation. |
| **Modeling Pitfalls**   | Avoid automation without understanding, misused metrics, and non-causal reasoning. |

---
