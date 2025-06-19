# Module 1

Each line in a dataset is a row, and commas separate the values.

To understand the data, you must analyze the attributes for each column of data.

Python libraries are collections of functions and methods that facilitate various functionalities without writing code from scratch and are categorized into Scientific Computing, Data Visualization, and Machine Learning Algorithms.

Many data science libraries are interconnected; for instance, Scikit-learn is built on top of NumPy, SciPy, and Matplotlib.

The data format and the file path are two key factors for reading data with Pandas.

The read_CSV method in Pandas can read files in CSV format into a Pandas DataFrame.

Pandas has unique data types like object, float, Int, and datetime.

Use the dtype method to check each column’s data type; misclassified data types might need manual correction.

Knowing the correct data types helps apply appropriate Python functions to specific columns.

Using Statistical Summary with describe() provides count, mean, standard deviation, min, max, and quartile ranges for numerical columns.

You can also use include='all' as an argument to get summaries for object-type columns.

The statistical summary helps identify potential issues like outliers needing further attention.

Using the info() Method gives an overview of the top and bottom 30 rows of the DataFrame, useful for quick visual inspection.

Some statistical metrics may return "NaN," indicating missing values, and the program can’t calculate statistics for that specific data type.

Python can connect to databases through specialized code, often written in Jupyter notebooks.

SQL Application Programming Interfaces (APIs) and Python DB APIs (most often used) facilitate the interaction between Python and the DBMS.

SQL APIs connect to DBMS with one or more API calls, build SQL statements as a text string, and use API calls to send SQL statements to the DBMS and retrieve results and statuses.

DB-API, Python's standard for interacting with relational databases, uses connection objects to establish and manage database connections and cursor objects to run queries and scroll through the results.

Connection Object methods include the cursor(), commit(), rollback(), and close() commands.

You can import the database module, use the Connect API to open a connection, and then create a cursor object to run queries and fetch results. 

Remember to close the database connection to free up resources.


# Module 3 - EDA

### Tools like the 'describe' function in pandas can quickly calculate key statistical measures like mean, standard deviation, and quartiles for all numerical variables in your data frame. 

### Use the 'value_counts' function to summarize data into different categories for categorical data. 

### Box plots offer a more visual representation of the data's distribution for numerical data, indicating features like the median, quartiles, and outliers.

### Scatter plots are excellent for exploring relationships between continuous variables, like engine size and price, in a car data set.

### Use Pandas' 'groupby' method to explore relationships between categorical variables.

### Use pivot tables and heat maps for better data visualizations.

### Correlation between variables is a statistical measure that indicates how the changes in one variable might be associated with changes in another variable.

### When exploring correlation, use scatter plots combined with a regression line to visualize relationships between variables.

### Visualization functions like regplot, from the seaborn library, are especially useful for exploring correlation.

### The Pearson correlation, a key method for assessing the correlation between continuous numerical variables, provides two critical values—the coefficient, which indicates the strength and direction of the correlation, and the P-value, which assesses the certainty of the correlation.

### A correlation coefficient close to 1 or -1 indicates a strong positive or negative correlation, respectively, while one close to zero suggests no correlation.

### For P-values, values less than .001 indicate strong certainty in the correlation, while larger values indicate less certainty. Both the coefficient and P-value are important for confirming a strong correlation.

### Heatmaps provide a comprehensive visual summary of the strength and direction of correlations among multiple variables.


## What is EDA?

### Exploratory data analysis or in short, EDA, is an approach to analyze data in order to summarize main characteristics of the data, gain better understanding of the data set, uncover relationships between different variables and extract important variables for the problem we're trying to solve. The main question we are trying to answer in this module is, what are the characteristics that have the most impact on the car price? We will be going through a couple of different useful exploratory data analysis techniques in order to answer this question. In this module, you will learn about, descriptive statistics, which describe basic features of a data set and obtains a short summary about the sample and measures of the data. Basic of grouping data using GroupBy and how this can help to transform our data set. ANOVA, the analysis of variance a statistical method in which the variation in a set of observations is divided into distinct components. The correlation between different variables. And lastly, advanced correlation, where we'll introduce you to various correlation statistical methods, namely Pearson correlation and correlation heatmaps.

## Descriptive Statistics

### When you begin to analyze data, it's important to first explore your data before you spend time building complicated models. One easy way to do so is to calculate some descriptive statistics for your data. Descriptive statistical analysis helps to describe basic features of a dataset and obtains a short summary about the sample and measures of the data. Let's show you a couple different useful methods. One way in which we can do this is by using the describe function in pandas. Using the describe function and applying it on your data frame, a describe function automatically computes basic statistics for all numerical variables. It shows the mean, the total number of data points, the standard deviation, the quartiles, and the extreme values. Any NaN values are automatically skipped in these statistics. This function will give you a clearer idea of the distribution of your different variables. You could have also categorical variables in your dataset. These are variables that can be divided up into different categories or groups and have discrete values. For example, in our dataset, we have the drive system as a categorical variable,which consists of the categories forward wheel-drive, rear wheel-drive, and four wheel-drive. One way you can summarize the categorical data is by using the function value_counts. We can change the name of the column to make it easier to read. We see that we have 118 cars in the front wheel-drive category, 75 cars in the rear wheel-drive category, and eight cars in the four wheel-drive category. Box plots are a great way to visualize numeric data, since you can visualize the various distributions of the data. The main features that the box plot shows are the median of the data which represents where the middle data point is, the upper quartile shows where the 75th percentile is, the lower quartile shows where the 25th percentile is. The data between the upper and lower quartile represents the inter-quartile range. Next, you have the lower and upper extremes. These are calculated as 1.5 times the inter-quartile range above the 75th percentile, and as 1.5 times the IQR below the 25th percentile. Finally, box plots also display outliers as individual dots that occur outside the upper and lower extremes. With box plots, you can easily spot outliers and also see the distribution and skewness of the data. Box plots make it easy to compare between groups. In this example, using box plot, we can see the distribution of different categories of the drive-wheels feature over price feature. We can see that the distribution of price between the rear wheel-drive and the other categories are distinct. But the price for front wheel-drive and four wheel-drive are almost indistinguishable. Oftentimes, we tend to see continuous variables in our data. These data points are numbers contained in some range. For example, in our dataset, price and engine size are continuous variables. What if we want to understand the relationship between engine size and price? Could engine size possibly predict the price of a car? One good way to visualize this is using a scatter plot. Each observation in a scatter plot is represented as a point. This plot shows the relationship between two variables. The predictor variable is the variable that you are using to predict an outcome. In this case, our predictor variable is the engine size. The target variable is the variable that you are trying to predict. In this case, our target variable is the price since this would be the outcome. In a scatter plot, we typically set the predictor variable on the x-axis or horizontal axis, and we set the target variable on the y-axis or vertical axis. In this case, we will thus plot the engine size on the x-axis and the price on the y-axis. We are using the Matplotlib function scatter here, taking in x and a y variable. Something to note is that it's always important to label your axes and write a general plot title so that you know what you're looking at. Now, how is the variable engine size related to price? From the scatter plot, we see that as the engine size goes up, the price of the car also goes up. This is giving us an initial indication that there is a positive linear relationship between these two variables.



## Correlation 

### we'll talk about the correlation between different variables. Correlation is a statistical metric for measuring to what extent different variables are interdependent. In other words, when we look at two variables over time, if one variable changes, how does this affect change in the other variable? For example, smoking is known to be correlated to lung cancer, since you have a higher chance of getting lung cancer if you smoke. In another example, there is a correlation between umbrella and rain variables, where more precipitation means more people use umbrellas. Also, if it doesn't rain, people would not carry umbrellas. Therefore, we can say that umbrellas and rain are interdependent and by definition they are correlated. It is important to know that correlation doesn't imply causation. In fact, we can say that umbrella and rain are correlated, but we would not have enough information to say whether the umbrella caused the rain or the rain caused the umbrella. In data science, we usually deal more with correlation. Let's look at the correlation between engine size and price. This time we'll visualize these two variables using a scatter plot and an added linear line called a regression line, which indicates the relationship between the two. The main goal of this plot is to see whether the engine size has any impact on the price. In this example, you can see that the straight line through the data points is very steep, which shows that there is a positive linear relationship between the two variables. With increase in values of engine size, values of price go up as well, and the slope of the line is positive. So there is a positive correlation between engine size and price. We can use seaborne reg plot to create the scatter plot. As another example, now let's look at the relationship between highway miles per gallon to see its impact on the car price. As we can see in this plot, when highway miles per gallon value goes up, the value of price goes down. Therefore, there is a negative linear relationship between highway miles per gallon and price. Although this relationship is negative, the slope of the line is steep, which means that the highway miles per gallon is still a good predictor of price. These two variables are said to have a negative correlation. Finally, we have an example of a weak correlation. For example, both low peak RPM and high values of peak RPM have low and high prices. Therefore, we cannot use RPM to predict the values.


## Correlation Statistics 

### we'll introduce you to various correlation statistical methods. One way to measure the strength of the correlation between continuous numerical variables is by using a method called Pearson Correlation. Pearson Correlation method will give you two values; the correlation coefficient and the p-value. How do we interpret these values? For the correlation coefficient, a value close to one implies a large positive correlation, while a value close to -1 implies a large negative correlation, and a value close to zero implies no correlation between the variables. Next, the p-value will tell us how certain we are about the correlation that we calculated. For the p-value, a value less than 0.001 gives us a strong certainty about the correlation coefficient that we calculated, a value between 0.001 and 0.05 gives us moderate certainty, a value between 0.05 and 0.1 will give us a weak certainty, and a p-value larger than 0.1 will give us no certainty of correlation at all. We can say that there is a strong correlation when the correlation coefficient is close to one or -1 and the p-value is less than 0.001. The following plot shows data with different correlation values. In this example, we want to look at the correlation between the variables horsepower and car price. See how easy you can calculate the Pearson Correlation using the Scipy stats package? We can see that the correlation coefficient is approximately 0.8 and this is close to one, so there's a strong positive correlation. We can also see that the p-value is very small, much smaller than 0.001, and so we can conclude that we are certain about the strong positive correlation. Taking all variables into account, we can now create a heat map that indicates the correlation between each of the variables with one another. The color scheme indicates the Pearson correlation coefficient, indicating the strength of the correlation between two variables. We can see a diagonal line with a dark red color indicating that all the values on this diagonal are highly correlated. This makes sense because when you look closer, the values on the diagonal are the correlation of all variables with themselves, which will be always one. This correlation heat map gives us a good overview of how the different variables are related to one another, and most importantly, how these variables are related to price.