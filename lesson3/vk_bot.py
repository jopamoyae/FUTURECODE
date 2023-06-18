import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from cb_RF import get_course
from wiki import get_article

vk_session = vk_api.VkApi(token="vk1.a.DnWRdd5kGtoDrWRQQQkUyXDcXc39RzYrzitYE_jozxGiUnhnxs1ht_l5uTY8BA49kfz7SIVAtMWyFFBjf6jlnwz8KEO9886YDx-yZxeuh2-vf3yglWDAKg26SkNhZOuZ54CFm_MEuh7TrhdOnJ1BdKwCWSaSjJRciao5qpHc9Vr2vvkDoXoER-D34y1UhJnogsbviArRr1EZ_6S6CSrK5A")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_msg = event.text.lower()
        if user_msg[0:2] == '-к':
            response = "Курс доллара {0} руб. за 1 шт.\nКурс евро {1} руб. за 1 шт.\nКурс юаня {2} руб. за 1 шт.".format(
                get_course("R01235"), get_course("R01239"), get_course("R01375")
            )
        elif user_msg[0:2] == '-в':
            article = user_msg[2:]
            response = f'Вот что я нашел:\n\n{get_article(article)}'
        else:
            response = 'Нет такой команды('
        vk.messages.send(user_id=event.user_id, message=response, random_id=random.randint(-10 ** 7, 10 ** 7))
