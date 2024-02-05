import pandas as pd
import ml_backend

df = pd.read_csv('simulation_data/C.csv')
for i in range(12):
    for j in ml_backend.analyze_data(df.iloc[i:i+1]):
        print(j)