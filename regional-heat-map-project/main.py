import folium 
import pandas as pd
from folium.plugins import HeatMap
from folium import DivIcon
from folium.plugins import MiniMap

#Latitude and longitude information of locations and research numbers in each location
locations = [
    {'name': 'İzmit Körfezi', 'lat': 40.74305, 'lon': 29.90333, 'research_count': 31},
    {'name': 'Bandırma Körfezi', 'lat': 40.400000, 'lon': 28.016667, 'research_count': 12},
    {'name': 'Saros Körfezi', 'lat': 40.558930, 'lon': 26.459340, 'research_count': 1},
    {'name': 'Çanakkale Boğazı', 'lat': 40.200000, 'lon': 26.400000, 'research_count': 22},
    {'name': 'Yenikapı', 'lat': 41.001040, 'lon': 28.949790, 'research_count': 4},
    {'name': 'Burgaz Adası', 'lat': 40.881300, 'lon': 29.067070, 'research_count': 3},
    {'name': 'Gemlik Körfezi', 'lat': 40.431420, 'lon': 29.153240, 'research_count': 8},
    {'name': 'Haliç', 'lat': 41.029167, 'lon': 28.961111, 'research_count': 20},
    {'name': 'Yalova', 'lat': 40.654930, 'lon': 29.283780, 'research_count': 11},
    {'name': 'Susurluk Havzası', 'lat': 39.913950, 'lon': 28.156870, 'research_count': 1},
    {'name': 'İstanbul Boğazı', 'lat': 41.119444, 'lon': 29.075278, 'research_count': 18},
    {'name': 'Gönen Çayı', 'lat': 40.143710, 'lon': 27.654800, 'research_count': 1},
    {'name': 'Erdek Körfezi', 'lat': 40.366667, 'lon': 27.666667, 'research_count': 13},
    {'name': 'Tuzla', 'lat': 40.885000, 'lon': 29.351111, 'research_count': 4},
    {'name': 'İznik Gölü', 'lat': 40.443611, 'lon': 29.508333, 'research_count': 4},
    {'name': 'Küçükçekmece Gölü', 'lat': 41.005556, 'lon': 28.746944, 'research_count': 6},
    {'name': 'Bursa', 'lat': 40.183333, 'lon': 29.066667, 'research_count': 6},
    {'name': 'Kocaeli', 'lat': 40.852000, 'lon': 29.878000, 'research_count': 9},
    {'name': 'Tekirdağ', 'lat': 40.966667, 'lon': 27.500000, 'research_count': 15},
    {'name': 'Terkos Gölü', 'lat': 41.340000, 'lon': 28.571111, 'research_count': 1},
    {'name': 'Adalar', 'lat': 40.880278, 'lon': 29.095000, 'research_count': 12},
    {'name': 'İstanbul', 'lat': 41.016667, 'lon': 29.000000, 'research_count': 36},
    {'name': 'Yenikapı', 'lat': 41.000000, 'lon': 28.950000, 'research_count': 4},
    {'name': 'Karadeniz', 'lat': 41.51750, 'lon': 29.13306, 'research_count': 11},
    {'name': 'Çanakkale', 'lat': 40.151944, 'lon': 26.405556, 'research_count': 7},
    {'name': 'Marmara Ereğlisi', 'lat': 40.969722, 'lon': 27.955278, 'research_count': 6},
    {'name': 'Kapıdağ Yarımadası', 'lat': 40.459490, 'lon': 27.851720, 'research_count': 9},
    {'name': 'Kınalıada', 'lat': 40.913056, 'lon': 29.050000, 'research_count': 4},
    {'name': 'Akdeniz', 'lat': 35.370750, 'lon': 30.168920, 'research_count': 6},
    {'name': 'Ege Denizi', 'lat': 39.64056, 'lon': 25.64472, 'research_count': 6},
    {'name': 'Büyükada', 'lat': 40.857778, 'lon': 29.120000, 'research_count': 1},
    {'name': 'Susurluk Nehri', 'lat': 39.716190, 'lon': 28.169990, 'research_count': 1},
    {'name': 'Nilüfer Çayı', 'lat': 40.299444, 'lon': 28.457222, 'research_count': 2},
    {'name': 'Akçakoca', 'lat': 41.083333, 'lon': 31.116667, 'research_count': 1},
    {'name': 'Paşalimanı', 'lat': 40.478611, 'lon': 27.615278, 'research_count': 1},
    {'name': 'Küçükçekmece', 'lat': 41.000000, 'lon': 28.800000, 'research_count': 1},
    {'name': 'Avcılar', 'lat': 40.979167, 'lon': 28.721389, 'research_count': 1},
    {'name': 'Kumbağ', 'lat': 40.869444, 'lon': 27.458333, 'research_count': 1},
    {'name': 'Uçmakdere', 'lat': 40.798105, 'lon': 27.365073, 'research_count': 1},
    {'name': 'Zeytinbağı', 'lat': 40.392222, 'lon': 28.794444, 'research_count': 1},
    {'name': 'Pendik', 'lat': 40.910278, 'lon': 29.296111, 'research_count': 2},
    {'name': 'Gemlik', 'lat': 40.431667, 'lon': 29.156111, 'research_count': 9},
    {'name': 'Marmara Takımadaları', 'lat': 40.500000, 'lon': 27.566667, 'research_count': 4},
    {'name': 'Marmara Adası', 'lat': 40.616667, 'lon': 27.616667, 'research_count': 1},
    {'name': 'Erdek', 'lat': 40.398611, 'lon': 27.793056, 'research_count': 3},
    {'name': 'Kocasu Deltası', 'lat': 40.394050, 'lon': 28.510410, 'research_count': 1},
    {'name': 'Şarköy', 'lat': 40.603889, 'lon': 27.106389, 'research_count': 5},
    {'name': 'Büyükçekmece', 'lat': 41.031111, 'lon': 28.548333, 'research_count': 4},
    {'name': 'Gelibolu', 'lat': 40.413889, 'lon': 26.670278, 'research_count': 2},
    {'name': 'Lapseki', 'lat': 40.343889, 'lon': 26.683611, 'research_count': 1},
    {'name': 'Karabiga', 'lat': 40.403611, 'lon': 27.303889, 'research_count': 2},
    {'name': 'Ocaklar', 'lat': 40.450472, 'lon': 27.752028, 'research_count': 4},
    {'name': 'Maltepe', 'lat': 40.956111, 'lon': 29.160000, 'research_count': 2},
    {'name': 'Eceabat', 'lat': 40.183889, 'lon': 26.356380, 'research_count': 1},
    {'name': 'Mudanya', 'lat': 40.376389, 'lon': 28.883330, 'research_count': 1},
    {'name': 'Beykoz', 'lat': 41.125000, 'lon': 29.105556, 'research_count': 1},
    {'name': 'Bakırköy', 'lat': 40.983056, 'lon': 28.853611, 'research_count': 2},
    {'name': 'Heybeliada', 'lat': 40.877778, 'lon': 29.091667, 'research_count': 1},
    {'name': 'Kumburgaz Havzası', 'lat': 40.833340, 'lon': 28.333333, 'research_count': 1},
    {'name': 'Ataköy', 'lat': 40.983056, 'lon': 28.853611, 'research_count': 1},
    {'name': 'Ambarlı', 'lat': 40.964722, 'lon': 28.674444, 'research_count': 3},
    {'name': 'Üsküdar', 'lat': 41.016667, 'lon': 29.016667, 'research_count': 2},
    {'name': 'Armutlu', 'lat': 41.016667, 'lon': 29.016667, 'research_count': 3},
    {'name': 'Çınarcık', 'lat': 40.642222, 'lon': 29.120278, 'research_count': 9},
    {'name': 'İntepe', 'lat': 40.013333, 'lon': 26.331944, 'research_count': 1},
    {'name': 'Kandıra', 'lat': 40.072222, 'lon': 30.161111, 'research_count': 1},
    {'name': 'Darıca', 'lat': 40.759700, 'lon': 29.385600, 'research_count': 3},
    {'name': 'Balıkesir', 'lat': 39.740833, 'lon': 27.819167, 'research_count': 4},
    {'name': 'Kemer', 'lat': 40.415655, 'lon': 27.067543, 'research_count': 3},
    {'name': 'Bostancı', 'lat': 40.958333, 'lon': 29.095556, 'research_count': 1},
    {'name': 'Altıntaş', 'lat': 40.366200, 'lon': 28.900800, 'research_count': 1},
    {'name': 'Gebze', 'lat': 40.800000, 'lon': 29.433333, 'research_count': 2},
    {'name': 'Kırklareli', 'lat': 41.681111, 'lon': 27.471389, 'research_count': 1},
    {'name': 'Kütahya', 'lat': 39.304722, 'lon': 29.590000, 'research_count': 1},
    {'name': 'Dragos', 'lat': 40.901980, 'lon': 29.149980, 'research_count': 1},
    {'name': 'Fenerbahçe', 'lat': 40.974444, 'lon': 29.043611, 'research_count': 1},
    {'name': 'Edirne', 'lat': 41.676944, 'lon': 26.555556, 'research_count': 1},
    {'name': 'Hereke', 'lat': 40.790833, 'lon': 26.555556, 'research_count': 1},
    {'name': 'Sivriada', 'lat': 40.876667, 'lon': 28.966667, 'research_count': 1},
    {'name': 'Kalamış', 'lat': 40.978333, 'lon': 29.040278, 'research_count': 6},
    {'name': 'Kartal', 'lat': 40.906389, 'lon': 29.210833, 'research_count': 1},
    {'name': 'Fatih', 'lat': 41.013056, 'lon': 28.953611, 'research_count': 1},
    {'name': 'Silivri', 'lat': 41.073889, 'lon': 28.246389, 'research_count': 8},
    {'name': 'Kadıköy', 'lat': 40.986944, 'lon': 29.036667, 'research_count': 2}
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
            icon_anchor=(5, 5),  # Position of the icon relative to its point
            html=f'<div style="background-color: lightgray; width: 10px; height: 10px; border-radius: 50%; opacity: 0.5;"></div>'
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
