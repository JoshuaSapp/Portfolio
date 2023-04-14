import altair as alt
from altair_saver import save
import pandas as pd

def convert_f_to_c(temp):
    return((temp-32)*(5/9))

def convert_c_to_f(temp):
    return((temp*(9/5))+32)

def find_chill(temp,units):
    if units != "f" and units!= "c":
        return("error: Units must either be in Celsius (c) or Fahrenheit (f).")
    else:
        if units == "c":
            temp = convert_c_to_f(temp)
        entries = 12
        x = 5
        x_axis = []
        y_axis = []
        while entries > 0:
            x_axis.append(x)
            w_chill = round(35.74 + (0.6215*temp) - 35.75*(pow(x,0.16)) + (0.4275*temp)*(pow(x,0.16)),2)
            if units == "c":
                w_chill = convert_f_to_c(w_chill)
            y_axis.append(w_chill)
            x += 5
            entries -= 1

        data = pd.DataFrame({"wind_speed": x_axis,f"Temperature ({units})":y_axis})

        print(data)

        chart = alt.Chart(data).mark_line().encode(
            alt.X("wind_speed:Q",title="Wind Speed (MPH)"),
            alt.Y(f"Temperature ({units}):Q",title = f"Temperature ({units})")
        )

        save(chart,"temprature chart.png")

temp = float(input("What is the temperature?    "))
units = input("Fahrenheit or Celsius? (F/C)   ")

units = units.lower()

find_chill(temp,units)
