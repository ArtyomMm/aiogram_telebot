import requests
import json

url = "https://hotels4.p.rapidapi.com/locations/v2/search"
my_req = requests.get(url)

querystring = {"query": "Bryansk", "locale": "en_US", "currency": "USD"}

headers = {
	"X-RapidAPI-Key": "3e1942b3a0msh9be2dc804bdadbep1b133fjsn43c864153fd5",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
# data = json.loads(response.text)
# with open('my_test.json', 'w') as file:
# 	json.dump(data, file, indent=4)
