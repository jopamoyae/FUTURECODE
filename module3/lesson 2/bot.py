import vk_api
import random
from cb_rf import get_currency
import requests

vk = vk_api.VkApi(token="vk1.a.DnWRdd5kGtoDrWRQQQkUyXDcXc39RzYrzitYE_jozxGiUnhnxs1ht_l5uTY8BA49kfz7SIVAtMWyFFBjf6jlnwz8KEO9886YDx-yZxeuh2-vf3yglWDAKg26SkNhZOuZ54CFm_MEuh7TrhdOnJ1BdKwCWSaSjJRciao5qpHc9Vr2vvkDoXoER-D34y1UhJnogsbviArRr1EZ_6S6CSrK5A")


while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages["count"] >= 1:
        msg_text = messages["items"][0]["last_message"]["text"]

        if msg_text.lower() == '-к':
            global currency_id
            currency_info = get_currency(currency_id)
            ans = f'Курс {currency_info.get("name")} составляет {currency_info.get("value")} руб.'
            # ans = f'Курс доллара на сегодня составляет: {get_currency()} руб.'
        else:
            ans = 'Неизвестная команда('

        user_id = messages['items'][0]['last_message']['from_id']
        vk.method(
            "messages.send",
            {
                'random_id': random.randint(-10 ** 7, 10 ** 7),
                'user_id': user_id,
                'message': ans
            }
        )


        def get_starships():
            response = requests.get("https://swapi.dev/api/starships/")
            return response.json()


        def handle_message(msg_text):
            if msg_text.lower() == "корабли":
                starships = get_starships()["results"]
                fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"]))
                response = f'Максимальная скорость звездного корабля {fastest_starship["name"]} - {fastest_starship["max_atmosphering_speed"]} км/ч.'
            else:
                response = "Я не понимаю, что вы хотите."
            return response
