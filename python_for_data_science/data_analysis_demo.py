from PIL import Image
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

#imagefileurl = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
fileurl = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# download file
response = requests.get(fileurl)
if response.status_code == 200:
    with open("diabetes.csv", 'wb') as f:
        f.write(response.content)

df = pd.read_csv("diabetes.csv")

# we can use the **dataframe.head(n)** method to check the top n rows of the dataframe, 
# where n is an integer. 
# Contrary to **dataframe.head(n)**, **dataframe.tail(n)** 
# will show you the bottom n rows of the dataframe.

print("\nThe first 5 rows of the dataframe\n", df.head(5)) 
print("\nThe last 5 rows of the dataframe\n", df.tail(5))

# missing data
missing_data = df.isnull()
print("\n Missing data : \n", missing_data.head(5))

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# .dtype() to check the data type

# .astype() to change the data type
print("\n Data types of the columns\n", df.dtypes)

'''
Visualization
'''

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()