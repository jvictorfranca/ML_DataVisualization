
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier

titanic = sns.load_dataset('titanic')

titanic['age'] = titanic.age.fillna(titanic.age.mean())
titanic.drop(columns=['class', 'who', 'adult_male', 'deck', 'embark_town', 
                      'alive', 'alone'], inplace=True)

titanic_dummies = pd.get_dummies(titanic, drop_first=True)
X = titanic_dummies.drop(columns = ['survived'])
y = titanic_dummies['survived']

arvore = DecisionTreeClassifier(criterion='gini', max_depth = 3, random_state=42)

arvore.fit(X, y)

plt.figure(figsize=(20, 10))
plot_tree(arvore, feature_names=X.columns.tolist(), class_names=['Not Survived', 'Survived'], filled=True)
plt.show()