import numpy as np
import pandas as pd
import altair as alt
from altair_saver import save

class What_is_in_a_name:

    def main(self):
        self.settup()
        self.q1()
        self.q2()
        self.q3()
        self.q4()

    def settup(self):
        #do any needed initilizing
        self.data = pd.read_csv("names_year.csv")
        #alt.data_transformers.enable('json')

    def q1(self):
        #How does your name at your birth year compare to its use historically?

        #Refines dataset to contain only relevant data
        q1_data = self.data.query("name == 'Joshua'& year <= 2015 & year >= 1960")

        #Generates Table using given data
        chart = (alt.Chart(q1_data,title = 'Joshua as a name historic usage')
            .encode(
                x= 'year:O',
                y='Total')
            .mark_bar()
            )


        save(chart, "q1.png")

    def q2(self):
        #If you talked to someone named Brittany on the phone, what is your guess of their age? What ages would you not guess?
        q2_data = self.data.query("name == 'Brittany'")
        chart = (alt.Chart(q2_data,title="Brittany as a name historic useage")
            .encode(
                x= 'year:O',
                y='Total')
            .mark_bar()
            )

        save(chart, "q2.png")

    def q3(self):
        #Mary, Martha, Peter, and Paul are all Christian names. From 1920 - 2000, compare the name usage of each of the four names.
        q3_data1 = self.data.query("name == 'Martha' & year <= 2000 & year >= 1920")
        q3_data2 = self.data.query("name == 'Peter' & year <= 2000 & year >= 1920")
        q3_data3 = self.data.query("name == 'Paul' & year <= 2000 & year >= 1920")
        q3_data4 = self.data.query("name == 'Mary' & year <= 2000 & year >= 1920")

        chart1 = (alt.Chart(q3_data1,title= "Mary, Martha, Peter, and Paul name usage between 1920 to 2000")
            .encode(
                alt.X('year:O'),
                y='Total',
                color =alt.Color('name',legend=alt.Legend(title="names")))
            .mark_line()
            )

        chart2 = (alt.Chart(q3_data2)
            .encode(
                alt.X('year:O'),
                y='Total',
                color =alt.Color('name',legend=alt.Legend(title="names")))
            .mark_line()
            )

        chart3 = (alt.Chart(q3_data3)
            .encode(
                alt.X('year:O'),
                y='Total',
                color =alt.Color('name',legend=alt.Legend(title="names")))
            .mark_line()
            )

        chart4 = (alt.Chart(q3_data4)
            .encode(
                alt.X('year:O'),
                y='Total',
                color =alt.Color('name',legend=alt.Legend(title="names")))
            .mark_line()
            )

        chart = chart1 + chart2 + chart3 + chart4

        filename = 'q3.png'
        save(chart, filename)

    def q4(self):
        #Think of a unique name from a famous movie. Plot that name and see how increases line up with the movie release.
        q4_data = self.data.query("name == 'Jackson' & year <= 2015 & year >= 1980")
        chart = (alt.Chart(q4_data,title="Jackson as a name historic useage")
            .encode(
                x= 'year:O',
                y='Total')
            .mark_bar()
            )

        save(chart, "q4.png")

w = What_is_in_a_name()
w.main()


