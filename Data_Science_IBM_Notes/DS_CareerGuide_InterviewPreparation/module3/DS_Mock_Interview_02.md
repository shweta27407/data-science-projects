# Data Science Mock Interview – Part 2  

**Interviewer (Antonio Cangiano, Skills Network Engineering Manager & AI Specialist at IBM):**  
So, ridge regression and linear regression are two very popular types of regression. Can you tell me the difference between the two?  

**Candidate (Cindy):**  
Yes. Ridge regression includes a **penalty term**, which is the sum of the squares of the coefficients in the linear function. Linear regression, on the other hand, does not include this penalty.  

As a result, ridge regression is less vulnerable to random noise in the dataset and helps prevent overfitting. Linear regression does not have this capability.  

---

**Antonio:**  
Good. What is the implication for **cost on training data**?  

**Cindy:**  
Hmm, I’m not entirely sure.  

**Antonio:**  
That’s okay—we can move on.  

**Cindy (thinking aloud):**  
Well, my educated guess would be that the cost for linear regression might be lower, since it doesn’t consider the penalty term. Ridge regression, because of the penalty, may require more computation before convergence. So linear regression could potentially be faster in training.  

---

**Antonio:**  
Alright. Imagine you have a model that always outputs the number 4—exactly 4 every time. What would the variance be?  

**Cindy:**  
Variance represents how much the output depends on the training set. In this case, since the model always outputs 4, the variance would be **zero**, because the predictions never change.  

---

**Antonio:**  
Okay, now suppose you have a **linear system of three equations and two unknowns**. How would you approximately solve the system?  

**Cindy:**  
A system with three equations and two unknowns is **overdetermined**, so there might not be an exact solution. To approximate, we can use the **least squares method**.  

If the system is written as *Ax = b*, then least squares finds the solution for *x* that minimizes the difference between *Ax* and *b*. This gives us an approximate solution even when the system is inconsistent.  

---

**Antonio:**  
Good. Now, can you tell me about a project that you’re very proud of?  

**Cindy:**  
Yes. This past semester, I worked with three other students on a project where we were given the vague question: *“Are our devices racist?”*  

We had to determine whether the company’s devices discriminated against certain populations based on test scores and usage data. It was a challenging project because the problem statement was broad—we had to decide:  
- Which variables to focus on.  
- What models to use.  
- How to structure the analysis as a group.  

It was very rewarding because, as an individual, I might have approached it in one way, but hearing different perspectives from my teammates opened my mind to more effective methods.  

---

**Antonio:**  
And what was your **individual contribution** in this project?  

**Cindy:**  
I was mainly responsible for **data cleaning** and **feature engineering**.  

- The data wasn’t given in a convenient format like CSV—we had to extract it via an API and then convert it into a usable form.  
- Once cleaned, I engineered features that would be useful for my teammates to feed into the models.  

This work ensured that the modeling team had high-quality, well-structured data to analyze.  

---

➡️ *This concludes Part 2 of Cindy’s mock interview. The conversation continues in **Data Science Mock Interview, Part 3.***