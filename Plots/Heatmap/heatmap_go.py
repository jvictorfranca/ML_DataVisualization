import pandas as pd
import numpy as np
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default='browser'

dados_paises = pd.read_csv('Datasets/dados_paises.csv')
paises = dados_paises.drop(columns=['country'])
corr = paises.corr()

# Gráfico de calor (heatmap)
fig = go.Figure()

fig.add_trace(
    go.Heatmap(
        x = corr.columns,
        y = corr.index,
        z = np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}',
        colorscale='viridis'))

fig.update_layout(
    height = 600,
    width = 600)

fig.show()