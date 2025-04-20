import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

import patsy
import time

titanic = sns.load_dataset('titanic')

titanic.head()


# Transforms the notation in a design matrix . Creates dummies automatically.
y, X = patsy.dmatrices('survived ~ pclass + sex + age + sibsp + parch + fare + embarked', data=titanic, return_type="dataframe")

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2360873)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

rf = RandomForestClassifier(n_estimators=50, random_state=42)
rf.fit(X_train, y_train)