# Descriptive Statistics
# Weihua Li

# About the script:
# This is a simple script that reads in an csv and plots a histgram about a column that has numbers.
# It will also plot mean and median and 1QR and 2 QR and all the good stuff.

# Here is the plan
# 1. read in the file and save the average payment column into a linestyle
# 2. calculate the measurements related to mean and median
# 3. print the measurements in the terminal
# 4. build a histgram that shows these measurements

# import libraries
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics
import matplotlib.patches as mpatches

# pull in the data
filename = input("Type your filename, including the extension (.csv etc)")
data_file = open(filename, "rU")

column_name = input("Type which column you want to plot")

# convert to DictReader
data_reader = csv.DictReader(data_file)

# create an empty list that will have all the data that you want to plot
# I used "data" for variable name so I can reuse this script
data = []

# for every row in the csv, pull out the desired value, save that to the data list
for row in data_reader:
    data.append(float(row[column_name]))

# calculate mean
data_mean = statistics.mean(data)

# calculate standard deviation
data_std = np.std(data )

# build a list that has mean, mean-2sd, mean-3sd, mean-1sd, mean+1sd, mean+2sd and mean+3sd
mean_measures = [data_mean]
for i in range(4):
    mean_measures.append(data_mean + (i*data_std))
    mean_measures.append(data_mean - (i*data_std))

# calculate the quartiles
data_quartiles = np.percentile(data, [25, 50, 75])

# calculate the upper and lower bounds
# IQR = third quartile - first quartile
iqr = data_quartiles[2] - data_quartiles[0]
# upper bound = third quartile + IQR
data_upper_bound = data_quartiles[2] + (1.5*iqr)
# lower bound = first quartile - IQR
data_lower_bound = data_quartiles[0] - (1.5*iqr)

# print the measurements in terminal
print("Max: ", max(data))
print("Min: ", min(data))
print("--------------------------")
print("Mean: ", data_mean)
print("SD: ", data_std)
print("Mean - 1SD: ", data_mean-data_std)
print("Mean - 2SD: ", data_mean-(2*data_std))
print("Mean - 3SD: ", data_mean-(3*data_std))
print("Mean + 1SD: ", data_mean+data_std)
print("Mean + 2SD: ", data_mean+(2*data_std))
print("Mean + 3SD: ", data_mean+(3*data_std))
print("--------------------------")
print("Median: ", data_quartiles[1])
print("Q1: ", data_quartiles[0])
print("Q3: ", data_quartiles[2])
print("Lower Bound: ", data_lower_bound)
print("Upper Bound: ", data_upper_bound)

# plot the histogram of average medicare payment
plt.figure(figsize=(15, 10))
my_hist = plt.hist(data, histtype="bar", color="#ff7f00")

# plot quartile lines
plt.vlines(data_quartiles, 0, 1600, color=["#fb9a99"], linestyle="dashed", linewidth=2)

# # plot upper and lower bounds
plt.vlines(data_upper_bound, 0, 1600, color=["#fb9a99"], linestyle="dashed", linewidth=2)
plt.vlines(data_lower_bound, 0, 1600, color=["#fb9a99"], linestyle="dashed", linewidth=2)

# plot the mean lines
plt.vlines(mean_measures, 0, 1600, color=["green"], linestyle="dashed", linewidth=2)

# create a very basic legend
green = mpatches.Patch(color="green", label="mean and related measures")
pink = mpatches.Patch(color="#fb9a99", label="median and related measure")

plt.legend(handles=[green, pink])

# make the graph show up
plt.show()

# Questions:
# What are the outliers? What are the type of services they provide?
# If I do a stacked histogram that shows psychiatrist from different boroughs, will I spot any other trends?
