import pandas as pd
import plotly.express as px 
import plotly.io as pio
from sklearn.cluster import KMeans
from scipy.stats import zscore

pio.renderers.default='browser'

dados_cartao = pd.read_csv('Datasets/cartao_credito.csv')
print(dados_cartao.info())

cartao_cluster = dados_cartao.drop(columns=['Sl_No', 'Customer Key'])
cartao_pad = cartao_cluster.apply(zscore, ddof=1)


kmeans_final = KMeans(n_clusters = 3, init = 'random', random_state=100).fit(cartao_pad)

# Gerando a variável para identificarmos os clusters gerados

kmeans_clusters = kmeans_final.labels_
cartao_cluster['cluster_kmeans'] = kmeans_clusters
cartao_cluster['cluster_kmeans'] = cartao_cluster['cluster_kmeans'].astype('category')


fig = px.scatter_3d(cartao_cluster, 
                    x='Avg_Credit_Limit', 
                    y='Total_Credit_Cards', 
                    z='Total_visits_online',
                    color='cluster_kmeans')
fig.show()