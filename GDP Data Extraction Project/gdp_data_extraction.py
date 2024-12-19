"""
Project Scenario : 
An international firm is looking to expand business in different countries across the world 
Data Engineers are tasked with creating a script that can extract the list of the 
top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), 
as logged by the International Monetary Fund (IMF).

required data available at : 
https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29
"""

import pandas as pd
import numpy as np
import lxml
import ssl
import certifi
import warnings
import urllib.request

# Disable warnings
def warn(*args, **kwargs):
    pass

warnings.warn = warn
warnings.filterwarnings('ignore')

# URL of the Wikipedia page
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Create SSL context using certifi's certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Use urllib to fetch the content with certifi's SSL context
response = urllib.request.urlopen(URL, context=ssl_context)
html = response.read()

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(html)
df = tables[3]
print(df)


# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11,:]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

# Load the DataFrame to the CSV file named "Largest_economies.csv"
df.to_csv('./Largest_economies.csv')

