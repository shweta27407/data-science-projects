# Model Evaluation 
We will learn about simple and multiple linear regression, model evaluation using visualization, polynomial regression and pipelines, R-squared and MSE for in-sample evaluation, prediction and decision making, and how you can determine a fair value for a used car. 

A model or estimator can be thought of as a mathematical equation used to predict a value given one or more other values, relating one or more independent variables or features to dependent variables. 

For example, you input a car models highway miles per gallon as the independent variable or feature. 

The output of the model or dependent variable is the price. 

Usually the more relevant data you have, the more accurate your model is. For example, you input multiple independent variables or features to your model. 

Therefore, your model may predict a more accurate price for the car. To understand why more data is important consider the following situation. You have two almost identical cars. 

Pink cars sell for significantly less. You want to use your model to determine the price of two cars, one pink, one red. If your model's independent variables or features do not include color, your model will predict the same price for cars that may sell for much less. 

In addition to getting more data, you can try different types of models. In this course you will learn about simple linear regression, multiple linear regression, and polynomial regression.

## Linear Regression and Multiple Linear Regreession

Linear regression will refer to one independent variable to make a prediction. Multiple linear regression will refer to multiple independent variables to make a prediction. 

Simple linear regression, or SLR, is a method to help us understand the relationship between two variables: the predictor (independent variable x) and the target (dependent variable y). We would like to come up with a linear relationship between the variables shown here. The parameter b0 is the intercept, the parameter b1 is the slope. When we fit or train the model we will come up with these parameters. 

This step requires lots of math, so we will not focus on this part. Let's clarify the prediction step. 

It's hard to figure out how much a car costs, but the highway miles per gallon is in the owner's manual. If we assume there is a linear relationship between these variables, we can use this relationship to formulate a model to determine the price of the car. If the highway miles per gallon is 20, we can input this value into the model to obtain a prediction of $22,000. 

In order to determine the line, we take data points from our data set marked in red here. We then use these training points to fit our model. The results of the training points are the parameters. 

We usually store the data points in two data frame or NumPy arrays. The value we would like to predict is called the target that we store in the array y. 

We store the dependent variable in the data frame or array x. Each sample corresponds to a different row in each data frame or array. In many cases, many factors influence how much people paid for a car, for example, make or how old the car is. 

In this model, this uncertainty is taken into account by assuming a small random value is added to the point on the line. This is called noise. The figure on the left shows the distribution of the noise. The vertical axis shows the value added and the horizontal axis illustrates the probability that the value will be added. Usually a small positive value is added or a small negative value.
Play video starting at :2:30 and follow transcript2:30
Sometimes large values are added, but for the most part, the values added are near zero.
Play video starting at :2:39 and follow transcript2:39
We can summarize the process like this. We have a set of training points. We use these training points to fit or train the model and get parameters. We then use these parameters in the model, we now have a model. We use the hat on the y to denote the model is an estimate. We can use this model to predict values that we haven't seen, for example, we have no car with 20 highway miles per gallon. We can use our model to make a prediction for the price of this car but don't forget our model is not always correct. We can see this by comparing the predicted value to the actual value. We have a sample for ten highway miles per gallon, but the predicted value does not match the actual value. If the linear assumption is correct, this error is due to the noise but there can be other reasons. To fit the model in Python, first we import linear model from scikit-learn. Then create a linear regression object using the constructor. We define the predictor variable and target variable. Then use the method fit to fit the model and find the parameters b0 and b1, the input are the features and the targets. We can obtain a prediction using the method predict. The output is an array. The array has the same number of samples as the input x. The intercept b0 is an attribute of the object lm the slope b1 is also an attribute of the object lm. The relationship between price and highway miles per gallon is given by this equation in bold: price = 38,423.31 - 821.73 times highway miles per gallon, like the equation we discussed before.
Play video starting at :4:38 and follow transcript4:38
Multiple linear regression is used to explain the relationship between one continuous target (y) variable and two or more predictor (x) variables.
Play video starting at :4:49 and follow transcript4:49
If we have, for example, four predictor variables, then b0 intercept x=0, b1, the coefficient or parameter of x1, b2, the coefficient of parameter x2, and so on. If there are only two variables, then we can visualize the values. Consider the following function the variables x1 and x2 can be visualized on a 2D plane, let's do an example on the next slide. The table contains different values of the predictor variables x1 and x2. The position of each point is placed on the 2D plane, color coded accordingly. Each value of the predictor variables x1 and x2 will be mapped to a new value y, y hat. The new values of y, y hat, are mapped in the vertical direction with height proportional to the value that y hat takes.
Play video starting at :5:48 and follow transcript5:48
We can fit the multiple linear regression as follows. We can extract the four predictor variables and store them in the variable z then train the model as before using the method fit or dependent variables and the targets colon. We can also obtain a prediction using the method predict. In this case, the input is an Array or data frame with four columns. The number of rows corresponds to the number of samples. The output is an array with the same number of elements as number of samples. The intercept is an attribute of the object and the coefficients are also attributes. It is helpful to visualize the equation replacing the independent variable names with actual names. This is identical to the form we discussed earlier.


## Lesson Summary

Congratulations! You have completed this lesson. At this point in the course, you know: 

Linear regression refers to using one independent variable to make a prediction.

You can use multiple linear regression to explain the relationship between one continuous target y variable and two or more predictor x variables.

Simple linear regression, or SLR, is a method used to understand the relationship between two variables, the predictor independent variable x and the target dependent variable y.

Use the regplot and residplot functions in the Seaborn library to create regression and residual plots, which help you identify the strength, direction, and linearity of the relationship between your independent and dependent variables.

When using residual plots for model evaluation, residuals should ideally have zero mean, appear evenly distributed around the x-axis, and have consistent variance. If these conditions are not met, consider adjusting your model.

Use distribution plots for models with multiple features: Learn to construct distribution plots to compare predicted and actual values, particularly when your model includes more than one independent variable. Know that this can offer deeper insights into the accuracy of your model across different ranges of values.

The order of the polynomials affects the fit of the model to your data. Apply Python's polyfit function to develop polynomial regression models that suit your specific dataset.

To prepare your data for more accurate modeling, use feature transformation techniques, particularly using the preprocessing library in scikit-learn, transform your data using polynomial features, and use the modules like StandardScaler to normalize the data.

Pipelines allow you to simplify how you perform transformations and predictions sequentially, and you can use pipelines in scikit-learn to streamline your modeling process.

You can construct and train a pipeline to automate tasks such as normalization, polynomial transformation, and making predictions.

To determine the fit of your model, you can perform sample evaluations by using the Mean Square Error (MSE), using Python’s mean_squared_error function from scikit-learn, and using the score method to obtain the R-squared value.

A model with a high R-squared value close to 1 and a low MSE is generally a good fit, whereas a model with a low R-squared and a high MSE may not be useful.

Be alert to situations where your R-squared value might be negative, which can indicate overfitting. 

When evaluating models, use visualization and numerical measures and compare different models.

The mean square error is perhaps the most intuitive numerical measure for determining whether a model is good.

A distribution plot is a suitable method for multiple linear regression.

An acceptable r-squared value depends on what you are studying and your use case.

To evaluate your model’s fit, apply visualization, methods like regression and residual plots, and numerical measures such as the model's coefficients for sensibility: 

Use Mean Square Error (MSE) to measure the average of the squares of the errors between actual and predicted values and examine R-squared to understand the proportion of the variance in the dependent variable that is predictable from the independent variables.

When analyzing residual plots, residuals should be randomly distributed around zero for a good model. In contrast, a residual plot curve or inaccuracies in certain ranges suggest non-linear behavior or the need for more data.