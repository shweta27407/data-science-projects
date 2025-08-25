# Cross-Validation and Advanced Model Validation Techniques

## 🎯 Learning Objectives

After watching this video, you will be able to:

- Define **model validation**
- Explain what **data snooping** is and how to avoid it
- Discuss key **strategies for model validation**

---

## 📘 What is Model Validation?

Model validation is the process of testing how well your model performs on **unseen data**. It helps:

- Prevent **overfitting**
- Ensure **generalization**
- Tune **hyperparameters** safely

---

## 🧪 Basic Train-Test Split

- **Training Set**: Used to train the model
- **Test Set**: Used to evaluate model performance on new data

> ⚠️ If you tune hyperparameters using test data, you're "leaking" information — this is called **data snooping**.

---

## 🚫 What is Data Snooping?

**Data snooping** (a form of **data leakage**) occurs when:

- The test set influences model configuration or hyperparameters
- Results in **overfitting** to the test data
- Makes the model **unreliable** on new, unseen data

---

## ✅ Proper Validation Strategy

Use **three subsets**:

1. **Training set** – to train the model
2. **Validation set** – to tune the model/hyperparameters
3. **Test set** – for final unbiased performance evaluation

---

## 🔁 K-Fold Cross-Validation

A robust method to improve model generalization:

1. Split training data into **K equal-sized folds**
2. For each fold:
   - Train on **K-1** folds
   - Validate on the **remaining** fold
3. Repeat for all folds
4. Average performance scores to pick the best hyperparameters

### ✅ Benefits:
- All data points are used for both training and validation
- Reduces bias from single validation set
- Helps in reliable model evaluation

---

## 📊 Stratified Cross-Validation (Classification)

- Ensures each fold has the **same class distribution**
- Prevents bias in imbalanced datasets

---

## 📉 Skewed Targets in Regression

- Many regression models assume normally distributed targets
- If the target is **skewed**, transform it using:
  - **Logarithmic transform**
  - **Box-Cox transform**

> These help stabilize variance and improve model fit

---

## 🧠 Key Takeaways

- Always separate **training**, **validation**, and **test** data
- Never evaluate or tune on test data before model finalization
- Use **K-fold cross-validation** for robust hyperparameter tuning
- Apply **stratified sampling** for imbalanced classification problems
- For regression, **transform skewed targets** to improve learning

---