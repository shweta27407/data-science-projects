# Data Sceince Methodologies

As a general science methodology, data methodology consists of the following 10 stages. 
1. Business understanding,
2. analytic approach,
3. data requirements,
4. data collection,
5. data understanding,
6. data preparation,
7. modeling,
8. evaluation,
9. deployment, and
10. feedback.


## Questions drive every stage of data science methodology. Data science methodology aims to answer the following 10 basic questions which align with the data methodology questions. 
  **These first two questions help you define the issue and determine what approach to use.**
1. what is the problem that you're trying to solve?
2. How can you use data to answer the question?
   ** You'll use the next four questions to help you get organized around the data. You'll ask,**
3. what data do you need to answer the question,
4. where's the data source from, and how will you receive the data?
5. Does the data you collect represent the problem to be solved and
6. what additional work is required to manipulate and work with the data?
   **Then you'll use these final four questions to validate your approach and final design for ongoing analysis.**
7. when you apply data visualizations, do you see answers that address the business problem?
8. Does the data model answer the initial business question or must you adjust the data?
9. Can you put the model into practice?
10. Can you get constructive feedback from the data and the stakeholder to answer the business question?

# Common Analytic Approach 

When choosing an analytic approach for a problem, the type of question you’re trying to answer greatly influences the methodology. Here are five common types of questions and corresponding analytic approaches:

## 1. Descriptive Questions: “What is the current status?”
Approach: Descriptive Analytics

### Question:  "What is the current status of our sales?"  

Techniques:

Data aggregation: Combining data from various sources into a unified view.

Data mining: Extracting useful information from large datasets.

Data visualization: Using visual tools to present data in an easily understandable format.

Examples:

Summarizing sales data

Creating dashboards

Generating reports


## 2. Diagnostic Questions: “Why did it happen?”
Approach: Diagnostic Analytics

### Question: "Why did our sales decline in the last quarter?"  

Techniques:

Drill-down: Exploring detailed data to find underlying causes.

Data discovery: Identifying patterns and relationships in data.

Correlation analysis: Assessing the relationship between different variables.

Examples:

Identifying root causes of sales decline

Analyzing customer complaints

Understanding failure points in a process


## 3. Predictive Questions: “What is likely to happen?”
Approach: Predictive Analytics

### Question: "What is our sales forecast for the next year?"  

Techniques:

Regression analysis: Predicting outcomes based on relationships between variables.

Time series forecasting: Predicting future values based on past trends.

Machine learning models: Using algorithms to predict future outcomes based on historical data.

Examples:

Forecasting sales

Predicting customer churn

Estimating future demand


## 4. Prescriptive Questions: “What should we do?”
Approach: Prescriptive Analytics

### Question: "What should we do to increase website traffic?"  

Techniques:

Optimization models: Finding the best solution from a set of alternatives.

Simulation: Modeling scenarios to predict outcomes.

Decision analysis: Evaluating and comparing different decisions.

Examples:

Recommending inventory levels

Optimizing marketing campaigns

Determining pricing strategies


## 5. Classification Questions: “Which category does this belong to?”
Approach: Classification (Supervised Learning)

### Question: "Which category does this data point belong to?"   

Techniques:

Logistic regression: Predicting the probability of a categorical outcome.

Decision trees: Splitting data into branches to classify it.

Support vector machines: Finding the best boundary to separate categories.

Neural networks: Using interconnected nodes to classify data.

Examples:

Email spam detection

Image classification

Disease diagnosis


Understanding these different types of questions and the corresponding analytic approaches can help you unlock your data's true potential.

# Modeling and Evaluation

Foundational methodology, a cyclical, iterative data science methodology developed by John Rollins, consists of 10 stages, starting with Business Understanding and ending with Feedback.

CRISP-DM, an open source data methodology, combines several data-related methodology stages into one stage and omits the Feedback stage resulting in a six-stage data methodology.

The primary goal of the Business Understanding stage is to understand the business problem and determine the data needed to answer the core business question. 

During the Analytic Approach stage, you can choose from descriptive diagnostic, predictive, and prescriptive analytic approaches and whether to use machine learning techniques.

During the Data Requirements stage, scientists identify the correct and necessary data content, formats, and sources needed for the specific analytical approach.

During the Data Collection stage, expert data scientists revise data requirements and make critical decisions regarding the quantity and quality of data. Data scientists apply descriptive statistics and visualization techniques to thoroughly assess the content, quality, and initial insights gained from the collected data, identify gaps, and determine if new data is needed, or if they should substitute existing data.

The Data Understanding stage encompasses all activities related to constructing the data set. This stage answers the question of whether the collected data represents the data needed to solve the business problem. Data scientists might use descriptive statistics, predictive statistics, or both.

Data scientists commonly apply Hurst, univariates, and statistics such as mean, median, minimum, maximum, standard deviation, pairwise correlation, and histograms. 

During the Data Preparation stage, data scientists must address missing or invalid values, remove duplicates, and validate that the data is properly formatted. Feature engineering and text analysis are key techniques data scientists apply to validate and analyze data during the Data Preparation stage.

The end goal of the Modeling stage is that the data model answers the business question. During the Modeling stage, data scientists use a training data set. Data scientists test multiple algorithms on the training set data to determine whether the variables are required and whether the data supports answering the business question. The outcome of those models is either descriptive or predictive. 

The Evaluation stage consists of two phases, the diagnostic measures phase, and the statistical significance phase. Data scientists and others assess the quality of the model and determine if the model answers the initial Business Understanding question or if the data model needs adjustment. 

During the Deployment stage, data scientists release the data model to a targeted group of stakeholders, including solution owners, marketing staff, application developers, and IT administration., 

During the Feedback stage, stakeholders and users evaluate the model and contribute feedback to assess the model’s performance. 

The data model’s value depends on its ability to iterate; that is, how successfully the data model incorporates user feedback.
