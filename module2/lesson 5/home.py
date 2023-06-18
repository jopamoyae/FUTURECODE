import requests

# response = requests.get("https://swapi.dev/api/")
#
# starships_url = response.json()['starships']
#
# for i in range(1, 6):
#     starships_url = f'{starships_url}{i}'
#     response = requests.get(starships_url)
#     print(response.status_code)
#
#     if response.status_code == 200:
#         print(response.json())





# starships_url = response.get('results')
# max_speed = 0
# fastest_ship = ""
#
# for ship in starships_url:
#     speed = ship.get("max_atmosphering_speed")
#     if speed == 'unknown':
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ship.get("name")
#
# print("Cамый быстрый корабль:", fastest_ship)

import requests

response = requests.get('https://swapi.dev/api/starships/').json()
starships = response.get('results')

max_speed = 0
ship_name = ''
for i in range(36):
    speed_str = starships[i].get('max_atmosphering_speed')
    if speed_str != "n/a":
        speed = int(speed_str)
        print(f"{starships[i].get('name')}: {speed}")
        if speed > max_speed:
            max_speed = speed
            ship_name = starships[i].get('name')

print(f"Звездный корабль с максимальной скоростью: {ship_name}.")