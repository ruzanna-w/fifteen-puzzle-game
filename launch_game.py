from fifteen_game import clear, generate_numb, find_inversions, generate_and_print_field, move_digits

clear()
print('''\033[35mДобро пожаловать в игру пятнашки!
Вам необходимо ввести размер поля, например, 4 для поля 4x4
при этом размер поля должет быть больше 2 \033[0m''')


while True:
    try:
        n = int(input('\nВведите размер поля: '))
        if n <= 2:
            print('Размер поля должен быть не меньше 3х3')
            continue
        else:
            clear()
            print(f'Вы выбрали размер {n}x{n}\n')
            numbers = generate_numb(n)
            solvability_check = find_inversions(n, numbers)
            matrix, empty_cell_row, empty_cell_column = generate_and_print_field(n, numbers, solvability_check)
            move_digits(matrix, empty_cell_row, empty_cell_column, n)
            break
    except ValueError:
        print('Введите корректное значение для поля (например, 4х4)')