file = open("eStoreData.csv","r")
file = file.readlines()

# print(file)

#min and max of the anomalies column
time=[]
ip=[]
email=[]
state=[]
phoneNumber=[]
textNotification=[]
card=[]
cost=[]
department=[]
company=[]

for row in file:
    data = row.split(",")
    try:
        cost.append(float(data[8]))
        department.append(data[9])
    except:
        print(data)
        pass

# print(anomalies)
# print(f"min: {min(anomalies)} during the year of {years[anomalies.index(min(anomalies))]}")
# print(f"max:{max(anomalies)} during the year of {years[anomalies.index(max(anomalies))]}")