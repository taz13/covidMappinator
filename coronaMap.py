# Import necessary packages
import folium
from branca.element import IFrame


class CoronaMap:
    mapCorona = folium.Map(location=[21.389082, 39.857910], zoom_start=3.4,
                           tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
                           attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                           max_zoom=19
                           )

    def addToMap(self, countryName, lat, long, searchResult=[], coronaData=[0, 0, 0]):
        articleListHtml = self.ulify(searchResult)

        html = '''<h3>{}</h3>\
                    <ul>
                      <li>Cases: {}</li>
                      <li>Death: {}</li>
                      <li>Recovered: {}</li>
                      <li>More info: <a href="{}" target="_blank">{}</a></li>
                    </ul>
               <h5>News Articles:</h5>{}<br/>'''.format(countryName, coronaData[0], coronaData[1], coronaData[2],
                                                        coronaData[3], coronaData[3],
                                                        articleListHtml)

        iframe = IFrame(html, width=250, height=250)
        popup = folium.Popup(iframe, max_width=250)
        icon = folium.Icon(color="black", icon="heartbeat", icon_color='white', prefix='fa')
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