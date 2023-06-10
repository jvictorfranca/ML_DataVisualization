import pandas as pd
import numpy as np

credit_data = pd.read_csv('Datasets\credit_data.csv')

# Get color labels with one condition:

credit_data['color_labels_default'] = np.where(credit_data['default'] == 1, "Defaulted", "Not_Defaulted" )
print(credit_data.head())

#  Get color labels with multiple conditions:

col         = 'loan'
conditions  = [ credit_data[col] >= 5000, (credit_data[col] < 5000) & (credit_data[col]> 2500), credit_data[col] <= 2500 ]
choices     = [ "high", 'medium', 'low' ]
credit_data["color_labels_loan"] = np.select(conditions, choices, default=np.nan)
print(credit_data)
