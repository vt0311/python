import urllib.request
import folium 
import pandas as pd 
import datetime
import webbrowser
import json 

#[CODE1]
def get_request_url( url):
    client_id = "LaQyj9g37x7Ac6N0rxhK"
    client_secret = "YdruZ2tsgK"
    
    req = urllib.request.Request( url )
    req.add_header('X-Naver-Client-Id', client_id) # 교재 35쪽 참고
    req.add_header('X-Naver-Client-Secret', client_secret)
    
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as err:
        print( err )
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE2]
def getGeoData(address):
    base = 'https://openapi.naver.com/v1/map/geocode'
    try :
        parameters = '?query=%s' % (urllib.parse.quote(address))
    except :
        return None
    
    url = base + parameters
    
    retData = get_request_url( url )
    if retData == None :
        return None 
    
    jsonAddress = json.loads(retData)
    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else :
        return None 
    
    return [latitude, longitude]

def main():
    #[CODE3]
    latitude = 37.5485148
    longitude = 127.1341524
    map = folium.Map(location=[latitude, longitude], zoom_start=14)
    
    filename = 'bbq_modify_mini.csv'
    df = pd.read_csv(filename, encoding='cp949', index_col = 0, header = 0)
    geoData = []

    #[CODE4]
    for index, row in df.iterrows() :
#         print(index, '/', row)
        # row['store_address'] 예시 : 서울특별시 강동구 올림픽로 786 (암사동) 
        geoData = getGeoData(row['store_address'])
        if geoData != None : # row['store'] 예시 : 강일지구점
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='red')).add_to(map)
            
    filename = 'pericana_modify_mini.csv'
    df = pd.read_csv(filename, encoding='cp949', index_col = 0, header = 0)

    for index, row in df.iterrows() :
        geoData = getGeoData(row['store_address'])
        if geoData != None :
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='green')).add_to(map)
            
    filename = 'nene_modify_mini.csv'
    df = pd.read_csv(filename, encoding='cp949', index_col = 0, header = 0)

    for index, row in df.iterrows() :
        geoData = getGeoData(row['store_address'])
        if geoData != None : 
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='blue')).add_to(map)  
    
    svFileName = 'chicken.html'
    map.save( svFileName )
    webbrowser.open( svFileName )
            
if __name__ == '__main__' :
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    