import random

import requests


class CoronaApi:
    coronaApiUrlFormat = "https://thevirustracker.com/free-api?countryTotal={}"

    UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
           "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
           )

    def getCountryResult(self, countryCode):
        ua = self.UAS[random.randrange(len(self.UAS))]

        coronaData = [0, 0, 0]
        apiUrl = self.coronaApiUrlFormat.format(countryCode)
        respone = requests.get(apiUrl, headers={'Accept-Encoding': 'identity', 'user-agent': ua})
        print("status  code: " + str(respone.status_code))
        try:
            jsonResponse = respone.json()
            countryDataKey = 'countrydata'
            if countryDataKey in jsonResponse.keys():
                coronaData[0] = jsonResponse[countryDataKey][0]['total_cases']
                coronaData[1] = jsonResponse[countryDataKey][0]['total_deaths']
                coronaData[2] = jsonResponse[countryDataKey][0]['total_recovered']
            return coronaData
        except Exception as ex:
            print(ex)
        # text = json.dumps(respone.json(), sort_keys=True, indent=4)
        # print(text)
