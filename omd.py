import random

def step1():
    print(
        'Утка-маляр Джо 🦆 решила выпить зайти в бар.\n'
        'Взять ей зонтик? ☂️ (1) Да (2) Нет'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return umbrella()
    return no_umbrella()

def no_umbrella():
    print(
        'Упс! Начался дождь 🌧, может утка️ Джо успеет добежать до метро?\n'
        '(1) Да (2) Нет'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return money()
    return shop()

def money():
    print(
        'Какой же Джо забывчивый: оставил бумажник дома!\n'
        'Что же делать? (1) Вернуться домой за бумажником? (2) Проехать зайцем!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return home()
    return law()

def home():
    print(
        'Дома тепло и уютно!\n'
        '(1) Выпить чаю и уснуть? (2) Напиться и отрубиться!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return sleep()

def sleep():
    print(
        'Утка Джо счастливо спит 💤 и видит сны о новом походе в бар!\n'
        'Начать игру заново? (1) Да! (2) Нет.'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step1()
    print('Пока!')

def law():
    print(
        'Закон нарушать нельзя!\n'
        '(1) Утку поймал полицейский и отправил домой\n'
        '(2) Утке повезло и ее не заметили'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return sleep()
    return bar_1()

def bar_1():
    print(
        'Ура! Утка Джо наконец-то добрался до бара и уже успел заказать свой любимый коктейль 🥤!\n'
        'Начать игру заново? (1) Да! (2) Нет.'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step1()
    print('Пока!')

def shop():
    print(
        'Утка Джо промок до нитки и забежал в ближайший магазин.\n'
        '(1) Купить лимон и имбирь и бежать скорее домой пить чай от простуды?\n'
        '(2) Купить Алкоголь для домашней вечеринки!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return home()

def umbrella():
    print(
        'У Джо целая коллекция зонтиков. Какой ему выбрать?\n'
        '(1) С желтыми уточками ⛱ (2) В зеленый горошек (3) С сердечками ☔ (4) Угольно-чёрного цвета'
    )
    option = ''
    options = ['1', '2', '3', '4']
    while option not in options:
        print('Выберите: {}/{}/{}/{}'.format(*options))
        option = input()
    return funny(option)

def funny(x):
    color = ["С желтыми уточками ⛱", "В зеленый горошек", "С сердечками ☔", "Угольно-чёрного цвета"]
    print(
        'Утка-маляр Джо весело шагает со своим зонтиком', color[int(x)-1], 'в бар.\n'
        'Входим? (1) Да! (2) Конечно!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return bar_2()

def bar_2():
    opt = ['Отлично! Какой классный бар!', 'Супер, какое классное местечко!', 'А здесь миленько.']
    x = random.randint(0, 2)
    print(
        opt[x], 'Интересно, а тут есть караоке 🎤?\n'
        '(1) Да. (2) Нет.'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return song()
    return bar_3()

def song():
    print(
        'Какую песню Джо спеть?\n'
        '(1) Алла Пугачева "Миллион алых роз" 🎼 (2) Конечно же "Батарейку"! '
        '(3) Меладзе "Небеса" 🎵 (4) 🎶 "Утка-маляр"!'
    )
    option = ''
    options = ['1', '2', '3', '4']
    while option not in options:
        print('Выберите: {}/{}/{}/{}'.format(*options))
        option = input()
    print('Бар апплодировал стоя утке Джо. Бармен налил Джо коктейль за свой счет.')
    return bar_4()

def bar_3():
    print(
        'Ну и ладно. И так хорошо посидели, пора домой!\n'
        '(1) Нет! (2) Пора!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return sleep()
    return bar_4()

def bar_4():
    print(
        'Джо выпил ещё пару коктейлей 🥤🥤. Джо точно не перебрал?\n'
        '(1) Перебрал, пора домой! (2) Нет, крякнем ещё по одной!'
    )
    option = ''
    options = {'1': True, '2': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return sleep()
    return bar_4()

if __name__ == '__main__':
    step1()