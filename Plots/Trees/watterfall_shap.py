import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import shap
import matplotlib.pyplot as plt

df = pd.read_csv('Datasets/houses_to_rent.csv', index_col=0)

print(df.info())

# Treat database columns

df['property tax'] = df['property tax']

df['floor'] = df.floor.str.replace('-','NaN').astype('float64')
for var in ['hoa', 'rent amount', 'property tax', 'fire insurance', 'total']:
    df[var] = df[var].str.replace('R$','')\
        .str.replace(',','')\
        .str.replace('Sem info','NaN')\
        .str.replace('Incluso','0').astype('float64')
        
print(df.info())

X_cols = ['city', 'area', 'rooms', 'bathroom', 'parking spaces', 'floor', 'animal', 'furniture']
y_col = 'total'

X = pd.get_dummies(df[X_cols], drop_first=True)
y = df[y_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

rf = RandomForestRegressor()
rf.fit(X, y)

r2_score(y_test, rf.predict(X_test))
print(r2_score)

df['pred'] = rf.predict(X)

amostra = X_test.sample(frac=0.1)

explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(amostra)

#%% Waterfall for a register
shap.waterfall_plot(shap.Explanation(values=shap_values[0], 
                                     base_values=explainer.expected_value, 
                                     data=amostra.iloc[0], 
                                     feature_names=amostra.columns))

# #%% Forceplot
# # Inicializar a visualização
# shap.initjs()

# # Explicação no nível de indivíduo (force plot para a primeira amostra de teste)
# force_plot = shap.force_plot(explainer.expected_value, 
#                 shap_values[0], 
#                 amostra.iloc[0], 
#                 feature_names=amostra.columns)
# plt.show()

# # Este não mostra no console, vamos salvar em arquivo
# shap.save_html("force_plot.html", force_plot)
