import pandas as pd
import numpy as np
import plotly.express as px

credit_data = pd.read_csv('Datasets\credit_data.csv')

print(credit_data.columns)

credit_data['color_labels'] = np.where(credit_data['default'] == 1, "Defaulted", "Not_Defaulted" )

scatter_matrix_plot = px.scatter_matrix(credit_data, dimensions=['age', 'income', 'loan'], color='color_labels')
scatter_matrix_plot.write_html('./Plots/Scatter/scatter_matrix_px.html')