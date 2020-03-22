import random
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout


class GoogleSearch:
    searchResult = []

    def searchWithKeyWord(self,keyWord):
        # to search
        self.searchResult = [];
        query = keyWord

        UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
               "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
               "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
               )
        for url in search(query, tld="com", num=10,start=0, stop=10, pause=3):
            ua = UAS[random.randrange(len(UAS))]
            headers = {'user-agent': ua}

            try:
                r1 = requests.get(url,headers=headers,timeout=20)
                coverpage = r1.content
                soup1 = BeautifulSoup(coverpage, 'html.parser')
                title = soup1.find_all('title')
                print(title[0].get_text() + " : " + url)
                self.searchResult.append(title[0].get_text() + " : " + url)
            except Exception as ex:
                print(ex)
                print("Request timed out for: "+url)

