import requests
import json
response = requests.get('https://www.google.com')
print(response) #<Response [200]>


if response :
    print('Using response in conditional statement returns true if its status code lies between 200 and 400')
else :
    print("Else it returns false")

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = "delhi technological university"
param = {"address": location}
response = requests.get(URL, param) #passes two parameters: URL and a parameter dictionary
print(response.url)
data = response.json() #returned response can be converted into a json object using json()
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results][0]['geometry']['location']['lng']
print("Latitude:%s\nLongitude:%s"%(latitude,longitude)) 
#Latitude:28.7499867
#Longitude:77.1183137
