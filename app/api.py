from http.server import HTTPServer, BaseHTTPRequestHandler
import json 
import os 
from os import path
import requests
import redis

API_INFO = None
CACHE_DB = None

#Defining a API config storage class
class ApiConfig:
	
	def __init__(self, var_name):
		config = json.loads(os.environ[var_name])
		self.domain = config[0]["owm_list"][0]["domain"]
		self.path = config[0]["owm_list"][0]["path"]
		self.api_key = config[0]["owm_list"][0]["key"]
		self.unit = config[0]["owm_list"][0]["unit"]



#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):

	#GET Method Defination
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()
		#splits the given path to get the id
		path = self.path.split("/")
		city_id = path[3]
		#get the requested info
		weatherInfo = get_weather(city_id)
		self.wfile.write(json.dumps(weatherInfo).encode())



#Initializes Api config data and server
def init():
	print("\napi - init\n")
	load_config()	
	server = HTTPServer((os.environ.get('API_IP'), int(os.environ.get('API_PORT'))), ServiceHandler)
	try:
		server.serve_forever()
	finally:
		server.shutdown()



#Loads API variables and connect to redis
def load_config():
	global API_INFO
	global CACHE_DB
	API_INFO = ApiConfig('SERVICE_WEATHERAPI_CONFIG')
	CACHE_DB = redis.StrictRedis(os.environ.get('REDIS_IP'), int(os.environ.get('REDIS_PORT')))



#Gets the weather info from the cache if exists else makes request
def get_weather(city_id):
	if(CACHE_DB.execute_command('EXISTS', city_id) == 1):
		data = json.loads(CACHE_DB.execute_command('JSON.GET', city_id))
		return data
	return request_and_store(city_id)			



#Makes request to OpenWeather and stores in cache
def request_and_store(city_id):
	response = requests.get(API_INFO.domain + API_INFO.path, headers = {"Accept": "application/json"}, params = {"id": city_id, "units": API_INFO.unit, "appid": API_INFO.api_key})
	data = response.json()
	CACHE_DB.execute_command('JSON.SET', city_id, '.', json.dumps(data))
	return data



#Helper to print the data
def print_info(info) :

    print("Temperature now in " + info['name'] + " is " + str(info['main']['temp']) + " Celsius")
    print("and if you look to the sky you see " + info['weather'][0]['description'] )


