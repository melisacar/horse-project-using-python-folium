import folium 
import pandas as pd
from folium.plugins import HeatMap
from folium import DivIcon

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
        #icon=folium.Icon(color='lightgray', icon='info-sign'),
        icon=DivIcon(
            icon_size=(20, 20),  # Icon size (width, height)
            icon_anchor=(10, 10),  # Position of the icon relative to its point
            html=f'<div style="background-color: lightgray; width: 20px; height: 20px; border-radius: 50%; opacity: 0.5;"></div>'
        )
    ).add_to(heat_map)

heat_map.save("heat_map.html")
