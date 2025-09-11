## Causal ML in Predicting Treatment Outcomes Research


Imagine you’re testing a new blood pressure medication.
	•	ML (Regular) would predict: “People who take the medicine tend to have lower blood pressure.”
	•	Causal ML answers: “Does taking the medicine cause a person’s blood pressure to drop?”


Differencde ML vs Causal ML 

✅ Traditional ML says:

“People who take the medicine usually have lower BP, so it predicts you’ll have lower BP if you take it.”

BUT… maybe people who take the medicine also exercise, eat healthy, or are younger. The model doesn’t know why the BP is lower — just that there’s a pattern.

“If YOU took the medicine, how much would your blood pressure change compared to not taking it?”

So it builds two worlds:
	•	In one, you take the medicine.
	•	In the other, you don’t.


Go to the diagram one, Explain it

Diag 1 explanation :

▶️ Left: Traditional ML
	•	The model looks at past data where patients were not treated (marked with red crosses ❌).
	•	It learns patterns like: “Patients like this tend to have low survival.”
	•	But it doesn’t know what would have happened if they had been treated.
	•	So, it makes predictions only based on observed data, and Plan A is just an extension of current trends.

✅ It tells how patients who were not treated typically perform.

⸻

▶️ Right: Causal ML
	•	Causal ML builds two scenarios for each patient:
	•	One where the patient is treated (blue path).
	•	One where the patient is not treated (red path).
	•	It estimates the treatment effect:
“If this person had taken treatment, how would survival improve compared to not taking it?”

💡 This is the individualized treatment effect (ITE) — and it helps decide between Plan A vs. Plan B.


-----------

▶️ Traditional ML Table (left side)

🔹 Data section:
	•	It uses columns like:
	•	Patient ID
	•	Covariates (like age, sex)
	•	Treatment (0 = not treated, 1 = treated)
	•	Patient outcome (e.g., survival score)

So, you only observe one outcome per person — either after treatment or without.

🔹 Task section:
	•	You try to predict the missing outcome based on current treatment and features.

🧠 But here’s the limitation:
	•	You don’t know what would have happened if the treatment were different.


▶️ Causal ML Table (right side)

🔹 Data section:
	•	You try to model both:
	•	Outcome if not treated
	•	Outcome if treated

You only observe one, but the model tries to estimate both for each person.

🔹 Task section:
	•	Goal: Predict both potential outcomes and subtract to get the treatment effect:
\text{Treatment effect} = \text{Outcome if treated} - \text{Outcome if not treated}

This is counterfactual reasoning — asking: “What if this person had made a different choice?”


**Traditional ML predicts what is likely to happen, based on what was observed.**
**Causal ML predicts what would have happened under a different scenario, helping to make better treatment decisions.**

-----

✅ What Does This Graph Show?
	•	X-axis: Age of the patient (from children to elderly).
	•	Y-axis: Treatment Effect (how helpful the treatment is).
	•	The curved line: How the treatment effect changes with patient age

✅ Why This Graph is Important for Causal ML?

Traditional ML might say:

“This drug helps people on average.”

But Causal ML can say:

“This drug helps these specific people a lot, less so for others.”


-------------

🔄 STEP-BY-STEP EXPLANATION

🔴 1. Define a Research Question & Collect Data
	•	Example: Does Drug A reduce cancer recurrence more effectively for younger patients?
	•	You gather data from clinical trials or electronic health records.

⸻

⚙️ PROBLEM SETUP

🟡 2. Formulate the Causal Structure
	•	Create a causal diagram (called a causal graph or DAG).
	•	Think about what causes what (e.g., age → treatment decision → health outcome).

🟡 3. Select the Causal Quantity of Interest
	•	Example: Individualized Treatment Effect (ITE) — what would happen to a specific patient with vs. without treatment.

🟡 4. Assess Assumptions for Identifiability
	•	Make sure your question can actually be answered using your data.
	•	Example: No hidden confounders, enough variation in treatments, etc.

⸻

🤖 CAUSAL ML STAGE

🔵 5. Choose and Fit Causal ML Model
	•	Choose models like DR-Learner, Causal Forests, etc. (this paper uses DR-Learner).
	•	Train the model on your medical data.

🔵 6. Evaluate the Causal ML Model
	•	Use metrics to check: Is the model estimating treatment effects correctly?
	•	Compare with Randomized Controlled Trials (RCTs) if possible.

🔵 7. Perform Robustness Checks
	•	Change assumptions slightly and see if results still hold.
	•	Helps test if your findings are reliable and generalizable.

⸻

✅ FINAL STEP

🔷 8. Interpret the Results
	•	Explain what the model is telling you.
	•	Example: This drug is 30% more effective for people over age 50.
	•	Use this for personalized treatment decisions in the clinic.

-------------------

Diagram 3 

🔹 (a) Causal Graph – Understanding Relationships
	•	This is a simple causal diagram (also called a Directed Acyclic Graph, or DAG).
	•	It shows:
	•	Covariates (e.g., gender, age, history)
	•	Treatment (e.g., drug like Metformin)
	•	Outcome (e.g., blood glucose level)

🔁 Key Idea:
	•	You assume a causal path:
Covariates → Treatment → Outcome
	•	Covariates also influence Outcome directly.

This setup helps you reason about how treatment actually causes an outcome.

⸻

🔹 (b) Types of Causal Questions – The Estimand Grid

This grid helps decide what type of treatment effect you want to estimate:

X-axis = How personal the estimate is:
	•	Left (Averaged effects): Just want to know the average effect on a population.
	•	Middle (Effect heterogeneity): Want to know how effects change across different groups.
	•	Right (Individualized effects): Want to predict for each person individually.

Y-axis = Type of treatment:
	•	Binary treatments (e.g., yes/no):
	•	Did they get the drug or not?
	•	Continuous treatments (e.g., dosage amount):
	•	How much radiation did they receive?






Model Agnostic Box :


1. Plug-in learners
	•	S-Learner:
	•	You use one ML model.
	•	The model takes in both the patient’s features and the treatment type (like 0 or 1).
	•	It predicts the outcome (e.g., survival rate).
	•	You use it to compute what would happen with and without treatment.
2. T-Learner:
	•	You train two separate ML models:
	•	One model for treated patients.
	•	One for untreated (control) patients.
	•	Then you subtract the predictions:
➡️ Effect = Treated outcome - Untreated outcome

3. DR - Learner
It combines two types of information to make the estimation more accurate and reliable:
	1.	Propensity model:
👉 Estimates how likely someone is to receive the treatment (like a probability score).
➤ Example: Based on age, symptoms, etc., how likely is this patient to get a specific drug?
	2.	Outcome model:
👉 Predicts the expected outcome with and without treatment.

⸻

💡 Why is it called “Doubly Robust”?

Because even if one of the two models is wrong, the DR-Learner can still give good results.
✅ This makes it more robust (reliable) compared to other methods.

⸻



🔹 What is a pseudo-outcome?

A pseudo-outcome is a smart estimate of what we can’t actually observe (like what would’ve happened if someone had gotten a different treatment).

Factual : 
What actually happened to a patient. ✅
Counterfactual:
What would have happened if they had received the other treatment ❓


LAst Conclusion:

📌 Key Points in the Conclusion:
1.	Causal ML works well for estimating personalized treatment effects
	•	Especially helpful when randomized trials are hard or impossible.
	•	Can support personalized medicine by predicting how each individual might respond to a treatment.
	2.	They highlight the success of one method: DR-Learner
	•	Among the models tested, DR-Learner showed strong potential in clinical settings.
	•	It performed well on real-world cancer datasets (DCLA and NSCLC).
	•	It produced treatment effect estimates that closely matched results from randomized controlled trials (RCTs).

	•	Instead, they say it showed promise, but careful real-world validation is still needed.
4.	RCTs are still the gold standard — but Causal ML can complement them
	•	Causal ML could help identify which patients benefit the most (or least) from a treatment.
	•	Especially useful for vulnerable groups, rare diseases, or situations where running a trial is unethical.
5.	They encourage using Causal ML in practice, but with caution
	•	Emphasize the need for uncertainty estimation, clear guidelines, and collaboration with clinicians.