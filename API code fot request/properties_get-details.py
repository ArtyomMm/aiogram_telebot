import requests
import json

url = "https://hotels4.p.rapidapi.com/properties/get-details"

querystring = {"id":"260158","checkIn":"2020-01-08","checkOut":"2020-01-15","adults1":"1","currency":"RUB","locale":"ru_RU"}

headers = {
	"X-RapidAPI-Key": "3e1942b3a0msh9be2dc804bdadbep1b133fjsn43c864153fd5",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
with open('3_test_request.json', 'w') as file:
	json.dump(data, file, indent=4, ensure_ascii=False)
