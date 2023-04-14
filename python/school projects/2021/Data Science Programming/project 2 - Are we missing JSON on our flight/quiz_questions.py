import pandas as pd
import numpy as np

df = pd.read_json('flights_missing.json')


def count_nan(df):
    pdf = df.to_dict("records")
    nans = 0
    for record in pdf:
        if record['month'] not in ['January','February','March','April','June','July','August','September','October','November','December']:
            nans+=1

    print(nans)


def find23(df):
    pdf = df.to_numpy()
    for item in pdf:
        count = np.nan(item)
        print(count)

find23(df)


