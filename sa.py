import random 
import statistics
import plotly.figure_factory as ff
import pandas as pd 
import csv
import plotly.graph_objects as go 

df = pd.read_csv("sp.csv")
data = df["reading score"].tolist()
mean = sum(data)/len(data)
std_deviation = statistics.stdev(data)
print(f"mean of the data is : {mean}")
print(f"standard deviation of data is : {std_deviation}")

median = statistics.median(data)
mode = statistics.mode(data)
print(f"median of the data is : {median}")
print(f"mode of the data is : {mode}")
first_sd_start, first_sd_end = mean - std_deviation, mean + std_deviation
second_sd_start, second_sd_end = mean - 2*std_deviation, mean + 2*std_deviation
third_sd_start, third_sd_end = mean - 3*std_deviation, mean + 3*std_deviation

fig = ff.create_distplot([data],["reading score"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0, 0.20], mode = "lines", name = "first std deviation"))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0, 0.20], mode = "lines", name = "first std deviation"))
fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0, 0.20], mode = "lines", name = "second std deviation"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0, 0.20], mode = "lines", name = "second std deviation"))
fig.show()