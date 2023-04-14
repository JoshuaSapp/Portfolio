#%%
import pandas as pd
import datadotworld as dw
import altair as alt
from altair_saver import save

class Finding_Relationships_in_Baseball:

    def main(self):
        self.settup()
        self.q1()
        self.q2()
        self.q3()

    def settup(self):
        #do any needed initializing
        #alt.data_transformers.enable('json')
        pass

    def q1(self):
        """
        Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. 
        The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. 
        Order the table by salary (highest to lowest) and print out the table in your report.
        """

        request = dw.query('byuidss/cse-250-baseball-database', 
            "select sa.playerid, s.schoolid, sa.salary, sa.teamid, sa.yearid from salaries as sa join collegeplaying as c on sa.playerid = c.playerid join schools as s on c.schoolid = s.schoolid WHERE s.name_full = 'Brigham Young University-Idaho' order by sa.salary DESC")

        print(request.dataframe)

    def q2(self):
        """
        This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)

        a: Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from 
            highest batting average to lowest, and show the top 5 results in your report.
        
        b: Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.

        c: Now calculate the batting average for players over their entire careers (all years combined). 
        Only include players with more than 100 at bats, and print the top 5 results.
        """
        request1 = dw.query('byuidss/cse-250-baseball-database', 
                    "SELECT p.playerid,b.yearid ,(b.h/b.ab) AS batting_Average FROM people AS p JOIN batting as b on p.playerid = b.playerid WHERE b.ab >= 1 ORDER BY batting_Average DESC LIMIT 5")        
        print(request1.dataframe)     

        request2 = dw.query('byuidss/cse-250-baseball-database', 
                    "SELECT p.playerid,b.yearid ,(b.h/b.ab) AS batting_Average FROM people AS p JOIN batting as b on p.playerid = b.playerid WHERE b.ab > 10 ORDER BY batting_Average DESC LIMIT 5")        
        print(request2.dataframe)          

        request3 = dw.query('byuidss/cse-250-baseball-database', 
                    "SELECT p.playerid,(b.h/b.ab) AS batting_Average FROM people AS p JOIN batting as b on p.playerid = b.playerid WHERE b.ab > 100 GROUP BY p.playerid ORDER BY batting_Average DESC LIMIT 5")        
        print(request3.dataframe)                    



    def q3(self):
        """
        Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). 
        Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to 
        visualize the comparison. Provide the visualization and its description.
        """
        request1 = dw.query('byuidss/cse-250-baseball-database',
                    "select tf.franchname, s.yearid as year, avg(s.salary) from salaries as s JOIN teams as t on s.teamid = t.teamid JOIN teamsfranchises as tf on t.franchid = tf.franchid WHERE tf.franchname = 'Washington Nationals' group by s.yearid")
        request2 = dw.query('byuidss/cse-250-baseball-database',
                    "select tf.franchname, s.yearid as year, avg(s.salary) from salaries as s JOIN teams as t on s.teamid = t.teamid JOIN teamsfranchises as tf on t.franchid = tf.franchid WHERE tf.franchname = 'New York Mets' group by s.yearid")
        
        chart1 = (alt.Chart(request1.dataframe,title= "NY Mets Vs. Washington nationals: Average Salary By Year")
            .encode(
                x='year',
                y='avg',
                color =alt.Color('franchname',legend=alt.Legend(title="Team Franchise")))
            .mark_line()
            )

        chart2 = (alt.Chart(request2.dataframe)
            .encode(
                x='year',
                y='avg',
                color =alt.Color('franchname',legend=alt.Legend(title="Team Franchise")))
            .mark_line()
            )

        chart = chart1 + chart2
        filename = "q3 chart.png"
        save(chart,filename)

f = Finding_Relationships_in_Baseball()
f.main()



# %%
