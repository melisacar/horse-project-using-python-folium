#pip install folium
import folium
from folium.plugins import MiniMap
from branca.element import Template, MacroElement

#Coordinates and relative informations 
fac = [
    {'name': 'Ambarlı İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 40.9900, 'lon': 28.6811, 'detail': 'This facility treats 5000 m³ of wastewater daily.'},
    #Other water related acilities...
]

fac_2 = [
    {'name': 'Odayeri Enerji Üretim Tesisi', 'lat': 41.2167833, 'lon': 28.853361, 'detail': 'This facility produces ... energy per year.'},
    #Other energy related facilities...
]

fac_3 = [
    {'name': 'Odayeri AGM', 'lat': 41.1167833, 'lon': 28.853361, 'detail': 'This facility collects ... solid waste a year.'},
    #Other solid waste related facilities...
]


#Creating the map
marmara_region_map = folium.Map(location=[40.63, 28.12], tiles='Cartodb Positron', zoom_start=8)

#Add minimap
MiniMap(toggle_display=True).add_to(marmara_region_map)

#Setting the boundaries
bounds = [[40.0, 26.5], [41.5, 30.0]]
marmara_region_map.fit_bounds(bounds)

#Adding first type of facilities to the marmara region map
for facility in fac:
    folium.Marker(
        location=[facility['lat'], facility['lon']],
        popup=folium.Popup(facility['detail'], max_width=200),  #Balloon that opens when clicked
        icon=folium.Icon(color = 'blue', icon = 'tint', prefix = 'glyphicon'),
        tooltip=facility['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

#Adding second type of facilities to the marmara region map
for facility in fac_2:
    folium.Marker(
        location=[facility['lat'], facility['lon']],
        popup=folium.Popup(facility['detail'], max_width=200),  #Balloon that opens when clicked
        icon=folium.Icon(color = 'lightgray', icon = 'info-sign', prefix = 'glyphicon'),
        tooltip=facility['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

#Adding third type of facilities to the marmara region map
for facility in fac_3:
    folium.Marker(
        location=[facility['lat'], facility['lon']],
        popup=folium.Popup(facility['detail'], max_width=200),  #Balloon that opens when clicked
        icon=folium.Icon(color= 'green', icon = 'trash', prefix = 'glyphicon'),
        tooltip=facility['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

# Creating a custom legend
legend_html = '''
<div style="position: fixed;
            top: 25px; right: 25px; width: 250px; height: 90px;
            background-color: white; z-index:9999; font-size:12px;
            border:2px white; padding: 10px;">
    <h4>Legend</h4>
    <i class="fa fa-tint" style="color:blue"></i> Wastewater Facilities<br>
    <i class="fa fa-trash" style="color:green"></i> Solid Waste Facilities<br>
    <i class="fa fa-info-circle" style="color:lightgray"></i> Energy Production Facilities
</div>
'''
marmara_region_map.get_root().html.add_child(folium.Element(legend_html))

#Saving the map
marmara_region_map.save("marmara_waste_facilities_map.html")