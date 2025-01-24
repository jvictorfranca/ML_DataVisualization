from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

# Função 'roc_curve' do pacote 'metrics' do sklearn

df_atrasado = pd.read_csv('Datasets/atrasado.csv')
print(df_atrasado)

# Características das variáveis do dataset
print(df_atrasado.info())

# Estatísticas univariadas
print(df_atrasado.describe())

modelo_atrasos = smf.glm(formula='atrasado ~ dist + sem', data=df_atrasado,family=sm.families.Binomial()).fit()
print(modelo_atrasos)

df_atrasado['phat'] = modelo_atrasos.predict()
print(df_atrasado)

# Parâmetros do 'modelo_atrasos'
print(modelo_atrasos.summary())

fpr, tpr, thresholds = roc_curve(df_atrasado['atrasado'], df_atrasado['phat'])
roc_auc = auc(fpr, tpr)

# Cálculo do coeficiente de GINI
gini = (roc_auc - 0.5)/(0.5)

# Plotando a curva ROC
plt.figure(figsize=(15,10))
plt.plot(fpr, tpr, marker='o', color='darkorchid', markersize=10, linewidth=3)
plt.plot(fpr, fpr, color='gray', linestyle='dashed')
plt.title('Área abaixo da curva: %g' % round(roc_auc, 4) +
          ' | Coeficiente de GINI: %g' % round(gini, 4), fontsize=22)
plt.xlabel('1 - Especificidade', fontsize=20)
plt.ylabel('Sensitividade', fontsize=20)
plt.xticks(np.arange(0, 1.1, 0.2), fontsize=14)
plt.yticks(np.arange(0, 1.1, 0.2), fontsize=14)
plt.show()