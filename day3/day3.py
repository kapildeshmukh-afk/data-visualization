import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd
i
mport numpy as np

files=pd.read_csv('./titanic.csv')

files.head(1000)


print(files.isnull().sum())#there will be sum of errors 

#to clean the error on cabin column
 
files.Cabin=files.Cabin.fillna("null")

#to clean the error on Age column
 
files.Age=files.Age.fillna("age_empty")
 
#to clean the error on FAre column
 
files.Fare=files.Fare.fillna("fare_empty")

 
print(files.isnull().sum())     
#after this all error will be clean
#graph for 50 range(split)
sns.barplot(x='Fare',y='Pclass' ,data=files,bins=10 ,xLimit=50)