import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

credit_data = pd.read_csv('Datasets\credit_data.csv')

print(np.unique(credit_data['default'], return_counts=True))
graph = sns.countplot(x=credit_data['default'])

plt.show()