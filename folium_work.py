import requests

url = "https://countries-cities.p.rapidapi.com/location/city/5128580"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "countries-cities.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

