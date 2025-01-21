import statsmodels.api as sm
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd

df_tempodist = pd.read_csv('Datasets/tempodist.csv', delimiter=',')

x = df_tempodist['distancia']
y = df_tempodist['tempo']

# Define regression
slope, intercept = np.polyfit(x, y, 1)
y_trend = slope * x + intercept

fig = go.Figure()

# Intercept
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(color='navy', size=20), name='Valores Reais')
    )

# Inserção da reta (fitted values)
fig.add_trace(go.Scatter(
    x=x,
    y=y_trend,
    mode='lines',
    line=dict(color='dimgray', width=5), name='Fitted Values')
    )

# Configurações de layout
fig.update_layout(
    xaxis_title='Distância',
    yaxis_title='Tempo',
    title={
        'text': 'Gráfico de Dispersão com Fitted Values',
        'font': {'size': 20, 'color': 'black', 'family': 'Arial'},
        'x': 0.5,
        'y': 0.97,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    plot_bgcolor='snow',
    xaxis=dict(gridcolor='black'),
    yaxis=dict(gridcolor='black'),
    showlegend=True
)

fig.write_html('EXEMPLO1.html')

# open on webbrowser
import webbrowser
webbrowser.open('EXEMPLO1.html')