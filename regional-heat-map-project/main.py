import folium 
import pandas as pd
from folium.plugins import HeatMap

#Latitude and longitude information of locations and research numbers in each location
locations = [
    {'name': 'Location1', 'lat': 41.02611, 'lon': 29.00000, 'research_count': 100},
    {'name': 'Location2', 'lat': 40.90278, 'lon': 29.05250, 'research_count': 10},
    {'name': 'Location3', 'lat': 40.42723, 'lon': 26.73223, 'research_count': 40}  
    #Other locations
]

#Creating the map
heat_map = folium.Map(location=[40.63, 28.12], tiles='Cartodb Positron', zoom_start=8)

#Data points for the heatmap
heat_data = [[loc['lat'], loc['lon'], loc['research_count']] for loc in locations]

#Adding the heatmap
HeatMap(heat_data).add_to(heat_map)

#Adding markers
for loc in locations:
    folium.Marker(
        location=[loc['lat'], loc['lon']],
        popup=f"{loc['name']}: {loc['research_count']} studies",
        tooltip=loc['name'],
        icon=folium.Icon(color='black', icon='info-sign')
    ).add_to(heat_map)

heat_map.save("heat_map.html")
