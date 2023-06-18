import requests

# response = requests.get("https://swapi.dev/api/")
# planets_url = response.json()['planets']
#
# # response = requests.get(planets_url)
#
# planets_list = []
# for i in (1, 6):
#     response = requests.get(f'{planets_url}{i}')
#     data = response.json()
#     data['diameter'] = int(data['diameter'])
#
#     planets_list.append(data)
#
# print(max(planets_list, key=lambda x: x['diameter']))

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
# planets_list = ['planets']
# for i in planets_list:
#     response = requests.get(f'{planets_url}{i}')
#     print(response)
#     data = response.json()
#     data['diameter'] = int(data['diameter'])
#
#     planets_list.append(data)
#
# print(max(planets_list, key=lambda x: x['diameter']))

response = requests.get("https://swapi.dev/api/planets/").json()
planets = response.get('results')


max_diameter = 0
planet_name = ''
for i in range(60):
    diameter_str = planets[i].get('diameter')
    if diameter_str != "n/a":
        diameter = int(diameter_str)
        # print(f"{planets[i].get('name')}: {diameter}")
        if diameter > max_diameter:
            max_diameter = diameter
            planet_name = planets[i].get('name')

print(f"Планета с максимальным диаметром: {planet_name}.")