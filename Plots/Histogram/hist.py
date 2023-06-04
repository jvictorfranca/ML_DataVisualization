import pandas as pd
import matplotlib.pyplot as plt

credit_data = pd.read_csv('Datasets\credit_data.csv')

credit_data = credit_data[credit_data['age']>=0]

plt.show()