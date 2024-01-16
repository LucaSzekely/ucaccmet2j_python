#1.1.2 station code of seattle: GHCND:US1WAKG0038 --> select measurements from json
import json
from json import load

with open('.\\ucaccmet2j_python\precipitation.json', encoding ='utf - 8') as file:
        percipitation = json.load(file)
#print(percipitation)

Seatle_list = []
for Seatle in percipitation:
    station = Seatle["station"]
    if station == "GHCND:US1WAKG0038":
           Seatle_list.append(Seatle)
    else: station = ""
#print(Seatle_list) 

#1.1.3 calculate total_monthly_precipitation: add values up

#total_precipitation = 0
#for all in Seatle_list:
#      value = all["value"]
#      if 'value' in all:
#            total_precipitation = total_precipitation + value
#      else: total_precipitation = 0
#print(total_precipitation) 
#output: 11180
    
total_monthly_precipitation = 0
monthly_Jan = []
#i have a list of dictionaries, and I want to sort them by month
#Total for Jan
# month: if >10 add 0 at begining
total_precipitation_Jan = 0
number = 0
month_list = [0,0,0,0,0,0,0,0,0,0,0,0]

for Jan in Seatle_list:
      date = str(Jan["date"])
      new_date = date.split(sep = '-')
      month = int(new_date[1])
      value_Jan = Jan["value"]
      month_list[month-1] = month_list[month-1] + value_Jan
print (month_list)

with open ('results.json', 'w') as file:
    json.dump(month_list,file)