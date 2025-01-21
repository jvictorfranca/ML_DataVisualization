
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
import plotly.io as pio
import pandas as pd

pio.renderers.default='browser'

dados_vest = pd.read_excel('Datasets/vestibular.xlsx')


print(dados_vest.info())
dados_vest.describe()

vest = dados_vest.drop(columns=['estudante'])

dist_euclidiana = pdist(vest, metric='euclidean')
# Options for distances ("metric"):
    ## euclidean
    ## sqeuclidean
    ## cityblock
    ## chebyshev
    ## canberra
    ## correlation

# Generating dendogram with euclidian distance


plt.figure(figsize=(16,8))
dend_sing = sch.linkage(vest, method = 'single', metric = 'euclidean')
dendrogram_s = sch.dendrogram(dend_sing, color_threshold = 4.5, labels = list(dados_vest.estudante))
plt.title('Dendrograma', fontsize=16)
plt.xlabel('Pessoas', fontsize=16)
plt.ylabel('Distância Euclidiana', fontsize=16)
plt.axhline(y = 4.5, color = 'red', linestyle = '--')
plt.show()