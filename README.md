# Horse - Marmara Region Wastewater and Solid Waste Facilities Mapping

- This project visualizes the locations of wastewater and solid waste facilities in the Marmara region of Turkey. Using Python and the Folium library, the project generates an interactive map where facility details are displayed when hovering over the facility's location.

## Features
- **Interactive Map:** The map displays wastewater and solid waste facilities' coordinates within the Marmara region.
- **Tooltips:** Hovering over each facility marker shows a tooltip with relevant information.
- **Python-Powered:** Built using Python and the Folium library to create and customize the interactive map.

## Installation
1. Clone the Repo
```shell
git clone https://github.com/melisacar/horse-project-using-python-folium.git
cd horse-project-using-python-folium
```

2. Set Up the Environment
- Ensure you have Python installed on your machine. Then install the necessary packages using requirements.txt:
```shell
pip install -r requirements.txt
```

3. Run the Script
- Generate the map by running:
```shell
python main.py
```

4. View the Map
- Open the generated HTML file in your web browser to view the interactive map:
```shell
start marmara_waste_facilities_map.html  # Windows
open marmara_waste_facilities_map.html  # macOS
xdg-open marmara_waste_facilities_map.html  # Linux
```

## Dependencies
1. Python 3.x
2. Folium: To create and render interactive maps.

## Future Improvements:
- Make custom changes:
    - [x] map style
    - [x] icon style
    - [ ] popup background and typing color
    - [ ] minimap 
    - [ ] heatmap 

