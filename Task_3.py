# 3. Создайте программу для игры в ""Крестики-нолики"".


def draw_board(b):   # рисуем игровое поле
    print('-' * 13)
    for i in range(3):
        print('|', b[0 + i * 3], '|' , b[1 + i * 3], '|', b[2 + i * 3], '|')
        print('-' * 13)


def take_move(player_symbol): 
    valid = False
    while not valid:
        player_step = input(f'Куда поставим {player_symbol} ?')
        try:
            player_step = int(player_step)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число? ')
            continue
        if player_step >= 1 and player_step <= 9: 
            if(str(board[player_step - 1]) not in 'XO'):
                board[player_step - 1] = player_symbol
                valid = True
            else: 
                print('Эта клетка уже занята!')
        else:
            print('Некорректный ввод. Введите число от 1 до 9')


def check_win(b): # проверка наличия победителя
    win_lines = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]
    win = ''
    for i in win_lines:
        if b[i[0]] == 'X' and b[i[1]] == 'X' and b[i[2]] == 'X':
            win = 'X'
        if b[i[0]] == 'O' and b[i[1]] == 'O' and b[i[2]] == 'O':
            win = 'O'
    return win


def main_game(b):
    counter = 0
    winner = False
    while not winner:
        draw_board(b)
        if counter % 2 == 0:
            take_move('X')
        else:
            take_move('O')
        counter += 1
        if counter > 4:  # победителя не будет раньше, чем на пятом ходу
            tmp = check_win(b)
            if tmp:
                print(f'\n {tmp} выиграл!')
                winner = True
                break
            if counter == 9:
                print('Ничья!')
                break
    draw_board(b)


print('\nИгра Крестики-Нолики для двух игроков ')
# Инициализация карты
board = [1,2,3,
         4,5,6,
         7,8,9]

main_game(board)
input('Нажмите Enter для выхода!')
