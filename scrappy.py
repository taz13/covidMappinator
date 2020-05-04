import timeit

import coronaDataApi
import coronaMap
import googleSearch

googleSearch = googleSearch.GoogleSearch()
coronaMap = coronaMap.CoronaMap()

countryApiCodeMap = {}
with open("coronaCountryCode.txt") as f:
    for line in f:
        (key, val) = line.split(":")
        countryApiCodeMap[key] = val.rstrip()

countryLatLongMap = {}
with open("countryLatLong.txt") as f:
    for line in f:
        (key, val) = line.split(":")
        countryLatLongMap[key] = val.rstrip()
dataApi = coronaDataApi.CoronaApi()

# coronaData = dataApi.getCountryResult("US")
# print(coronaData)
# coronaData = dataApi.getCountryResult("ABC")
# print(coronaData)

start_time = timeit.default_timer()
print("Time starts now: ")
for country in countryLatLongMap.keys():
    print("\"" + country + "\" : " + countryLatLongMap[country])
    coronaData = dataApi.getCountryResult(country)
    googleSearch.searchWithKeyWord("covid-19 coronavirus " + country)
    (latitude, longitude) = countryLatLongMap[country].split(",")
    coronaMap.addToMap(country, float(latitude), float(longitude), googleSearch.searchResult, coronaData)
coronaMap.saveMap()

elapsedTime = timeit.default_timer() - start_time
print("Time elapsed: {} seconds".format(elapsedTime))
