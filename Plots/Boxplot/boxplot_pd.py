import pandas as pd
import matplotlib.pyplot as plt

vehicles = pd.read_csv('Datasets/vehicles.csv')

# Needs to pivot the DataFrame in order to have independent columns on the feature being studied.

print(vehicles.pivot(columns = 'drive', values = 'co2emissions'))

treated_dataframe = vehicles.pivot(columns = 'drive', values = 'co2emissions')


treated_dataframe.plot(kind = 'box', figsize = (10, 6))
plt.show()
