import pandas as pd


userData = {}


# Reading Data from Excel File
# with pd.ExcelFile(file) as xls:
df1 = pd.read_excel("Book1.xlsx", 'Sheet1')
    
# Convert Excel into CSV
toJson = df1.to_csv()

data = toJson.split(',')[3:]
for i in range(len(data)):
    if i %2!= 0 :
        data[i] = data[i].split('\r')[0]

i = 0
while i < len(data):
    userData[data[i]] = (data[i+1].split('\n'))[0]
    i+=2

print(userData)


# print(excelToJson("Book1.xlxs"))