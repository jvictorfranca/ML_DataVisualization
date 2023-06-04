import pandas as pd
import numpy as np
import plotly.express as px

credit_data = pd.read_csv('Datasets\credit_data.csv')

print(credit_data.columns)

credit_data['color_labels'] = np.where(credit_data['default'] == 1, "Defaulted", "Not_Defaulted" )

age_conditions = [((credit_data['age'] >= 0) & (credit_data['age'] < 30)), ((credit_data['age'] >= 30) & (credit_data['age'] < 50)), (credit_data['age'] >= 50) ]
age_values = ["Less than 30 years", "Less than 50 years", "More than 50 years"]

credit_data['age_labels'] = np.select(age_conditions, age_values)
credit_data['age'] = round(credit_data['age'],0).astype(str)

treemap_plot = px.treemap(credit_data, path=['color_labels', 'age_labels', 'age'])
treemap_plot.write_html('./Plots/Treemap/treemap_px.html')