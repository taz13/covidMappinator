import requests

class CoronaApi:
    coronaApiUrlFormat = "https://thevirustracker.com/free-api?countryTotal={}"
    def getCountryResult(self,countryCode):
        apiUrl = self.coronaApiUrlFormat.format(countryCode)
        respone = requests.get(apiUrl)
        print(respone.json())
