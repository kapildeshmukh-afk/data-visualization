import pandas as pd
import numpy as np
import seaborn as sb
from sklearn import ensemble
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(test_size=0.3,random_state=0)

df = pd.read_csv('titanic.csv', sep='\t', engine='python')


X = df.values
y = df['Survived'].values

#random forest classifier

rf_clf = ensemble.RandomForestClassifier(n_estimators=100)
rf_clf.fit(X_train, y_train)
rf_clf.score(X_test, y_test)


