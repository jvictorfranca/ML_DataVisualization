import pandas as pd

vehicles = pd.read_csv('Datasets/vehicles.csv')
titanic = pd.read_csv('Datasets/titanic.csv')

# Gets initial info of dataframe
info = vehicles.info()
print(info)

# Gets shape of dataframe
shape = vehicles.shape
print(shape)

# Gets first rols of the dataframe (can specify numbers)
first_rows = vehicles.head(15)
print(first_rows)

# Describe categorical column
categorical_column = vehicles['class']
categorical_info = categorical_column.describe()
print(categorical_info)

# Describe numeric column
numeric_column = vehicles['co2emissions']
numeric_info = numeric_column.describe()
print(numeric_info)

# Use mask to locate items
    # Create a mask with logic
mask = (vehicles['drive'] == '2-Wheel Drive') & (vehicles['displacement'] == 2.6)
print(mask)
 
   # Filter by the logic mask
filtered = vehicles[mask]
print(filtered)

    # Or filter using pandas .loc
filtered_loc = vehicles.loc[mask, :]
print(filtered_loc)

# Use groupby to see relations on 0 or 1 values:
survivability_by_Cabin = titanic.groupby(titanic['Cabin'].isnull())['Survived'].mean()
print(survivability_by_Cabin)
