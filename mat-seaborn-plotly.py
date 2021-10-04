import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

data = pd.read_csv('https://github.com/kapildeshmukh-afk/titanic_/blob/main/tested.csv')
data.head()
#using seaborn and matplotlib
sns.countplot(data['Survived'])
plt.title("Not survived and survived")
plt.xlabel("Survival")
plt.ylable("Count")
plt.show()
#using plotly
fig = px.line(data, x = 'Age', y = 'Pclass', title='titanic database')
fig.show()
