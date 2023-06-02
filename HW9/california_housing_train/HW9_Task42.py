# Узнать какая максимальная households в зоне минимального значения population.


import pandas as pd

df = pd.read_csv('california_housing_train.csv')
print(df.loc[df.population < df.population.quantile(0.15)].households.max())

