file = open("original/temperature_data.csv","r")
file = file.readlines()

# print(file)

#min and max of the anomalies column
anomalies=[]
years=[]
for row in file:
    data = row.split(",")
    try:
        anomalies.append(float(data[1]))
        years.append(data[0])
    except:
        print(data)
        pass

# print(anomalies)
print(f"min: {min(anomalies)} during the year of {years[anomalies.index(min(anomalies))]}")
print(f"max:{max(anomalies)} during the year of {years[anomalies.index(max(anomalies))]}")