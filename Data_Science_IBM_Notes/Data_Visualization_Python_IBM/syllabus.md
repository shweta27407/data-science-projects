## Module 1 Title: Introduction to Data Visualization Tools

Data visualization is a way of presenting complex data in a form that is graphical and easy to understand. 

When analyzing large volumes of data and making data-driven decisions, data visualization is crucial. 

In this module, you will learn about data visualization and some key best practices to follow when creating plots and visuals. 

You will discover the history and the architecture of Matplotlib. 

Furthermore, you will learn about basic plotting with Matplotlib and explore the dataset on Canadian immigration, which you will use during the course. Lastly, you will analyze data in a data frame and generate line plots using Matplotlib.


### Types of Plots 

As we know, data visualization represents data using visual formats like graphs, charts and maps. It effectively communicates information, trends and insights concisely, it also uncovers patterns, identify trends and simplifies complex information for easy understanding. 

#### Line Plot
A line plot, also known as a line chart, displays data as a series of data points connected by straight lines. 
Line plots display trends, such as stock market fluctuations or temperature changes over time, they compare datasets with a continuous independent variable like age or time. 
Line plots illustrate cause and effect relationships, such as sales revenue changes based on marketing budget. 
They also visualize continuous data, like height measurements over time. Line plots can be misleading if the scales on the axes are not carefully chosen to reflect the data accurately. 

The line plot shows a downfall in immigration trends in 1998, however, if you will correct the scale on the y-axis to start with zero, as in this plot, you'll see that the actual trend is not that alarming. 

#### Bar Plot
A bar plot, also known as a bar chart, displays data using rectangular bars, where the height or length of the bars represents the magnitude of the data. 

The bars can be oriented either vertically or horizontally. A vertically oriented bar chart is often referred to as a vertical bar chart or a column chart. 

If you're looking for an effective way to compare data, bar plots are ideal for comparing different categories or groups. They excel with discrete data, like comparing sales revenue by product. They show how different categories contribute to the whole and rankings, such as sales percentage or budget allocation. 

Bar plots can visualize data that you can easily rank, like displaying the bestselling books in the market. Their simplicity and interpretability, make them favored for data visualization.

Inaccurate bar choices or axis scales, can lead to misleading plots. 

In this bar plot, the y-axis starting at six, makes the difference between the values in 1995 and 1998 seem larger than it actually is. However, when the y-axis starts at zero, the plot accurately represents the data without misleading the viewer. 


#### Scatter Plot 
A scatter plot, is a type of plot that presents values for two variables for a set of data using Cartesian coordinates. 

The data points are displayed as a collection of points, where one variable's value determines the position on the horizontal axis and the other variable's value determines the position on the vertical axis. 

When can you use a scatter plot? Let's explore some options. You can use it for examining the relationship between two continuous variables like temperature and energy consumption. Investigating patterns or trends in data, such as house prices versus size, detecting outliers or unusual observations such as outliers in test scores or abnormal stock behavior. Visualizing data with many observations to identify clusters or groups, and exploring complex data. Outliers significantly impact interpretation, requiring consideration of their inclusion or exclusion. On the screen, the data is plotted with and without outliers. With outliers, it shows two clusters, but removing outliers makes the remaining data more visible. Proper outlier handling, enhances accuracy and meaningful insights in scatter plots. 

#### Box Plot 
A box plot, also known as a box and whisker plot, is a type of plot that displays the distribution of a data set, along with key statistical measures. 

It consists of a box, representing the interquartile range, IQR, a line inside the box representing the median and lines whiskers extending from the box to indicate the range of the data, excluding outliers. Outliers may be represented as individual data points beyond the whiskers. Let's look at some scenarios where box plots come in handy. While comparing the distribution of a continuous variable across different categories or groups. 

For example, employees salaries across departments, examining spread and skewness of data set, visualizing quartiles and outliers, identifying and analyzing potential outliers within a data set. 
Visualizing summary statistics, median, quartiles, range in a concise and informative manner, comparing distributions of multiple variables in datasets side by side. 

Remember, box plots provide valuable information about outliers, such as their presence and extent. Ignoring or mishandling outliers, can distort the interpretation of the data and mask important insights, same as with scatter plots. 

#### Histogram
A histogram, is a graphical representation of the distribution of a data set, showing the frequency or relative frequency of values within specific intervals.

It consists of bars, where the height represents the data count in each interval. Histograms offer valuable insights into data distribution, outliers, skewness and variability.
They visually depict the shape of the data, whether it's symmetric skewed or bimodal. Skewness can be assessed by examining the histogram's shape. Histograms also showcase data variability, allowing you to observe concentrations, gaps and clusters that reveal patterns or subgroups. Apart from issues with scale and inadequate labeling, be careful while choosing the bins to create a histogram. We have generated a random data set and created three histograms, with three different binning options. 

Too few bins, five represented in green color, an optimal number of bins, 20 represented in blue and too many bins 50, the yellow one. By comparing these histograms, you can observe how the choice of binning affects the representation of the data distribution and results in a misleading representation of the data. Selecting too few or too many bins, can oversimplify or overcomplicate the distribution, respectively. 

there are various types of plots commonly used in data visualization.
Line plots capture trends and changes over time, allowing us to see patterns and fluctuations. 

Bar plots compare categories or groups, providing a visual comparison of their values. 

Scatter plots explore relationships between variables, helping us identify correlations or trends. 

Box plots display the distribution of data, showcasing the median, quartiles and outliers. 

Histograms illustrate the distribution of data within specific intervals, allowing us to understand its shape and concentration. 

### Libraries

Matplotlib is a plotting library that offers a wide range of plotting capabilities. 

Pandas is a plotting library that provides integrated plotting functionalities for data analysis. 

Seaborne is a specialized library for statistical visualizations, offering attractive default aesthetics and color palettes. 

Follium is a Python library that allows you to create interactive and customizable maps. 

Plotly is an interactive and dynamic library for data visualization that supports a wide range of plot types and interactive features. 

PyWaffle enables you to visualize proportional representation using squares or rectangles.

## Module 2 Title: Basic and Specialized Visualization Tools

Visualization tools play a crucial role in data analysis and communication. 

These are essential for extracting insights and presenting information in a concise manner to both technical and non-technical audiences. 

In this module, you will create a diverse range of plots using Matplotlib, the data visualization library. 

Throughout this module, you will learn about area plots, histograms, bar charts, pie charts, box plots, and scatter plots. 

You will also explore the process of creating these visualization tools using Matplotlib.


## Module 3 Title: Advanced Visualizations and Geospatial Data

Advanced visualization tools are sophisticated platforms that provide a wide range of advanced features and capabilities. 

These tools provide an extensive set of options that help create visually appealing and interactive visualizations. 

In this module, you will learn about waffle charts and word cloud including their application. 

You will explore Seaborn, a new visualization library in Python, and learn how to create regression plots using it. 

In addition, you will learn about folium, a data visualization library that visualizes geospatial data. 

Furthermore, you will explore the process of creating maps using Folium and superimposing them with markers to make them interesting. Finally, you will learn how to create a Choropleth map using Folium.


## Module 4 Title: Creating Dashboards with Plotly and Dash


Dashboards and interactive data applications are crucial tools for data visualization and analysis because they provide a consolidated view of key data and metrics in a visually appealing and understandable format. 

In this module, you will explore the benefits of dashboards and identify the different web-based dashboarding tools in Python. 

You will learn about Plotly and discover how to use Plotly graph objects and Plotly express to create charts. 

You will gain insight into Dash, an open-source user interface Python library, and its two components. 

Finally, you will gain a clear understanding of the callback function and determine how to connect core and HTML components using callback.


## Module 5 Title: Final Project and Exam

The primary focus of this module is to practice the skills gained earlier in the course and then demonstrate those skills in your final assignment. 

For the final assignment you will analyze historical automobile sales data covering periods of recession and non-recession. 

You will bring your analysis to life using visualization techniques and then display the plots and graphs on dashboards. 

Finally, you will submit your assignment for peer review and you will review an assignment from one of your peers. 

To wrap up the course you will take a final exam in the form of a timed quiz.



