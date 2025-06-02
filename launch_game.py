from fifteen_game import clear, generate_numb, find_inversions, generate_and_print_field, move_digits, update_matrix
from fifteen_game import mistake_color, main_color, welcome_color, reset_color
import time
from json_tools import save_game, load_game

clear()

welcome_text = (f'''{welcome_color}Добро пожаловать в игру пятнашки!
Вам необходимо ввести размер поля, например, 4 для поля 4x4
при этом размер поля должен быть больше 2х{reset_color} ''')

print(welcome_text)

# выбор игры (новая/старая)
while True:
    try:
        choice = int(input(f'''\n{main_color}Вы хотите начать новую игру или продолжить предыдущую?{reset_color}
        
        1 - новая игра
        2 - продолжить старую игру
                           
        {main_color}Введите число:{reset_color} '''))
        
        if choice == 1:
            clear()
            # проверка ввода имени
            while True:
                user_name = input(f'\n{main_color}Введите ваше имя:{reset_color} ').capitalize()
                if user_name == '':
                    print(f'\n{mistake_color}Вы не ввели имя! {reset_color}\n')
                    time.sleep(1)
                    clear()
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
                        save_game(user_name, n, 0, matrix, empty_cell_row, empty_cell_column, game_status='Новая игра')
                        game_status, total_moves = move_digits(matrix, empty_cell_row, empty_cell_column, n, user_name, mistake_color, reset_color, choice)
                        save_game(user_name, n, total_moves, matrix, empty_cell_row, empty_cell_column, game_status)
                        break
                except ValueError:
                    print(f'\n{mistake_color}Введите корректное значение для поля (например, 4х4){reset_color}')
            
        elif choice == 2:
            clear()
            if load_game() == None:
                time.sleep(3)
                clear()
                continue
            else:
                user_name, field_size, total_moves, matrix, empty_cell_position, game_status = load_game()
                update_matrix(matrix, total_moves, field_size, user_name)
                empty_cell_row, empty_cell_column = empty_cell_position
                move_digits(matrix, empty_cell_row, empty_cell_column, field_size, user_name, mistake_color, reset_color, choice)
                break
            
    except ValueError:
        print(f'\n{mistake_color}Необходимо ввести 1 или 2{reset_color}')
        time.sleep(3)
        clear()
        print(welcome_text)

