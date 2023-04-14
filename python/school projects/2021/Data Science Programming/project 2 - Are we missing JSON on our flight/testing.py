import pandas as pd

df = pd.read_json('flights_missing.json')
pdf = df.to_dict('records')

for row in pdf:
    print(row)