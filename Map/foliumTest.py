import folium 

# 서울 특별 시청을 중심으로 포리움 맵 생성
latitude = 37.566345
longitude = 126.977893
map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
map_osm.save('c:/work/map1.html')
print( type(map_osm))

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('c:/work/map2.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Toner')
map_osm.save('c:/work/map3.html')

# 마커(Marker)와 팝업(Popup)의 설정
folium.Marker([latitude, longitude], popup='서울 특별시청').add_to(map_osm)
folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map_osm)
map_osm.save('c:/work/map4.html')

# 부트 스트랩을 이용하여 아이콘 타입을 설정할 수 있다.
# 범위를 설정하기 위하여 circle 속성을 줄 수 있다.
# 부트 스트랩을 사용하기 위하여 따로 설정할 것은 없는 듯.... 
map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울 특별시청', \
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859, 126.9754788], radius=150, color='#3186cc', \
            fill_color='#3186cc', popup='덕수궁').add_to(map_osm)

map_osm.save('c:/work/map5.html')
print( type(map_osm))

print('파일 저장 완료')