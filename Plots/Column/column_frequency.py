import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

titanic = sns.load_dataset('titanic')

# Generates a column chart with the specified variable frequency

def column_with_frequency(df_, var, vresp, max_classes=5):
    
    df = df_.copy()
    
    if df[var].nunique()>max_classes:
        df[var] = pd.qcut(df[var], max_classes, duplicates='drop')
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    sns.pointplot(data=df, y=vresp, x=var, ax=ax1)
    
    # Create second axis
    ax2 = ax1.twinx()
    sns.countplot(data=df, x=var, palette='viridis', alpha=0.5, ax=ax2)
    ax2.set_ylabel('Frequência', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    
    ax1.set_zorder(2)
    ax1.patch.set_visible(False)  # Disable first axes visibility

    plt.show()

print(titanic.head())
print(titanic.columns)

#%%
column_with_frequency(titanic, "sex", 'survived')
column_with_frequency(titanic, "class", 'survived')
column_with_frequency(titanic, "age", 'survived', max_classes=10, )
column_with_frequency(titanic, "fare", 'survived', max_classes=5)
column_with_frequency(titanic,"embarked", 'survived')
column_with_frequency(titanic,"sibsp", 'survived')
column_with_frequency(titanic,"parch", 'survived')