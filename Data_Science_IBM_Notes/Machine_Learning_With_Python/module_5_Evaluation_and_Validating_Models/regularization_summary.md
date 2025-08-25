
# Regularization in Linear Regression

## Introduction

Regularization is a regression technique used to **prevent overfitting**. It constrains the model during training, discouraging it from fitting too closely to the training data by **suppressing the size of its coefficients**.

---

## Regularized Cost Function

With regularization, a **modified cost function** is used:

$$
J(\theta) = \text{MSE} + \lambda \cdot \Omega(\theta)
$$

Where:
- \( J(\theta) \): Regularized cost function  
- \( \lambda \): Regularization strength (hyperparameter)  
- \( \Omega(\theta) \): Penalty term (depends on the type of regularization)  

---

## Linear Regression

In standard linear regression, the model predicts:

$$
\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n
$$

The loss function minimized is usually the **Mean Squared Error (MSE)**:

$$
\text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (y^{(i)} - \hat{y}^{(i)})^2
$$

---

## Ridge Regression (L2 Penalty)

Ridge regression adds an **L2 penalty** (sum of squared coefficients):

$$
J(\theta) = \text{MSE} + \lambda \sum_{j=1}^{n} \theta_j^2
$$

This shrinks the coefficients but does not eliminate them.

---

## Lasso Regression (L1 Penalty)

Lasso regression adds an **L1 penalty** (sum of absolute values of coefficients):

$$
J(\theta) = \text{MSE} + \lambda \sum_{j=1}^{n} |\theta_j|
$$

This can shrink some coefficients to **exactly zero**, making it useful for **feature selection**.

---

## Sparse vs Non-Sparse Coefficients

- **Sparse Coefficients**: Only a few features are important.
- **Lasso** performs very well in identifying and selecting only the useful features (sparse models).

---

## Signal-to-Noise Ratio (SNR)

- **High SNR**: All three regression models (Linear, Ridge, Lasso) perform well.
- **Low SNR**: 
  - Linear regression overfits and assigns large incorrect coefficients.
  - Ridge improves slightly.
  - **Lasso** still performs best due to feature selection.

---

## Visual Comparison Summary

- Lasso predicts **zero coefficients** better than Linear and Ridge.
- Ridge performs better than Linear in **noisy conditions** but not as good as Lasso in selecting features.
- **Lasso has the lowest Mean Squared Error (MSE)** in most scenarios.

---

## Conclusion

- Regularization helps prevent overfitting by penalizing large coefficients.
- **Ridge** (L2) shrinks coefficients but keeps all features.
- **Lasso** (L1) can eliminate unimportant features by setting coefficients to zero.
- Use **Lasso** when feature selection is important, and **Ridge** when you want all features but need stability.
