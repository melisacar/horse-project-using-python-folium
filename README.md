# Horse - Marmara Region Mapping

## Overview
- This repository contains two projects focused on mapping and visualizing environmental data and academic research related to the Marmara region of Turkey. These projects are designed to provide insights into both the region's waste management infrastructure and the concentration of research activities on the Sea of Marmara.
  
## Projects
1. **Marmara Region Energy, Wastewater and Solid Waste Facilities Mapping**
   - **Description:** This project visualizes the locations of energy, wastewater and solid waste facilities in the Marmara region. Using Python and Folium, it generates an interactive map that displays facility details when hovering over each location.
   - **Interactive Map:** Explore the map here to see information about each facility.
   - **Key Features:**
     - Interactive map showcasing facilities in the region.
     - Tooltips provide quick access to relevant information.
     - Project Folder: `marmara-facilities-project`

2. **The Sea of Marmara Mapping - Realted Researches**
   - **Description:** This project involves a comprehensive literature review of academic studies published between 2020 and 2024 on the Sea of Marmara. The goal is to visualize the concentration of research activities through an interactive heatmap, helping researchers identify areas with more intensive study.
   - **Interactive Heatmap:** Visualize the research concentration here.
   - **Key Features:**
     - Heatmap showing research density across the Marmara Sea.
     - Systematic archiving of academic studies for easy reference.
     - Project Folder: `regional-heat-map-project`


## Installation
1. Clone the Repo
```shell
git clone https://github.com/melisacar/horse-project-using-python-folium.git
cd horse-project-using-python-folium
```

2. Set Up the Environment
- Ensure you have Python installed on your machine. Then install the necessary packages using requirements.txt:
```shell
pip install -r marmara-facilities-project/requirements.txt  # For Facilities Mapping
pip install -r regional-heat-map-project/requirements.txt  # For Research Heatmap
```

3. Run the Script
- Generate the map by running:
  - Facilities Map
```shell
python marmara-facilities-project/main.py
```
  - Research Heatmap
```shell
python regional-heat-map-project/main.py
```

4. View the Map
   - Open the generated HTML file in your web browser to view the interactive map and heatmap.

## Dependencies
1. Python 3.x
2. Folium: To create and render interactive maps.

## Future Improvements:
- Facilities Mapping:
    - [ ] Further customization of map icons and popups.

- Research Heatmap
    - [ ] Expand dataset to include publications from before 2020.
    - [ ] Enhance interactive features on the heatmap.