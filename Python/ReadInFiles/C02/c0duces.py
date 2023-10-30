import pandas
import matplotlib.pyplot as plt
import math


#read the csv file
FILENAME = "original/temperature_data.csv"
file = pandas.read_csv(FILENAME,header=5)

#if you read in a file and you NaN -> Not a Number
#clean the data remove the -99.99
file["Average"] = file["Average"].replace(-99.99,math.nan)
#clean the data as in remove NaN
file.dropna(subset=['Average'],inplace=True)
# dropna(which column, remove entire line?)

plt.plot(file["decimal_year"],file["Average"])
plt.ylabel("Average co2")
plt.xlabel("Years")
plt.title("Average co2 over time")
plt.show()







