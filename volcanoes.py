import folium

# base map
map = folium.Map(location=[51.481583, -3.179090], zoom_start=8)

map.save("map1.html")
