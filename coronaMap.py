# Import necessary packages
import folium
from branca.element import IFrame


class CoronaMap:

    mapCorona = folium.Map(location=[21.389082, 39.857910],zoom_start=3)




    def addToMap(self,countryName,lat,long,searchResult=[]):
        articleListHtml = self.ulify(searchResult)

        html = '''<h3>Country: {}</h3>\
               <h4>News Articles:</h4> {}<br />'''.format(countryName,articleListHtml)

        iframe = IFrame(html, width=300 + 200, height=300 + 20)
        popup = folium.Popup(iframe, max_width=650)
        icon = folium.Icon(color="white", icon="cloud", icon_color='black')
        tooltip = 'Click to view more about: ' + countryName
        location = [lat, long]
        folium.Marker(location=location,
                               popup=popup, tooltip=tooltip, icon=icon).add_to(self.mapCorona)

    def saveMap(self):
        self.mapCorona.save("coronaMap.html")

    def ulify(self,list=[]):
        htmlString = "<ul>\n"
        for s in list:
            urlElements = str(s).split(" : ")
            htmlString += "<li>" + '<a href="{}" target="_blank">{}</a>'.format(urlElements[1],urlElements[0]) + "</li>\n"
        htmlString += "</ul>"
        return htmlString