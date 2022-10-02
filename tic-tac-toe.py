import sys

BANNER = """
#######                                                              
   #    #  ####        #####   ##    ####        #####  ####  ###### 
   #    # #    #         #    #  #  #    #         #   #    # #      
   #    # #      #####   #   #    # #      #####   #   #    # #####  
   #    # #              #   ###### #              #   #    # #      
   #    # #    #         #   #    # #    #         #   #    # #      
   #    #  ####          #   #    #  ####          #    ####  ###### 
"""

VALID_ANSWER = {"ДА": ['да', 'y', 'yes', 'д'],
                "НЕТ": ['нет', 'n', 'no', 'н']}

# game_field = []

# players_postions = {}


def get_field_size_max_move(field_size):
    return int(str(field_size - 1) + str(field_size - 1))


#    0 1 2
# 0 |-|-|-|
# 1 |-|-|-|
# 2 |-|-|-|
def show_actual_field(field):
    print(f"   {' '.join([str(i) for i in range(len(field))])}")
    for idx, seq in enumerate(field):
        print(f'{idx} |{"|".join(seq)}|')


def check_tied(field):
    pass


def check_winner(field): # rows = field
    rows = field
    columns = [list(row) for row in zip(*rows)] # Транспорирование матрицы 
    first_diag = [row[i] for i, row in enumerate(rows)]
    second_diag = [col[j] for j, col in enumerate(columns)]
    result_combos =[list(set(i)) for i in [*rows, *columns, first_diag, second_diag]]
    symbols = ['x', 'o']
    for sym in symbols:
        for res in result_combos:
            if sym == res[0] and len(res) == 1:
                return sym
    return


def player_move(player_id, positions, field):
    print(f'Ход {"первого" if player_id == 1 else "второго"} игрока..')
    print('Введите координаты ячейки для хода, где первое число - номер строчки, а второе - номер столбца.')
    print('q - для выхода из игры.')
    input_move = input('-> ')
    if input_move == 'q':
        sys.exit(0)
    elif not input_move.isdigit():
        print('!!! Введены неправильные символы, координаты передаются двухзначным числом')
        return False, positions, field
    input_move = int(input_move)
    positions_list = [i for j in list(positions.values()) for i in j]
    if input_move > get_field_size_max_move(len(field)) or input_move in positions_list:
        print('!!! Неправильный ход, повторите ввод раз')
        return False, positions, field
    positions[player_id].append(input_move)
    field[input_move // 10][input_move % 10] = 'x' if player_id == 1 else 'o'
    return True, positions, field


def move_queue_gen():
    while True:
        for i in [1, 2]:
            yield i


def new_game(field_size=3):
    game_field = [["-" for j in range(field_size)] for i in range(field_size)]
    players_postions_by_id = {1: [], 2: []}
    # show_actual_field(game_field)
    move_queue = iter(move_queue_gen()) # очередность ходов 1,2,1...
    who_move = next(move_queue)
    while True:
        show_actual_field(game_field)
        is_correct_move, players_postions_by_id, game_field = player_move(who_move, players_postions_by_id, game_field)
        winner = check_winner(game_field)
        if winner:
            show_actual_field(game_field)
            return winner
        if is_correct_move:
            who_move = next(move_queue)
            continue
        else:
            continue


if __name__ == "__main__":
    print(BANNER)
    player_sym = {'x': 'Игрок 1 (X)', 'o': 'Игрок 2 (O)'}
    # all_answers = [answer for group in list(VALID_ANSWER.values()) for answer in group]
    while True:
        yesno = input("Начать игру? (y/n) -> ").lower()
        if yesno in VALID_ANSWER['ДА']:
            print('Новая игра...')
            print('Игрок 1 - X\nИгрок 2 - O')
            game_result = new_game(field_size=3)
            if game_result:
                print(f'Победил {game_result}!!!')
            # Обработка ничьи
            new_game = input('Новая игра? (y/n) -> ').lower()
            if new_game in VALID_ANSWER['ДА']:
                continue
            elif new_game in VALID_ANSWER['НЕТ']:
                print('Выход...')
                sys.exit(0)
        elif yesno in VALID_ANSWER['НЕТ']:
            print('Выход...')
            sys.exit(0)
    