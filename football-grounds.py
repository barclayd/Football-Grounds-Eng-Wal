import folium
import pandas as pd

# Load Data
data = pd.read_csv("football-data.txt")
lat = data['Latitude']
lon = data['Longitude']
team = data['Team']
city = data['City']
country = data['Country']

# base map
map = folium.Map(location=[51.481583, -3.179090], zoom_start=5, tiles='CartoDB dark_matter')

# change colour based on country


def colour_change(country):

    switcher = {
        'England': 'green',
        'France': 'blue',
        'Germany': 'orange',
        'Scotland': 'black',
        'Spain': 'red'
    }
    return switcher.get(country, lambda: 'gray')


# first ground
folium.Marker(location=[51.4728, -3.2030], popup="Cardiff City Stadium", icon=folium.Icon(color='blue')).add_to(map)

# multiple grounds in Swansea
for coordinates in [[51.6427, -3.9346], [51.6834, -4.1478], [51.596249, -3.780910]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color='gray')).add_to(map)

# plot grounds
for lat, lon, team, country, city in zip(lat, lon, team, country, city):
    folium.CircleMarker(location=[lat, lon], popup=str(team) + " FC" + ", " + str(city),
                        radius=9, fill_opacity=0.9,
                        fill_color=(colour_change(country))).add_to(map)

map.save("football-grounds.html")
