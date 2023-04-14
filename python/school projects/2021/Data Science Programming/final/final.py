import pandas as pd 
import altair as alt
import numpy as np
from altair_saver import save
from pandas.io.formats.format import TextAdjustment

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

class Final:

    def __init__(self):
        self.p1 = Problem_1()
        self.p2 = Problem_2()
        self.p3 = Problem_3()
        self.p4 = Problem_4()
        self.p5 = Problem_5()

    def main(self):
        self.p1.main()  #<-- complete
        #self.p2.main()  #<-- needs chart
        self.p3.main()  #<-- complete
        self.p4.main()  #<-- complete
        #self.p5.main()  #<-- WIP

class Problem_1:

    def __init__(self):
        url = 'https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv'
        self.dat_home = pd.read_csv(url).sample(n=4500, random_state=15)

    def main(self):
        #print(self.dat_home.columns)
        self.refine_data()
        self.create_chart(self.dat_home)

    def refine_data(self):
        #print(self.dat_home['arcstyle'].unique())
        self.dat_home = self.dat_home.query("arcstyle == 'ONE-STORY' or arcstyle == 'TWO-STORY' or arcstyle == 'SPLIT LEVEL'")

    def create_chart(self,data):
        
        chart = alt.Chart(data).mark_point().encode(
            alt.X('yrbuilt:T',title='Year home was built'),
            alt.Y("livearea:Q",title="Square footage of home(log)"),
            alt.Color('arcstyle:N',title="Standard house types")
        )

        chart.title = "Thank goodness the 21st century doesn't have split levels"

        chart_name = "q1.png"
        save(chart,chart_name)

class Problem_2:

    def __init__(self):
        self.mister = pd.Series(["lost",15,22,45,31,"lost",85,38,129,80,21,2])

    def main(self):
        self.refine_data()
        self.create_chart(self.mister)

    def refine_data(self):
        self.mister = self.mister.replace('lost',125)
        data = self.mister.to_numpy()

    def create_chart(self,data):
        
        chart = alt.Chart(data).mark_boxplot(extent='min-max').encode(
            x='index',
            y='value'
        )

        chart_name = "q2.png"
        save(chart,chart_name)

class Problem_3:

    def __init__(self):
        self.mister = pd.Series(["lost",15,22,45,31,"lost",85,38,129,80,21,2])

    def main(self):
        self.refine_data()
        self.find_mean()

    def refine_data(self):
        self.mister = self.mister.replace('lost',125)

    def find_mean(self):
        mean = self.mister.mean()
        print(round(mean,2))

class Problem_4:

    def __init__(self):
        url = 'https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/table1/table1.json'  
        self.data = pd.read_json(url)

    def main(self):
        self.refine_data()
        self.create_table()

    def refine_data(self):
        print(self.data.columns)
        self.data = self.data.drop(columns=['country','year','population'])

    def create_table(self):
        print(self.data.to_markdown())

class Problem_5:

    def __init__(self):
        url = "http://byuistats.github.io/CSE250-Course/data/clean_starwars.csv"
        self.dat = pd.read_csv(url)

    def main(self):
        self.classify()

    def split_data(self):
        data = train_test_split(self.dat,test_size = .20,random_state = 2020)
        self.test_data = data.drop(columns='gender')
        self.key = data.gender


    def classify(self):
        gbc = GradientBoostingClassifier()
        gbc.fit(self.test_data.self.key)


demo = Final()
demo.main()



"""
Code bits

for item in self.mister:
    if item == "lost":
        self.mister[item] = 125

self.data = self.data.drop('country')
self.data = self.data.drop('year')
self.data = self.data.drop('population')



"""