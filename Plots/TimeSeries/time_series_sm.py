import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


queimadas = pd.read_excel("Datasets/queimadas.xlsx")
queimad = pd.Series(queimadas['focos'].values, 
                index=pd.date_range(start='1999-01-01', 
                                    periods=len(queimadas), freq='M'))


sm.graphics.tsa.month_plot(queimad)

plt.show()
