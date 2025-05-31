from fifteen_game import clear, generate_numb, find_inversions, generate_and_print_field, move_digits
from fifteen_game import mistake_color, main_color, welcome_color, reset_color
import time
from json_tools import save_game

clear()

welcome_text = (f'''{welcome_color}Добро пожаловать в игру пятнашки!
Вам необходимо ввести размер поля, например, 4 для поля 4x4
при этом размер поля должен быть больше 2х{reset_color} ''')

print(welcome_text)

# проверка ввода имени
while True:
    user_name = input(f'\n{main_color}Введите ваше имя:{reset_color} ').capitalize()
    if user_name == '':
        print(f'\n{mistake_color}Вы не ввели имя! {reset_color}\n')
        time.sleep(1)
        clear()
        print(welcome_text)
    else:
         break

# проверка ввода размера поля
while True:
    try:
        n = int(input(f'\n{main_color}Введите размер поля:{reset_color} '))
        if n <= 2:
            print(f'\n{mistake_color}Размер поля должен быть не меньше 3х3{reset_color}')
        else:
            clear()
            print(f'{main_color}Ваше имя:{reset_color} {user_name}\n')
            print(f'{main_color}Размер поля:{reset_color} {n}x{n}\n')
            numbers = generate_numb(n)
            solvability_check = find_inversions(n, numbers)
            matrix, empty_cell_row, empty_cell_column = generate_and_print_field(n, numbers, solvability_check)
            save_game(user_name, n, 0)
            total_moves = move_digits(matrix, empty_cell_row, empty_cell_column, n, user_name, mistake_color, reset_color)
            save_game(user_name, n, total_moves)
            break
    except ValueError:
        print(f'\n{mistake_color}Введите корректное значение для поля (например, 4х4){reset_color}')