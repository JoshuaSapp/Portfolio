from altair.vegalite.v4.schema.channels import Color
import pandas as pd
import altair as alt
import os

HOME_DIRECTORY = os.getcwd()

class Main():

    def main(self):
        self.data = pd.read_json('data.json')
        self.prepForOutput()
        self.Q1()
        #self.Q2()
        #self.Q3()
        #self.Q4()
        #self.Q5()
         
    def Q1(self):
        # Which airport has the worst delays?  How do you define 'worst' include table that lists total 
        # number of flights, total number of delayed flights, proportion of delayed flights, and 
        # average delay time in hours for each airport.

        # "worst Delays" is defined as having the highest average delay time per flight: (score = (delay time/delayed flights)/total flights)  with a low score being good.

        self.airportCodeList = self.data['airport_code'].unique()

        reportList = []
        report = {}
        for airport in self.airportCodeList:
            
            airportData = self.data.query(f"airport_code == '{airport}'")
            airportDelayScore = (airportData['minutes_delayed_total'].sum()/airportData['num_of_delays_total'].sum())/airportData['num_of_flights_total'].sum()


            airportDelayScore = airportDelayScore*100000
            totalFlights = airportData['num_of_flights_total'].sum()/100000
            totalDelays = airportData['num_of_delays_total'].sum()/100000
            delayRatio = airportData['num_of_delays_total'].sum()/airportData['num_of_flights_total'].sum()
            hoursDelayed = (airportData['minutes_delayed_total'].sum()/60)/100000

            report = pd.DataFrame({
                f'{airport}': ['total flights (x 100,000)', 'total delays (x 100,000)', 'delay ratio','hours delayed (x 100,000)','delay score'],
                'y': [totalFlights,totalDelays,delayRatio,hoursDelayed,airportDelayScore]
                })

            chart = alt.Chart(report).mark_bar().encode(
                x= f'{airport}',
                y='y',
            )    

            chart.save(f"{HOME_DIRECTORY}/program outputs/Q1{airport}chart.png")

    def Q2(self):
        # What is the worst month to fly if you want to avoid delays? 
        # Include one chart to help support your answer, with the x-axis ordered by month. 
        # You also need to explain and justify how you chose to handle the missing Month data.





        chart.save(f"{HOME_DIRECTORY}/program outputs/Q2chart.png")

    def Q3(self):
        # According to the BTS website the Weather category only accounts for severe weather delays.
        # Other “mild” weather delays are included as part of the NAS category and the Late-Arriving 
        # Aircraft category. Calculate the total number of flights delayed by weather 
        # (either severe or mild) using these two rules:
        # - 30% of all delayed flights in the Late-Arriving category are due to weather.
        # - From April to August, 40% of delayed flights in the NAS category are due to weather. 
        # The rest of the months, the proportion rises to 65%.




        chart.save(f"{HOME_DIRECTORY}/program outputs/Q3chart.png")

    def Q4(self):
        #Create a barplot showing the proportion of all flights that are delayed by weather at each airport. 
        # What do you learn from this graph (Careful to handle the missing Late Aircraft data correctly)?





        chart.save(f"{HOME_DIRECTORY}/program outputs/Q4chart.png")

    def Q5(self):
        #Fix all of the varied NA types in the data to be consistent and save the file back out in the same format 
        # that was provided (this file shouldn’t have the missing values replaced with a value). Include one record 
        # example from your exported JSON file that has a missing value (No imputation in this file).





        chart.save(f"{HOME_DIRECTORY}/program outputs/Q5chart.png")


    def prepForOutput(self):
        #creates a folder to save graphs to in working directory
        if not os.path.exists(f'{HOME_DIRECTORY}/program outputs'):
            os.mkdir(f'{HOME_DIRECTORY}/program outputs')
        os.chdir(f'{HOME_DIRECTORY}/program outputs')

m = Main()
m.main()