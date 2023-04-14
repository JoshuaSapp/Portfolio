from altair.vegalite.v4.schema.channels import Color
from altair_saver import save
import pandas as pd
import altair as alt

df = pd.read_csv('life-expectancy.csv')
print(df)

#What is the year and country that has the lowest life expectancy in the dataset?
me = df['Life expectancy (years)'].min()
me_row = df[df['Life expectancy (years)'] == me]
#print(me_row)

#What is the year and country that has the highest life expectancy in the dataset?
me = df['Life expectancy (years)'].max()
me_row = df[df['Life expectancy (years)'] == me]
#print(me_row)

#Allow the user to type in a year, then, find the average life expectancy for that year. 
#Then find the country with the minimum and the one with the maximum life expectancies for that year.
year = int(input("Please input a year:  "))
ydf = df[df['Year'] == year]

me = ydf['Life expectancy (years)'].max()
me_row1 = ydf[ydf['Life expectancy (years)'] == me]
#print(me_row1)

me = ydf['Life expectancy (years)'].min()
me_row2 = ydf[ydf['Life expectancy (years)'] == me]
#print(me_row2)

print(f"In {year}, {me_row1['Entity'].unique()[0]} had the highest life expectancy at {me_row1['Life expectancy (years)'].unique()[0]} years,\nwhile {me_row2['Entity'].unique()[0]} had the lowest life expectancy at {me_row2['Life expectancy (years)'].unique()[0]} years")

chart = alt.Chart(title="life expectancy over years")
countries = df['Entity'].unique()

for country in countries:
    chart_data = df[df['Entity']==country]
    chart = alt.Chart(chart_data).mark_line().encode(alt.X('Year'),alt.Y('Life expectancy (years)'))
    name = f"chart for {country}.png"
    save(chart,name)

