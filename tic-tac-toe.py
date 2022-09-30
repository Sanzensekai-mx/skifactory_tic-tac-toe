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

def show_actual_field(field):
    print(f"   {' '.join([str(i) for i in range(len(field))])}")
    for idx, seq in enumerate(field):
        print(f'{idx} |{"|".join(seq)}|')

def new_game(field_size=3):
    game_field = [["-" for j in range(field_size)] for i in range(field_size)]
    players_postions = {'Игрок 1': [], 'Игрок 2': []}
    show_actual_field(game_field)


if __name__ == "__main__":
    print(BANNER)
    # all_answers = [answer for group in list(VALID_ANSWER.values()) for answer in group]
    while True:
        yesno = input("Начать игру? -> (y/n)").lower()
        if yesno in VALID_ANSWER['ДА']:
            print('Новая игра...')
            print('Игрок 1 - X\nИгрок 2 - O')
            new_game(field_size=3)

        elif yesno in VALID_ANSWER['НЕТ']:
            print('Выход...')
            sys.exit(0)
    