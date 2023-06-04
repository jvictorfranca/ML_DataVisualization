import pandas as pd
import matplotlib.pyplot as plt
import math

credit_data = pd.read_csv('Datasets\credit_data.csv')

credit_data = credit_data[credit_data['age']>=0]

max_age = credit_data['age'].max()
min_age = credit_data['age'].min()

rounded_max_age =  math.ceil(max_age/10)*10
rounded_min_age = math.floor(min_age/10)*10

graph = plt.hist(x=credit_data['age'], range=(rounded_min_age, rounded_max_age))

plt.show()