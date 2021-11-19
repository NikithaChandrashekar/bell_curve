import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("bell_curve_data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["average rating"],show_hist=True)
fig.show()