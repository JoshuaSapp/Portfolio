import pandas as pd
import datadotworld as dw
import altair as alt
from altair_saver import save

qr = dw.query('byuidss/cse-250-baseball-database', 
    "select * from batting Limit 2")

q2 = None
qr2 = qr.dataframe
pld = qr2.query("playerid == 'addybo01'")
ab = 118
h = 32

q2 = round(h/ab,3)
#q2 = pld

print("q1")   
print(qr.dataframe)
print()
print("q2")   
print(q2)
print()