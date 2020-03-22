import timeit
import googleSearch
import coronaMap
import pandas as pd
import coro

googleSearch = googleSearch.GoogleSearch()
coronaMap = coronaMap.CoronaMap()

countryLatLongMap = {}
with open("countryLatLong.txt") as f:
    for line in f:
       (key, val) = line.split(":")
       countryLatLongMap[key] = val


data = pd.read_csv("covid_19_data.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
countryGroups = data.groupby('Country/Region')
# countryProvinceGroups = data.groupby(['Country/Region','Province/State'])
countryList = data['Country/Region'].unique()
# print(countryGroups['Country/Region'].to_string(index=False))
countryNewsResult = {}
start_time = timeit.default_timer()
print("Time starts now: ")
for country in countryLatLongMap.keys():
    print("\""+country+"\" : " + countryLatLongMap[country])
    googleSearch.searchWithKeyWord("covid-19 coronavirus "+country)
    (latitude, longitude)=countryLatLongMap[country].split(",")
    coronaMap.addToMap(country, float(latitude), float(longitude), googleSearch.searchResult)
coronaMap.saveMap()

elapsedTime = timeit.default_timer() - start_time
print(elapsedTime)
print(countryNewsResult)