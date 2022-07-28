import requests
import json
from locations_v2_search import destination_id_list

url = "https://hotels4.p.rapidapi.com/properties/list"

for i_des_id in destination_id_list:
	querystring = {
		"destinationId": i_des_id, "pageNumber": "1", "pageSize": "25",
		"checkIn": "2020-01-08", "checkOut": "2020-01-15", "adults1": "1",
		"sortOrder": "PRICE", "locale": "ru_RU", "currency": "RUB"
	}

	headers = {
		"X-RapidAPI-Key": "3e1942b3a0msh9be2dc804bdadbep1b133fjsn43c864153fd5",
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	jason_request = response.json()
	prices_list = list()  # если /lowprice, то список минимумов, и наоборот

	try:
		for i_hotels in jason_request["data"]["body"]["searchResults"]["results"]:
			prices_list.append(i_hotels["ratePlan"]["price"]["current"])
	except KeyError:
		pass  # 'data'

	try:
		print(min(prices_list))
		print(max(prices_list))
	except ValueError:
		pass  # min() arg is an empty sequence

	# data = json.loads(response.text)
	# with open('2_test_request.json', 'w') as file:
	# 	json.dump(data, file, indent=4, ensure_ascii=False)
