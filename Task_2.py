# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from random import randint, choice

# 1. Человек против человека


def play_game_0(a, b, pl, mes):
    count = choose_first_move()
    print(f'\nПервый ход достается игроку {pl[count % 2]}')
    while a > 0:
        print(f'\n{pl[count % 2]}, {random.choice(mes)}') # переходы хода и взятие конфет
        move = int(input())
        if move < 1 or move > b:
            print(f'Можно взять не более {b} конфет и не менее 1. Текущее количество конфет: {a}')
            attempt = 3
            while attempt > 0:
                if move <= a and move <= b and move > 0:
                    break
                print(f'Попробуйте еще раз, у Вас есть {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print('Очень жаль, у Вас не оcталось попыток. Game over!')
        a -= move
        if a > 0:
            print(f'Количество оставшихся конфет: {a}')
        else:
            print('Все конфеты закончились')
        count += 1
    return pl[not count % 2]

# 2. Игра с компьютером
def play_game_1(a, b, pl, mes):
    count = choose_first_move()
    print(f'\nПервый ход достается игроку {pl[count]}!')
    while a > 0:
        if count % 2:
            move = randint(1, b)
            print(f'\nБот-сластена забрал {move} конфет')
        else:
            print(f'\n{pl[0]}, {choice(mes)}') 
            move = int(input())
            if move < 1 or move > b:
                print(f'Можно взять не более {b} конфет и не менее 1. Текущее количество конфет: {a}')
                attempt = 3
                while attempt > 0:
                    if move <= a and move <= b and move > 0:
                        break
                    print(f'Попробуйте еще раз, у Вас есть {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print('Очень жаль, у Вас не оcталось попыток. Game over!')
        a -= move
        if a > 0:
            print(f'Количество оставшихся конфет: {a}')
        else:
            print('Все конфеты закончились')
        count += 1
    return pl[count % 2]

# 2. Игра с умным компьютером
def play_game_2(a, b, pl, mes):
    count = choose_first_move()
    print(f'\nПервый ход достается игроку {pl[count]}!')
    while a > 0:
        if count % 2:
            move = a % (b + 1)
            if move == 0:
                move = randint(1, b)
            print(f'\nБот-сластена забрал {move} конфет')
        else:
            print(f'\n{pl[0]}, {choice(mes)}') 
            move = int(input())
            if move < 1 or move > b:
                print(f'Можно взять не более {b} конфет и не менее 1. Текущее количество конфет: {a}')
                attempt = 3
                while attempt > 0:
                    if move <= a and move <= b and move > 0:
                        break
                    print(f'Попробуйте еще раз, у Вас есть {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print('Очень жаль, у Вас не оcталось попыток. Game over!')
        a -= move
        if a > 0:
            print(f'Количество оставшихся конфет: {a}')
        else:
            print('Все конфеты закончились')
        count += 1
    return pl[not count % 2]


def choose_first_move():  # определение игрока, делающего ход первым
    return randint(0, 1)


def introduce_players(d):
    if d == 0:
        player1 = input('Имя первого игрока: ')
        player2 = input('Имя второго игрока: ')
        return[player1, player2]
    else:
        player1 = input('Как Вас зовут? ')
        player2 = 'Бот-сластена'
        print(f'\nЗа компьютер играет {player2}')
        return[player1, player2]


def game(d):
    if d == 0:
        winner = play_game_0(n, m, players, messages)
    elif d == 1:
        winner = play_game_1(n, m, players, messages)
    elif d == 2:
        winner = play_game_2(n, m, players, messages)

    if not winner:
        print('У нас нет победителя!')
    else: print(f'Поздравляю! Победил {winner}! Ему достаются все конфеты!')


greeting = ('\nЗдравствуйте! Это игра "Забери все конфеты!"'
    '\nОсновные правила игры: '
    '\nНам будет дано некоторое количество конфет, ' 
    '\nза один ход мы можем взять не более определенного количества, о котором мы договоримся.'
    '\nПраво первого хода будет определено случайным образом.'
    '\nИтак, начнем!\n')


messages = ['Ваша очередь брать конфеты', 'Возьмите конфеты', 
            'Сколько конфет возьмете?', 'Берите конфеты, не стесняйтесь!', 'Ваш ход!', 'Берите конфетки', 'Пора брать конфетки!']

print(greeting)

n = int(input('Сколько конфет будем разыгрывать? '))
m = int(input('Сколько конфет будем брать за один ход? '))
lvl = int(input('Выберите уровень сложности: '
        '\n0 - Игра с человеком'
        '\n1 - Игра с компьютером'
        '\n2 - Игра с умным компьютером \n'))

players = introduce_players(lvl)
winner = game(lvl)
