import pandas as pd


data = pd.read_csv('names_year.csv')

def q1():
    d1 = data.query("name == 'Oliver'")
    total = sum(d1['UT'])
    print(total)

def q2():
    d2 = data.query("name == 'Felisha'")
    year = min(d2['year'])
    print(year)

q2()