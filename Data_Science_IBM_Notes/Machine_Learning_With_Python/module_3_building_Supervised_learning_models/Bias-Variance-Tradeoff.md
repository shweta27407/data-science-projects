# Bias, Variance, and Ensemble Models

## 🎯 Learning Objectives
By the end of this summary, you’ll be able to:
- Analyze the **impact of bias and variance** on model accuracy and precision.
- Explain the **bias-variance tradeoff** in model complexity.
- Evaluate methods to **mitigate bias and variance**.
- Understand the principles and outcomes of **bagging and boosting** ensemble techniques.

---

## 🎯 Bias vs. Variance

Imagine four dartboards:

- **Bias**: How close the darts are to the bullseye. Low bias = more accurate predictions.
- **Variance**: How spread out the darts are. Low variance = more consistent predictions.

High accuracy (low bias) + high precision (low variance) = Best performance.

---

## 📈 Prediction Bias

- **Definition**: The average difference between model predictions and the actual values.
- Example:
  - A model’s blue line prediction has a bias of `0.22` (closer to the truth).
  - A shifted red line model has a higher bias of `4.22`.

---

   ![bias - variance](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Machine_Learning_With_Python/images/bias-variance.png)

Data_Science_IBM_Notes/Machine_Learning_With_Python/images/bias-variance.png

## 📉 Prediction Variance

- **Definition**: How much predictions vary when the model is trained on different subsets of data.
- High variance models are overly sensitive to the training data → **overfitting**.
- Low variance models generalize better on unseen data → **good generalization**.
- Example: Several fitted curves differ at edges due to high prediction variance.

---

## ⚖️ The Bias-Variance Tradeoff

As **model complexity increases**:
- **Bias decreases** (better fit to training data).
- **Variance increases** (sensitive to data noise).

### Underfitting
- Simple models
- High bias, low variance

### Overfitting
- Complex models
- Low bias, high variance

There's a **sweet spot** where the model is complex enough to reduce bias but not too complex to increase variance excessively.

   ![modelcomplexity](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Machine_Learning_With_Python/images/bias-variance.png)

Data_Science_IBM_Notes/Machine_Learning_With_Python/images/bias-variance.png

---

## 🧠 Weak vs. Strong Learners

- **Weak Learner**:
  - Slightly better than random guessing
  - High bias, low variance
  - Often underfits

- **Strong Learner**:
  - Low bias, high variance
  - Often overfits

---

## 🤝 Ensemble Methods

### 🧺 Bagging (Bootstrap Aggregating)
- Train **multiple models** on **random bootstrapped data subsets** in **parallel**.
- Final prediction = **average** of all predictions.
- Reduces **variance** significantly.
- Example: **Random Forest** uses shallow decision trees in a bagging approach.

### 🚀 Boosting
- Train **sequential models**, each correcting the errors of the previous one.
- Focuses on **reducing bias** by reweighting misclassified samples.
- Final model = **weighted sum** of weak learners.
- Common algorithms: **Gradient Boosting**, **XGBoost**, **AdaBoost**

---

## 🧪 Bagging vs. Boosting Summary

| Aspect            | Bagging                         | Boosting                          |
|-------------------|----------------------------------|------------------------------------|
| Training          | Parallel                        | Sequential                         |
| Goal              | Reduce Variance                 | Reduce Bias                        |
| Base Learners     | High variance, low bias         | Low variance, high bias            |
| Examples          | Random Forest                   | AdaBoost, XGBoost, Gradient Boosting |

---

## ✅ Summary
- **Bias** = how accurate a model is.
- **Variance** = how consistent the model is across data subsets.
- **Bias-Variance Tradeoff** = balancing underfitting and overfitting through model complexity.
- **Bagging** lowers variance (helps avoid overfitting).
- **Boosting** lowers bias (helps fix underfitting).