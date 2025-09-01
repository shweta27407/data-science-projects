# Data Science Mock Interview – Part 1  

**Interviewer (Antonio Cangiano, Skills Network Engineering Manager & AI Specialist at IBM):**  
Nice to meet you, Cindy. My name is Antonio Cangiano, and I'm a manager here at IBM. If you were to be hired for this position, I’d be your manager. Why don’t we start with you introducing yourself and telling me how you got started with data science?  

**Candidate (Cindy):**  
Yeah, for sure. My name is Cindy, and I just finished my third year at the University of Toronto studying Data Science. I didn’t have any background in the field at first, but two summers ago I did an internship where I developed a classification regression tree. That experience introduced me to machine learning and data science.  

I also worked on data visualization during that internship, which was really exciting. It motivated me to combine statistics and computer science to improve user experiences for products and services.  

---

**Antonio:**  
Great. So, R and Python are two of the most popular languages in data science. Why would you use one over the other?  

**Cindy:**  
I think R is stronger in statistical modeling. For example, it’s great for simulations like Monte Carlo or calculating standard error with jackknife estimators. R also has powerful visualization packages like **ggplot2** and **Plotly**, which make it easy to create readable and high-quality graphs.  

Python, on the other hand, is more general-purpose. It’s especially strong in machine learning and deep learning. Libraries like **scikit-learn, TensorFlow, and PyTorch** are designed primarily for Python, and they make it easy to experiment with models by changing just a few parameters.  

---

**Antonio:**  
Good. You mentioned some plots earlier. Do you know what a box plot is?  

**Cindy:**  
Yes. A box plot is a visualization that shows data distribution using quartiles. The main part is the box, which displays the interquartile range. It highlights the median (50th percentile) and often shows potential outliers as individual points above or below the whiskers. For example, if we plotted product prices, the box plot would display the spread and highlight unusual values.  

---

**Antonio:**  
Nice. Can you explain the difference between supervised and unsupervised learning?  

**Cindy:**  
Sure. The main difference is that **supervised learning uses labeled data**, while **unsupervised learning uses unlabeled data**.  

- **Supervised example:** A regression tree predicting house prices based on features.  
- **Unsupervised example:** Clustering customers with **k-means** to discover groups when no labels are provided.  

---

**Antonio:**  
Let’s do a scenario. Suppose you have a model with 90% accuracy on the training set but only 50% accuracy on the test set. What’s the problem?  

**Cindy:**  
That sounds like **overfitting**. The model is learning patterns too specific to the training data and not generalizing. Possible causes could include:  
- Using too much of the data for training, leaving too little for testing.  
- Wrong hyperparameters.  

Possible solutions:  
- Adjust the train/test split.  
- Use a **validation set** for tuning hyperparameters.  
- Apply **regularization** or reduce model complexity.  

---

**Antonio:**  
Good. And what are the dangers of underfitting?  

**Cindy:**  
Underfitting means the model hasn’t learned enough from the training data. It performs poorly on both the training set and the test set. Essentially, the model is too simple to capture the data’s patterns, so it won’t generalize well either.  

---

**Antonio:**  
Alright, let’s talk metrics. Suppose you’re working with an **imbalanced dataset for classification** and **false negatives don’t matter**. What metric would you use?  

**Cindy:**  
In that case, I’d focus on **precision**, because we’d want to know how many of the predicted positives are truly positive.  

Other related metrics could include:  
- **Recall (sensitivity):** Proportion of actual positives identified correctly.  
- **F1 score:** Balances precision and recall if both matter.  

But since false negatives don’t matter in this scenario, **precision** would be the most relevant metric.  

**Antonio:**  
Exactly—precision is the right focus here. But it’s good that you mentioned recall and F1 as alternatives.  

---

➡️ *This concludes Part 1 of Cindy’s mock interview. The conversation continues in **Data Science Mock Interview, Part 2.***