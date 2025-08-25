# Classification Metrics and Evaluation Techniques

Welcome to this video on **Classification Metrics and Evaluation Techniques**.  
After watching this video, you will be able to:

- Define the **train-test-split** technique  
- Describe the **confusion matrix**, **accuracy**, **precision**, **recall**, and **F1 score** metrics  
- Illustrate examples of each concept

---

## 🎯 What is Supervised Learning Evaluation?

Supervised learning evaluation determines how well a machine learning model can predict outcomes on **unseen data**. This process:

- Compares model predictions to ground truth labels  
- Is critical during **both training and testing phases**  
- Helps assess **model generalization**  

---

## 🔀 Train-Test-Split Technique

- **Training Set**: ~70–80% of data used to train the model  
- **Test Set**: Remaining data used to evaluate performance  
- Ensures the model is not overfitting and can generalize well to new data

---

## 📊 Common Classification Metrics

### ✅ Accuracy
- **Definition**: Ratio of correctly predicted instances to the total instances  
- Example: If 70% of predictions are correct, accuracy = 70%

### 🧮 Confusion Matrix
|               | Predicted Positive | Predicted Negative |
|---------------|--------------------|--------------------|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

- **TP**: Correctly predicted positive class  
- **TN**: Correctly predicted negative class  
- **FP**: Incorrectly predicted positive class  
- **FN**: Incorrectly predicted negative class

### 🎯 Precision
- **Definition**: `Precision = TP / (TP + FP)`  
- Example use case: **Movie recommendation systems**  
- **High precision** → Less cost from false positives

### 📈 Recall
- **Definition**: `Recall = TP / (TP + FN)`  
- Example use case: **Medical diagnoses**  
- **High recall** → Avoid missing actual positives (important in healthcare)

### ⚖️ F1 Score
- **Definition**: Harmonic mean of precision and recall  
- `F1 Score = 2 * (Precision * Recall) / (Precision + Recall)`  
- Use when **precision and recall are equally important**  

---

## 🌸 Iris Flower Classification Example

- **KNN classifier** applied to the **Iris dataset**  
- Confusion matrix visualized using heatmap  
- Diagonal of the confusion matrix → Correct predictions  
- **Weighted average** of metrics considers the support (number of instances per class)

---

## 🧠 Summary

In this video, you learned:

- Supervised learning evaluation is critical for measuring model performance on unseen data  
- The **train-test-split** technique partitions data into training and testing sets  
- **Accuracy**, **precision**, **recall**, **confusion matrix**, and **F1 score** are key evaluation metrics  
- Use case examples help understand when each metric is most important