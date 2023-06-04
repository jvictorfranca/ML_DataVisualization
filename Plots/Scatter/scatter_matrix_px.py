import pandas as pd
import plotly.express as px

credit_data = pd.read_csv('Datasets\credit_data.csv')

print(credit_data.columns)

scatter_matrix_plot = px.scatter_matrix(credit_data, dimensions=['age', 'income', 'loan'], color='default')
scatter_matrix_plot.write_html('./scatter_matrix_px.html')