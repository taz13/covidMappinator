import random

import requests


class CoronaApi:
    coronaApiUrl = "https://api.thevirustracker.com/free-api?countryTotals=ALL"
    countryCovidDict = {}

    UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
           "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
           )

    def __init__(self):
        ua = self.UAS[random.randrange(len(self.UAS))]

        respone = requests.get(self.coronaApiUrl, headers={'Accept-Encoding': 'identity', 'user-agent': ua})
        print("status  code: " + str(respone.status_code))
        try:

            jsonResponse = respone.json()
            countryDataKey = 'countryitems'
            if countryDataKey in jsonResponse.keys():
                countryItems = jsonResponse[countryDataKey][0]

                for country in countryItems.keys():
                    if country != 'stat':
                        countryTitle = countryItems[country]['title']
                        self.countryCovidDict[countryTitle] = countryItems[country]
        except Exception as ex:
            print(ex)

    def getCountryResult(self, country):
        coronaData = ['N/A', 'N/A', 'N/A', 'N/A']
        if country in self.countryCovidDict:
            coronaData[0] = self.countryCovidDict[country]['total_cases']
            coronaData[1] = self.countryCovidDict[country]['total_deaths']
            coronaData[2] = self.countryCovidDict[country]['total_recovered']
            coronaData[3] = self.countryCovidDict[country]['source']
        return coronaData
