import requests
import json

url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

querystring = {"id":"260158"}

headers = {
	"X-RapidAPI-Key": "3e1942b3a0msh9be2dc804bdadbep1b133fjsn43c864153fd5",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
with open('4_test_request.json', 'w') as file:
	json.dump(data, file, indent=4, ensure_ascii=False)