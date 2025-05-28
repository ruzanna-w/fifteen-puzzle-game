from fifteen_game import * 

clear()
print('''\033[35mДобро пожаловать в игру пятнашки!
Вам необходимо ввести размер поля, например, 4 для поля 4x4
при этом размер поля должет быть больше 2 \033[0m''')

n = int(input('\nВведите размер поля: '))

while True:
    if n <= 2:
        print('Размер поля должен быть не меньше 3х3')
        n = int(input('\nВведите размер поля: '))
    else:
        clear()
        print(f'Вы выбрали размер {n}x{n}\n')
        numbers = generate_numb(n)
        solvability_check = find_inversions(n, numbers)
        matrix, empty_position_row, empty_position_column = generate_and_print_field(n, numbers, solvability_check)
        move_digits(matrix, empty_position_row, empty_position_column)
        break