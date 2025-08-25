# 📈 Regression Metrics and Evaluation Techniques

Welcome to the lesson on **Regression Metrics and Evaluation Techniques**.  
After completing this video, you will be able to:

- Explain the need to evaluate regression models  
- Define model error  
- Understand and compare key regression metrics: MAE, MSE, RMSE, and R²  
- Use visualizations to interpret model performance  

---

## 🎯 Why Evaluate Regression Models?

Regression models aim to **predict continuous numerical values** (e.g., exam grades, prices).  
Since models aren't perfect, it's crucial to assess how well predictions align with actual values.

### Example:
If you're predicting **final exam grades** based on midterm scores:
- Blue dots = actual grades  
- Trend line = regression predictions  
- Distance between the line and dots = **prediction errors**

---

## 📏 Core Regression Metrics

### 1. **Mean Absolute Error (MAE)**
- Average of **absolute differences** between predicted and actual values  
- Formula: `MAE = (1/n) * Σ |y_i - ŷ_i|`

### 2. **Mean Squared Error (MSE)**
- Average of **squared differences**  
- Penalizes larger errors more than MAE  
- Formula: `MSE = (1/n) * Σ (y_i - ŷ_i)²`

### 3. **Root Mean Squared Error (RMSE)**
- Square root of MSE  
- Easier to interpret due to **same units** as target variable  
- Formula: `RMSE = sqrt(MSE)`

### 4. **R-squared (R²)**
- Proportion of variance in the target variable explained by the model  
- Also known as the **coefficient of determination**  
- Range: `0 (bad) → 1 (perfect)`  
- Formula:  