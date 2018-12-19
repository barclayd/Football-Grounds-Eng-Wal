import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Load data from .txt file
data = pd.read_csv("football-data.txt")
lat = data['Latitude']
lon = data['Longitude']
team = data['Team']
city = data['City']
country = data['Country']

# base map
grounds_map = folium.Map(location=[51.481583, -3.179090], zoom_start=5, tiles='CartoDB dark_matter')

# change colour based on country


def colour_change(location):

    switcher = {
        'England': 'green',
        'France': 'blue',
        'Germany': 'orange',
        'Scotland': 'black',
        'Spain': 'red'
    }
    return switcher.get(location, lambda: 'gray')


# first ground
folium.CircleMarker(location=[53.3831, -2.3356], popup="Altrincham FC, Altrincham", color='red', opacity='0.8', radius=5).add_to(grounds_map)

# create cluster of grounds
cluster = MarkerCluster().add_to(grounds_map)

# plot grounds
for lat, lon, team, country, city in zip(lat, lon, team, country, city):
    folium.CircleMarker(location=[lat, lon], popup=str(team) + " FC" + ", " + str(city),
                        radius=9, fill_opacity=0.8, color='blue',
                        fill_color=(colour_change(country))).add_to(cluster)

grounds_map.save("football-grounds.html")
