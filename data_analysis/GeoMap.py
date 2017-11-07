import folium
import pandas as pd
import urllib.request
import datetime
import time
import json
from config import *

import os
import sys
import webbrowser

#[CODE 1]
def get_request_url(url):
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 2]
def getGeoData(address):
    
    base = "https://openapi.naver.com/v1/map/geocode"
    
    try:
        parameters = "?query=%s" % urllib.parse.quote(address)
    except:
        return None
    
    url = base + parameters
    
    retData = get_request_url(url)
    if retData == None:
        return None

    jsonAddress = json.loads(retData)

    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else:
        return None
    
    return [latitude, longitude]

'''
    os.path.basename(filename) - 파일명만 추출
    os.path.dirname(filename) - 디렉토리 경로 추출
    os.path.split(filename) - 경로와 파일명을 분리
    os.path.splitdrive(filename) - 드라이브명과 나머지 분리 (MS Windows의 경우)
    os.path.splitext(filename) - 확장자와 나머지 분리
    '''

'''
colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]
'''
def main():
   
    #[CODE 3]
    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    filename = 'd:/temp/chicken_data/bbq_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    
    #[CODE 4]
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='red')).add_to(map)
    
    filename = 'd:/temp/chicken_data/pericana_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='blue')).add_to(map)

    filename = 'd:/temp/chicken_data/nene_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='gray')).add_to(map)

    filename = 'd:/temp/chicken_data/kyochon_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='orange')).add_to(map)

    filename = 'd:/temp/chicken_data/cheogajip_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='green')).add_to(map)

    filename = 'd:/temp/chicken_data/goobne_modify.csv'
    df = pd.DataFrame.from_csv(filename, encoding='CP949', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='purple')).add_to(map)

    #[CODE 5]
    s = os.path.split(filename)
    svFilename = ('%s/%s.html') % (s[0], s[1])
    map.save(svFilename)
    webbrowser.open(svFilename)  
    

if __name__ == "__main__":

    main()
