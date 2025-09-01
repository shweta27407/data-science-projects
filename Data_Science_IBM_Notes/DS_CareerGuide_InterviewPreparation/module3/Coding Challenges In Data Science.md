# Coding Challenges in Data Science  

## What You’ll Learn  
After this lesson, you will be able to:  
- Describe what a **coding challenge** or **take-home quiz** is.  
- Summarize the **process** of completing a coding challenge.  
- Recognize the **typical format** of a coding challenge problem.  

---

## What is a Coding Challenge?  
- A coding challenge is a **problem you solve at home** on your own time, then submit for review.  
- Its purpose is to **showcase your coding and problem-solving skills** in a concrete way.  
- Usually occurs **after initial screening**, though sometimes it’s the first step.  
- You may receive:  
  - A **file or dataset**.  
  - A **URL** with an online coding environment.  

---

## Types of Coding Assessments  
- **Take-home quiz**:  
  - Often short (about **40 minutes**).  
  - Usually online, with no option to pause or exit.  

- **Coding challenge**:  
  - More time allowed (**hours to several days**).  
  - Scope depends on **seniority level**:  
    - **Entry-level**: exploratory data analysis (EDA), summary statistics, charts, simple ML tasks.  
    - **Mid/Senior-level**: regression/classification models, time-series forecasting, large datasets requiring cleaning and preprocessing.  

---

## Typical Tasks in a Data Science Coding Challenge  
- Understand **variable roles** (categorical vs. numerical).  
- Calculate **descriptive and exploratory statistics**.  
- Identify suitable **machine learning models** for the task.  
- Perform **EDA and visualization**.  
- Split data into **training and testing sets**.  
- Apply **encoding for categorical features** (e.g., one-hot encoding).  
- Train the chosen model and explain **why** you selected it.  
- Report results clearly, often with **charts or metrics**.  

---

## Directed vs. Open-Ended Challenges  
- **Directed challenges**:  
  - Instructions clearly specify what steps to take (e.g., preprocessing, modeling).  
  - Key to success: **Follow all directions exactly**.  

- **Open-ended challenges** (common for senior roles):  
  - Problem is stated, but **steps are not provided**.  
  - Candidate must:  
    - Define assumptions.  
    - Justify chosen methods.  
    - Explain reasoning and approach.  

---

## Deliverables and Deadlines  
- **Instructions and dataset** provided by the company.  
- Dataset format varies (clean CSV vs. large, messy datasets).  
- **Firm deadlines**:  
  - Short quizzes: ~40 minutes.  
  - Take-home projects: **24–72 hours**.  

- Some companies may require signing an **NDA** (non-disclosure agreement) to protect problem statements and ownership of solutions.  

---

## Sample Coding Challenge Example  
**Task:** Build a regressor to recommend crew size for potential ship buyers.  

**Steps included in instructions:**  
1. Read data into a DataFrame and display all columns.  
2. Calculate descriptive statistics for variables (`NOX`, `age`, `tax`) – count, mean, median, standard deviation.  
3. Check for **outliers** in these variables.  
4. Select important features to predict **median sale values** of homes.  
5. Drop irrelevant columns and explain why.  
6. Apply **one-hot encoding** for categorical features.  
7. Split data: **60% training, 40% testing**.  
8. Choose a machine learning model and justify the choice.  
9. Train the model.  
10. Calculate **Pearson correlation coefficient** for training and test sets.  
11. Answer typical follow-up questions:  
    - How can accuracy be improved?  
    - How to tune hyperparameters?  
    - What is the role of the regularization parameter?  
    - Does the model have bias or variance problems?  
12. Plot **regularization parameter vs. Pearson correlation coefficient**.  

---

## Key Takeaways  
- Coding challenges are a **critical step** in the interview process.  
- Instructions may be **clear or open-ended**, depending on role seniority.  
- Deadlines vary: from **short quizzes** (minutes) to **multi-day projects**.  
- A challenge is an opportunity to **demonstrate your technical ability, reasoning, and clarity of communication**.  
- Success requires:  
  - **Following instructions carefully**.  
  - **Documenting assumptions and choices**.  
  - **Producing clean, readable, and reproducible code**.  