import pandas as pd
import matplotlib.pyplot as plt

vehicles = pd.read_csv('Datasets/vehicles.csv')

vehicles.plot(kind="scatter", x="year", y="co2emissions")
plt.show()

