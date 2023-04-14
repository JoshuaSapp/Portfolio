#%%
import pandas as pd   
import altair as alt  
from selenium import webdriver
from altair_saver import save

filename = 'chart.png'
driver = webdriver.Chrome("C:/Users/jaxon/OneDrive/Desktop/Coding Projects/Python/chromedriver/chromedriver_win32/chromedriver")

#%%
alt.data_transformers.enable('json')
alt.renderers.enable('altair_saver', fmts=['png'])
#%%
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)
#%%
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)
chart
#%%
save(chart, "chart.png")
# %%
