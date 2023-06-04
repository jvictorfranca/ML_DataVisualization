import pandas as pd
import numpy as np
import plotly.express as px

credit_data = pd.read_csv('Datasets\credit_data.csv')

print(credit_data.columns)

credit_data['color_labels'] = np.where(credit_data['default'] == 1, "Defaulted", "Not_Defaulted" )

age_conditions = [((credit_data['age'] >= 0) & (credit_data['age'] < 30)), ((credit_data['age'] >= 30) & (credit_data['age'] < 50)), (credit_data['age'] >= 50) ]
age_values = ["Less than 30 years", "Less than 50 years", "More than 50 years"]

income_conditions = [((credit_data['income'] >= 0) & (credit_data['income'] < 30000)), ((credit_data['income'] >= 30000) & (credit_data['income'] < 50000)), (credit_data['income'] >= 50000) ]
income_values = ["Less than 30K year", "Less than 50K year", "More than 50K year"]

credit_data['age_labels'] = np.select(age_conditions, age_values)
credit_data['income_labels'] = np.select(income_conditions, income_values)


paralel_categories_plot = px.parallel_categories(credit_data, dimensions= ['color_labels', 'age_labels', 'income_labels'])
paralel_categories_plot.write_html('./Plots/Paralel Categories/paralel_categories_px.html')