from random import randint

film = ['Дюна', 'Анчартед', 'Остров проклятых', 'Шоу Трумана', 'Стражи Галактики']
rand_ind = randint(0, len(film) - 1)

while True:
    lead = input('Введите команду <фильм>, чтобы увидеть рекомендации: ')
    if lead.lower() == 'фильм':
        print(film[rand_ind])
