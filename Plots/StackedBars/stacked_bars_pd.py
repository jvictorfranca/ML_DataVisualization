import pandas as pd
import matplotlib.pyplot as plt

vehicles = pd.read_csv('Datasets/vehicles.csv')

# First, group the colum you want to study by the bars stacked, on the example, each year will be a bar, with stacks of drive.:

vehicles.groupby('year')['drive'].value_counts()

# Now use unstack() to get on the x axes the year, and on the columns each unique type (drive on example):

treated_dataframe = vehicles.groupby('year')['drive'].value_counts().unstack()
print(treated_dataframe)

treated_dataframe.plot(kind = 'bar', stacked = True, figsize = (10, 6))

plt.show()
