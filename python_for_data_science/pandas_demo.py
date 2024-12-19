import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mydict = {
    'scores': [42, 87, 19, 65, 23],
    'ages': [32, 29, 58, 42, 25],
    'grades': [92, 76, 88, 97, 64],
    'temperatures': [15, 23, -3, 10, 5],
    'sales': [450, 876, 560, 732, 198]
}

#dictionary to dataframe
mydict_df = pd.DataFrame(mydict) 

#numpy operations
a = np.array([-1,1]) 
b = np.array([1,1]) 
print("answer",np.dot(a,b) )

X = np.array([[1,0],[0,1]])
Y = np.array([[2,2],[2,2]]) 
Z = np.dot(X,Y) 
print("output", Z)

# ************ API ********

dict_ = {
    'a':[11,21,31],
    'b':[12,22,32]
    }

df = pd.DataFrame(dict_)
print("Type : ", type(df))

