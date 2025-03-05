# Exception Handling

Common Exceptions in Python
Here are a few examples of exceptions we often run into and can handle using this tool:

1. ZeroDivisionError: This error arises when an attempt is made to divide a number by zero. Division by zero is undefined in mathematics, causing an arithmetic error. For instance:
For example:
result = 10 / 0 
print(result)


2. ValueError: This error occurs when an inappropriate value is used within the code. An example of this is when trying to convert a non-numeric string to an integer:
For example:
1 num = int("abc")


3. FileNotFoundError: This exception is encountered when an attempt is made to access a file that does not exist.
For example:
with open("nonexistent_file.txt", "r") as file:
     content = file.read()  


4. IndexError: An IndexError occurs when an index is used to access an element in a list that is outside the valid index range.
For example:

my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError


5. KeyError: The KeyError arises when an attempt is made to access a non-existent key in a dictionary.
For example:
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError


6. TypeError: The TypeError occurs when an object is used in an incompatible manner. An example includes trying to concatenate a string and an integer:
For example:
result = "hello" + 5   # Raises TypeError


7. AttributeError: An AttributeError occurs when an attribute or method is accessed on an object that doesn't possess that specific attribute or method. For instance:
For example:
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError


8. ImportError: This error is encountered when an attempt is made to import a module that is unavailable. For example: import non_existent_module

Note: Please remember, the exceptions you will encounter are not limited to just these. There are many more in Python. 
By using the technique provided below and following the correct syntax, you will be able to handle any exceptions that come your way.

Handling Exceptions:

Try and Except : You can use the try and except blocks to prevent your program from crashing due to exceptions.

The code that may result in an exception is contained in the try block.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```

# Pandas Attributes and Methods

### Series Operations
1. **values**: Returns the Series data as a NumPy array.
2. **index**: Returns the index (labels) of the Series.
3. **shape**: Returns a tuple representing the dimensions of the Series.
4. **size**: Returns the number of elements in the Series.
5. **mean()**, **sum()**, **min()**, **max()**: Calculate summary statistics of the data.
6. **unique()**, **nunique()**: Get unique values or the number of unique values.
7. **sort_values()**, **sort_index()**: Sort the Series by values or index labels.
8. **isnull()**, **notnull()**: Check for missing (NaN) or non-missing values.
9. **apply()**: Apply a custom function to each element of the Series.

---

### DataFrame Operations
1. **shape**: Returns the dimensions (number of rows and columns) of the DataFrame.
2. **info()**: Provides a summary of the DataFrame, including data types and non-null counts.
3. **describe()**: Generates summary statistics for numerical columns.
4. **head()**, **tail()**: Displays the first or last `n` rows of the DataFrame.
5. **mean()**, **sum()**, **min()**, **max()**: Calculate summary statistics for columns.
6. **sort_values()**: Sort the DataFrame by one or more columns.
7. **groupby()**: Group data based on specific columns for aggregation.
8. **fillna()**, **drop()**, **rename()**: Handle missing values, drop columns, or rename columns.
9. **apply()**: Apply a function to each element, row, or column of the DataFrame.

# Web Scraping with Python

Python provides several libraries for web scraping. Here are some of them:

1. BeautifulSoup: BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

```
from bs4 import BeautifulSoup
import requests
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
```

2. Scrapy: Scrapy is an open-source and collaborative web crawling framework for Python. It is used to extract the data from the website.

```
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}
```

3. Selenium: Selenium is a tool used for controlling web browsers through programs and automating browser tasks.

```
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.example.com")
```




