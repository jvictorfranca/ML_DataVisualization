import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


titanic = pd.read_csv('Datasets/titanic.csv')

for i, col in enumerate(['SibSp', 'Parch']):
    plt.figure(i)
    sns.catplot(x=col, y='Survived', data=titanic, kind='point', aspect=2, )

plt.show()