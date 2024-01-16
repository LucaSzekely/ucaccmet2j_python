#2.1 total_yearly_precipitation for each location

import json
from json import load
with open('.\\ucaccmet2j_python\precipitation.json', encoding ='utf - 8') as file:
        percipitation = json.load(file)
#print(percipitation)
        
#GHCND:USW00093814 CI
#GHCND:USC00513317 MA DONE
#GHCND:US1CASD0032 SD DONE
#GHCND:US1WAKG0038 SEATLE DONE
        

#total for 1 location
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

# monthly precipitation
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

#SD
SD_list = []
for SD in percipitation:
    stationSD = SD["station"]
    if stationSD == "GHCND:US1CASD0032":
           SD_list.append(SD)
    else: stationSD = ""
total_precipitationSD = 0

for allSD in SD_list:
      valueSD = allSD["value"]
      if 'value' in allSD:
            total_precipitationSD = total_precipitationSD + valueSD
      else: total_precipitationSD = 0
print(total_precipitationSD) 

month_listSD = [0,0,0,0,0,0,0,0,0,0,0,0]
for SD_again in SD_list:
      dateSD = str(SD_again["date"])
      new_dateSD = dateSD.split(sep = '-')
      monthSD = int(new_dateSD[1])
      value_SD = SD_again["value"]
      month_listSD[monthSD-1] = month_listSD[monthSD-1] + value_SD
print (month_listSD)

countSD = -1
value_monthlySD = []
for devidedSD in month_listSD:
      countSD = countSD + 1
      (value_monthlySD).append(month_listSD[countSD]/total_precipitationSD) 
print(value_monthlySD)

#MA
MA_list = []
for MA in percipitation:
    stationMA = MA["station"]
    if stationMA == "GHCND:USC00513317":
           MA_list.append(MA)
    else: stationMA = ""
total_precipitationMA = 0
for allMA in MA_list:
      valueMA = allMA["value"]
      if 'value' in allMA:
            total_precipitationMA = total_precipitationMA + valueMA
      else: total_precipitationMA = 0
print(total_precipitationMA) 

month_listMA = [0,0,0,0,0,0,0,0,0,0,0,0]
for mo_MA in Seatle_list:
      date = str(mo_MA["date"])
      new_date = date.split(sep = '-')
      month = int(new_date[1])
      value_MA = mo_MA["value"]
      month_listMA[month-1] = month_listMA[month-1] + value_MA
print (month_listMA)

countMA = -1
value_monthlyMA = []
for devidedMA in month_listMA:
      countMA = countMA + 1
      (value_monthlyMA).append(month_listMA[countMA]/total_precipitationMA) 
print(value_monthlyMA)

#CI
CI_list = []
for CI in percipitation:
    stationCI = CI["station"]
    if stationCI == "GHCND:USW00093814":
           CI_list.append(CI)
    else: stationCI = ""
total_precipitationCI = 0

for allCI in CI_list:
      valueCI = allCI["value"]
      if 'value' in allCI:
            total_precipitationCI = total_precipitationCI + valueCI
      else: total_precipitationCI = 0
print(total_precipitationCI) 


month_listCI = [0,0,0,0,0,0,0,0,0,0,0,0]
for mo_CI in CI_list:
      date = str(mo_CI["date"])
      new_date = date.split(sep = '-')
      month = int(new_date[1])
      value_CI = mo_CI["value"]
      month_listCI[month-1] = month_listCI[month-1] + value_CI
print (month_listCI)

countCI = -1
value_monthlyCI = []
for devidedCI in month_listCI:
      countMA = countMA + 1
      (value_monthlyCI).append(month_listCI[countCI]/total_precipitationCI) 
print(value_monthlyCI)

# from here on I would like to make it so stations are automatised