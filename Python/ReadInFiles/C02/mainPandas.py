import pandas
import matplotlib.pyplot as plt

#read the csv file
FILENAME = "original/temperature_data.csv"
file = pandas.read_csv(FILENAME)
#header=0 means the first line is ignored and they are headers
#file is a dataframe - not a list

# print(file["Anomaly"].sum())
# print(file["Anomaly"].min())
# print(file["Anomaly"].max())

#plot a line graph of the years vs anomalies
plt.plot(file["Year"],file["Anomaly"]) #one line, one command, one graph
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in Temperatures")
# plt.show()

plt.bar(file["Year"],file["Anomaly"], color="green", align="center") #one line, one command, one graph
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in Temperatures")
# plt.show()

#what years were the min and max anomalies
print(file["Year"].loc[file["Anomaly"] == file["Anomaly"].min()])
#     {years[anomalies.index(min(anomalies))]}
print(file["Year"].loc[file["Anomaly"] == file["Anomaly"].min()].values[0])
#this is creating another data frame and values[0] gets the first value out of the frame

#if you had to create a graph or chart for homework 
#things you want to include
# xlabel
# ylabel
# title
# make sure things are spelt correct
