"""
Your job is to extract financial data like historical share price and quarterly revenue reportings 
from various sources using Python libraries and webscraping on popular stocks. After collecting this data you will visualize it in a dashboard to identify patterns or trends. The stocks we will work with are Tesla, Amazon, AMD, and GameStop.


"""

import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

# download and save the file data
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response = requests.get(url)

# Save the content as a .py file
with open("apple.json", "w", encoding="utf-8") as file:
    file.write(response.text)

print("File downloaded as apple.py")

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))

print(apple_info)

print("\n Country : ", apple_info['country'])

apple_share_price_data = apple.history(period="max")

print(apple_share_price_data.head())

'''
We can reset the index of the DataFrame with the `reset_index` function. 
We also set the `inplace` paramter to `True` so the change takes place to the DataFrame itself.
'''

apple_share_price_data.reset_index(inplace=True)

# plot Open price against Date
apple_share_price_data.plot(x="Date", y="Open")

# dividends
print(apple.dividends)
apple.dividends.plot()



# Ticker module  AMD DATA
amd = yf.Ticker("AMD")

amd_info = amd.info
print("\n\n AMD DATA : ", amd_info)

print("\n\n Country AMD : ", amd_info['country'])
print("\n\n Sector AMD : ", amd_info['sector'])

# AMD Share Price Data

amd_share_price_data = amd.history(period="max")

print(amd_share_price_data.head())