## Welcome to Seaborn and regression plots. 

Although Seaborn is another data visualization library, it's based on Matplotlib. Seaborn offers a range of built-in themes and color palettes that improve the visual appeal of your plots with minimal effort. 

Seaborn makes creating plots very efficient, therefore, with Seaborn, you can generate plots with code that is five times less than with Matplotlib. 

Seaborn integrates well with statistical libraries such as NumPy and SciPy, allowing you to easily combine statistical analysis with visualizations. 

It provides specialized plot types such as regression plots, distribution plots, and categorical plots, that are particularly useful for analyzing data and modeling relationships.


While Pandas and Matplotlib are powerful tools for data manipulation and basic visualization, Seaborn complements them by providing a higher level interface for creating visually appealing and informative statistical graphics. 

Seaborn works well, especially when dealing with more complex visualizations and statistical analyses. 

Let's see how we can use Seaborn to create a statistical graphic. 

Let's look into regression plots. Let's say we have a data frame called df_total, representing total immigration to Canada from 1980 to 2013. The data frame displays the year in one column and the corresponding total immigration in another. We want to create a scatter plot and a regression line to highlight any trends in the data.

With Seaborn, you can do all this with one line of code. 

   ![word cloud](https://github.com/shweta27407/data-science-projects/blob/main/Data_Science_IBM_Notes/Data_Visualization_Python_IBM/module_2_specialized_visualization_tools/images/regplot.png)


Let's go ahead and change the shape of our markers to a plus marker instead of the default circular marker. Let's try to plot some categorical data. In our Canada immigration data set, there are some categorical features such as country, region, and continent. 

Why not plot continents for their count in the data set?

Using a single line of code, we can create a bar plot representing the count of records for each continent in the data using the counterplot function. 


Let's try to plot the Bohr plot on the categorical data from a slice of the df_Canada data set. 

Here we have plotted the continent by the total column of data. 

Seaborn has been grouped by the categorical variable continent and plotted the aggregated values of total, with confidence interval. 

You'll explore more in the lab session on Seaborn. In this video, you learned that Seaborn is a Data Visualization library based on Matplotlib. Seaborn was built primarily to provide a high-level interface for drawing statistical graphics. Scatter Plots and Regression Lines can be created with one line of code using Seaborn.
