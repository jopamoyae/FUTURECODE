import requests

response = requests.get("https://swapi.dev/api/")
planets_url = response.json()['planets']
# response = requests.get(planets_url)

planets_list = []
for i in range(1, 6):
    response = requests.get(f'{planets_url}{i}')
    data = response.json()
    data['diameter'] = int(data['diameter'])

    planets_list.append(data)

print(max(planets_list, key=lambda x: x['diameter']))

# max_diameter = 0
#
# for planet in planets_list:
#     if planet['diameter'] > max_diameter:
#         max_diameter = planet['diameter']
#
# print(max_diameter)
#
# for planet in planets_list:
#     if planet['diameter'] == max_diameter:
#         print(planet)
#         break
