# Data Science Mock Interview – Part 3  

**Interviewer (Antonio Cangiano, Skills Network Engineering Manager & AI Specialist at IBM):**  
Were there some challenges or things that you felt were hard to solve in your project?  

**Candidate (Cindy):**  
In terms of technical challenges, I didn’t really encounter much difficulty with coding because the project was at the level of what we’d already learned in class.  

The harder part was the **preliminary stage**:  
- Deciding what data was actually useful.  
- Figuring out what we could omit.  
- Handling issues like whether to drop variables or deal with correlated features.  

That was definitely the main challenge for me.  

---

**Antonio:**  
Okay. And did you use Python for this project?  

**Cindy:**  
I actually used **R**.  

**Antonio:**  
Any specific libraries you can remember?  

**Cindy:**  
Yes—we used **tidyverse** for data cleaning and **ggplot** for visualization. Both were very helpful for exploring variables and cleaning the dataset.  

---

**Antonio:**  
Good. So Cindy, are you familiar with SQL?  

**Cindy:**  
Yes, I’ve taken a class on SQL.  

**Antonio:**  
Great. Could you tell me the difference between an **INNER JOIN** and an **OUTER JOIN**?  

**Cindy:**  
Sure. An **INNER JOIN** takes the intersection of two datasets—it only returns rows with matching values in both. So, if there are no missing values, you won’t see gaps.  

An **OUTER JOIN** takes the union of two datasets. This can result in missing values if one dataset doesn’t contain certain values present in the other.  

---

**Antonio:**  
Good. As a follow-up: let’s say I’m returning a lot of results, maybe 300 rows, but I only want the first 10. What clause could I use?  

**Cindy:**  
Well, in some systems you might use something like `head` or `max` to limit results. But most often, the keyword is **LIMIT**. For example:  
```sql
SELECT * FROM table_name
LIMIT 10;