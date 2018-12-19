import folium
import pandas as pd

# base map
map = folium.Map(location=[51.481583, -3.179090], zoom_start=5, tiles='Mapbox bright')

# Load Data
data = pd.read_csv("football-data.txt")
lat = data['Latitude']
lon = data['Longitude']
team = data['Team']

# first ground
folium.Marker(location=[51.4728,-3.2030], popup="Cardiff City Stadium", icon=folium.Icon(color='blue')).add_to(map)

# multiple grounds in Swansea
for coordinates in [[51.6427, -3.9346],[51.6834, -4.1478], [51.596249, -3.780910]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color='white')).add_to(map)

# plot grounds
for lat, lon, team in zip(lat, lon, team):
    folium.Marker(location=[lat, lon], popup=str(team)+" FC", icon=folium.Icon(color='gray')).add_to(map)

map.save("football-grounds.html")
