#pip install folium
import folium

#Coordinates and relative informations 
fac = [
    {'name': 'Ambarlı İleri Biyolojik Atık Su Arıtma Tesisi', 'lat': 40.9900, 'lon': 28.6811, 'detail': 'This facility treats 5000 m³ of wastewater daily.'},
    {'name': 'Odayeri Enerji Üretim Tesisi', 'lat': 41.2167833, 'lon': 28.853361, 'detail': 'This facility produces 1000000 tons of solid waste per year.'},
    #Other facilities...
]

#Creating the map
marmara_region_map = folium.Map(location=[40.63, 28.12], zoom_start=8)
#Setting the boundaries
bounds = [[40.0, 26.5], [41.5, 30.0]]
marmara_region_map.fit_bounds(bounds)

#Adding facilities to the marmara region map
for facility in fac:
    folium.Marker(
        location=[facility['lat'], facility['lon']],
        popup=folium.Popup(facility['detail'], max_width=200),  #Balloon that opens when clicked
        tooltip=facility['name'],  #Note balloon that appears when hovering over it with the mouse
    ).add_to(marmara_region_map)

#Saving the map
marmara_region_map.save("marmara_waste_facilities_map.html")