import pandas as pd
import matplotlib.pyplot as plt

#read in our data
df = pd.read_csv("Original/elec_access_data.csv",header=0)

#how many countries are represented
#how many unique name are in file
uniqueCountries = df.Entity.unique()
print(uniqueCountries)
print(len(uniqueCountries))

#collect graph info
#add each country but group together their access data
myCountries=["Fiji","Vanuatu","Thailand","Cambodia","Iran"]
for uc in uniqueCountries:
    if uc in myCountries:
        years=df[df["Entity"]==uc]["Year"]
        
        electricityAccess = df[df["Entity"]==uc]["Access"]
        
        plt.plot(years,electricityAccess,label=uc)

plt.ylabel("Percentage of Country Population")
plt.xlabel("Years")
plt.title("Percent of Population with Access to Electricity")
plt.legend()
plt.show()