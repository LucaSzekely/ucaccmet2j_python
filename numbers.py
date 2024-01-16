#total for 1 location
#Seatle_list = []
#for Station in percipitation:
#    station = Station["station"]
 #   if station == "GHCND:US1WAKG0038":
  #         Seatle_list.append(Station)
   # else: station = ""

#total_precipitation = 0
#for all in Seatle_list:
#      value = all["value"]
 #     if 'value' in all:
  #          total_precipitation = total_precipitation + value
   #   else: total_precipitation = 0
#print(total_precipitation) 
#output: 11180

import json
from json import load

with open('.\\ucaccmet2j_python\precipitation.json', encoding ='utf - 8') as file:
        percipitation = json.load(file)




Seatle_list = []
for Seatle in percipitation:
    station = Seatle["station"]
    if station == "GHCND:US1WAKG0038":
           Seatle_list.append(Seatle)
    else: station = ""
total_precipitation = 0
for all in Seatle_list:
      value = all["value"]
      if 'value' in all:
            total_precipitation = total_precipitation + value
      else: total_precipitation = 0
print(total_precipitation) 

month_list = [0,0,0,0,0,0,0,0,0,0,0,0]
for Jan in Seatle_list:
      date = str(Jan["date"])
      new_date = date.split(sep = '-')
      month = int(new_date[1])
      value_Jan = Jan["value"]
      month_list[month-1] = month_list[month-1] + value_Jan
print (month_list)

count = -1
value_monthly = []
for devided in month_list:
      count = count + 1
      (value_monthly).append(month_list[count]/total_precipitation) 
print(value_monthly)