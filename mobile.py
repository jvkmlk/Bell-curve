
import csv
import pandas as p
import plotly.figure_factory as pf

data = p.read_csv("mobileBrand.csv")

Plot = pf.create_distplot([data["Avg Rating"].to_list()],["Mobile Graph"],show_hist = False)
Plot.show()