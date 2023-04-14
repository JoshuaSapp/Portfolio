from re import split
from altair.vegalite.v4.schema.channels import Color
import pandas as pd
import numpy as np
import altair as alt
from altair_saver import save
from sklearn.naive_bayes import GaussianNB
import os

HOME_DIRECTORY = os.getcwd()

# Overall goal:  
    # Write code that can predict a homes actual age, as well as classify homes that are built pre 1980

# Grand Questions:

    # 1. Create 2-3 charts that evaluate potential relationships between the home variables and before1980.  -done, can be inproved

    # 2. Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state  
    # of Colorado to use (explain your model choice and which models you tried)? -done with 76% accuricy, need to inprove

    # 3. Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?

    # 4. Can you describe the quality of your classification model using 2-3 evaluation metrics? 
    #You need to provide an interpretation of each evaluation metric when you provide the value.


class Main():

    def __init__(self):
        df = pd.read_csv("dwellings_denver.csv")
        df.loc[df.yrbuilt > 1980, 'target'] = "after 1980"
        df.loc[df.yrbuilt <= 1980, 'target'] = "during or before 1980"
        self.data = df
        
    def main(self):
        self.prepForOutput()
        #self.q1()
        self.q2()
        self.q3()
        self.q4()

         
    def prepForOutput(self):
        #creates a folder to save graphs to in working directory
        if not os.path.exists(f'{HOME_DIRECTORY}/program outputs'):
            os.mkdir(f'{HOME_DIRECTORY}/program outputs')
        os.chdir(f'{HOME_DIRECTORY}/program outputs')

    def create_and_save_table(self,data,x_metric,y_metric,table_type,table_name = None,key_metric = None,key_name = None):

        if table_type == "line":
            chart = (alt.Chart(data,title= table_name)
                .encode(
                    x=x_metric,
                    y=y_metric,
                    color =alt.Color(key_metric,legend=alt.Legend(title=key_name)))
                .mark_line()
                )
        
        if table_type == "bar":
            chart = (alt.Chart(data,title= table_name)
                .encode(
                    x=x_metric,
                    y=y_metric,
                    color =alt.Color(key_metric,legend=alt.Legend(title=key_name)))
                .mark_bar()
                )

        if table_type == "point":
            chart = (alt.Chart(data,title= table_name)
                .encode(
                    x=x_metric,
                    y=y_metric,
                    color =alt.Color(key_metric,legend=alt.Legend(title=key_name)))
                .mark_point()
                )

    def create_sample_tables(self):

        chart = (alt.Chart(self.data,title= "floors by year")
            .encode(
                x="yrbuilt",
                y="stories",
                color =alt.Color('franchname',legend=alt.Legend(title="Team Franchise"))
                )
            .mark_point()
            )

        name = "floors by year.png"
        save(chart,name)

    def split_data(self,data,test_size):
        # takes in a given test size percentage (.3 or .5 for example) and returns a list containing the two datasets with [0] 
        # containing the train data and [1] containing the test data
        test_data = data.sample(frac=test_size)
        train_data = data.drop(test_data.index)
        return([train_data,test_data])

    def classify(self,data,test_percent,target,data_columns):

        split = self.split_data(data,test_percent)

        train_data = split[0][data_columns]
        test_data = split[1][data_columns]
        train_targets = split[0][target]
        test_targets = split[1][target]

        train_data = train_data.to_numpy(na_value = 0)
        test_data = test_data.to_numpy(na_value = 0)
        train_targets = train_targets.to_numpy(na_value = 0).ravel()
        test_targets = test_targets.to_numpy(na_value = 0).ravel()

        # classify data
        classifier = GaussianNB()
        classifier.fit(train_data, train_targets)
        targets_predicted = classifier.predict(test_data)

        return([targets_predicted,test_targets])

    def q1(self):
        
        sample = self.split_data(self.data,5000/len(self.data))
        domain = [1850,2021]
        range_ = ['red', 'green']


        chart = alt.Chart(sample[1]).mark_point().encode(
            alt.X(alt.repeat("column"), type='quantitative'),
            alt.Y(alt.repeat("row"), type='quantitative'),
            alt.Color('target',type='quantitative',title="Year Built",scale=alt.Scale(domain=domain, range=range_))
        ).properties(
            width=150,
            height=150
        ).repeat(
            row=['livearea','stories','sprice'],
            column=['sprice','stories','livearea'],
        )

        chart.title = "Comparison of Denver Housing attributes"

        chart_name = "q1 bonus.png"
        save(chart,chart_name)

        sample = self.split_data(self.data,2500/len(self.data))

        chart = alt.Chart(sample[0]).mark_bar().encode(
        alt.X("livearea:Q", bin=True),
        y='count()',
        color = 'target:Q'
        )

        chart_name = "q1.png"
        save(chart,chart_name)

        # NOTE FOR FUTURE ME:  Big chart is working, though if we can summmarize the points to be averages for alll pre/post 1980 dates that would be great.

    def q2(self):
        total_success_count = 0
        total_guesses = 0
        runs = 1000 # 72.6% after 1000 runs

        while runs != 0:
            success_count = 0
            results = self.classify(self.data,.3,['target'],['nbhd','livearea','finbsmnt','basement','totunits','stories','nocars','floorlvl','numbdrm','numbaths','sprice','deduct','netprice','tasp','syear'])

            #print(list(results[1]))
            #print(list(results[0]))

            guesses = list(results[0])
            key = list(results[1])

            index = 0
            for value in guesses:
                if guesses[index] == key[index]:
                    success_count += 1
                index += 1

            total_guesses += len(guesses)
            total_success_count += success_count
            runs -= 1

        percent_accuracy = round((total_success_count/total_guesses)*100,1)

        print(f"Accuracy: {percent_accuracy}% ({total_success_count}/{total_guesses})")
    
    def q3(self):
        pass

    def q4(self):
        pass

    

m = Main()
m.main()





