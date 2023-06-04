import pandas as pd
import matplotlib.pyplot as plt

vehicles = pd.read_csv('Datasets/vehicles.csv')

# Pandas histogram uses only 1 column of the dataframe
emissions = vehicles['co2emissions']
print(type(emissions))

emissions.plot(kind='hist')

plt.show()


