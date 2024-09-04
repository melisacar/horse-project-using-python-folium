import folium 
import pandas as pd
from folium.plugins import HeatMap
from folium import DivIcon
from folium.plugins import MiniMap

#Latitude and longitude information of locations and research numbers in each location
locations = [
    {'name': 'İzmit Körfezi', 'lat': 40.7, 'lon': 29.94091, 'research_count': 31}
    #Other locations
]

#Creating the map
heat_map = folium.Map(location=[40.63, 28.12], tiles='Cartodb Positron', zoom_start=8)

#Add minimap
MiniMap(toggle_display=True).add_to(heat_map)

#Data points for the heatmap
heat_data = [[loc['lat'], loc['lon'], loc['research_count']] for loc in locations]

#Adding the heatmap
HeatMap(heat_data).add_to(heat_map)

#Adding markers
for loc in locations:
    folium.Marker(
        location=[loc['lat'], loc['lon']],
        popup=f"<div style='width: 100px;'><b>{loc['name']}</b>: Marmara Denizi konulu {loc['research_count']} bilimsel araştırma bulunmaktadır.",
        tooltip=loc['name'],
        icon=DivIcon(
            icon_size=(2, 2),  # Icon size (width, height)
            icon_anchor=(10, 10),  # Position of the icon relative to its point
            html=f'<div style="background-color: lightgray; width: 20px; height: 20px; border-radius: 50%; opacity: 0.5;"></div>'
        )
    ).add_to(heat_map)

#Legend
legend_html = '''
<div style="
    position: fixed; 
    bottom: 20px; left: 15px; width: 50px; height: 100px; 
    border: none; z-index:9999; font-size:10px;
    ">
    <div style="display: flex; flex-direction: column; height: 100%; align-items: center; padding: 0;">
        <div style="flex: 1; background: linear-gradient(to top, blue, green, yellow, red); width: 30%; height: 100%; border-radius: 5px;"></div>
        <div style="display: flex; flex-direction: column; justify-content: space-between; font-size: 8px; padding: 0; height: 100%; margin-right: 25px; margin-top: -100px;">
            <span style="margin: 0; ;">50</span>
            <span style="margin: 0; ">25</span>
            <span style="margin: 0; ">0</span>
        </div>
    </div>
</div>
'''

#Add legend
heat_map.get_root().html.add_child(folium.Element(legend_html))

heat_map.save("heat_map.html")
