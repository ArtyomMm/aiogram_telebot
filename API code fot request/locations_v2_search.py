import requests
import json

url = "https://hotels4.p.rapidapi.com/locations/v2/search"
my_req = requests.get(url)

querystring = {"query": "new york", "locale": "ru_RU", "currency": "RUB"}

headers = {
	"X-RapidAPI-Key": "3e1942b3a0msh9be2dc804bdadbep1b133fjsn43c864153fd5",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

destination_id_list = list()
jason_request = response.json()
city_hotel_group = len(jason_request["suggestions"])

for i_group in range(city_hotel_group):
	for i_hotel in range(len(jason_request["suggestions"][i_group]["entities"])):
		destination_id_list.append(jason_request["suggestions"][i_group]["entities"][i_hotel]["destinationId"])

if __name__ == "__main__":
	# print(response.text)
	print(destination_id_list)
	# data = json.loads(response.text)
	# with open('1_test_request.json', 'w') as file:
	# 	json.dump(data, file, indent=4, ensure_ascii=False)
