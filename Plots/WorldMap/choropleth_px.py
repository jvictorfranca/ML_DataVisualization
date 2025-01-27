import pandas as pd
import plotly.express as px
import webbrowser


df_corruption = pd.read_csv('Datasets/corruption.csv', delimiter=',')

# Mapa-múndi  https://plotly.com/python/choropleth-maps/
fig = px.choropleth(df_corruption, 
                    locations='code',  # Código ISO dos países
                    color='corruption',
                    hover_name='country',  # Informações que aparecerão ao passar o mouse
                    color_continuous_scale=px.colors.sequential.RdBu_r,  # Escala de cores
                    projection="natural earth",  # Projeção do mapa
                    title="Mapa de Corrupção por País")

fig.write_html("mapa_corrupcao.html")

webbrowser.open("mapa_corrupcao.html")