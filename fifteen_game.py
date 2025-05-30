import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# числа для рандомного распределения в пятнашек
def generate_numb(n):
    numbers = []
    for i in range(n*n):
        numbers.append(i)
    random.shuffle(numbers)
    return numbers

# определить возможно ли решить головоломку 
def find_inversions(n, numbers):
    inversions = []
    count = 0
    for num in range(len(numbers)):
        if numbers[num] == 0:
            index_position_zero = num # определить где будет 0(пустая клетка)
        else:
            inversions.append(numbers[num])
    
    # определить в какой строке находится пустая клетка или 0
    free_field_position = index_position_zero // n + 1
        
    # сравниваем числа в массиве
    for i in range(len(inversions)):
        for j in range(i + 1, len(inversions)):
            if inversions[i] < inversions[j]:
                pass
            else:
                count += 1
    
    if n % 2 == 0: # разрешимость пазла для четного размера поля (4х4)
        solvability_check = count + free_field_position
    elif n % 2 == 1: # разрешимость пазла для нечетного размера поля (3х3)
        solvability_check = count

    return solvability_check
    
# создать поле для игры
def generate_and_print_field(n, numbers, solvability_check):
    
    while True:
        if solvability_check % 2 == 0:
            matrix = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(numbers[i * n + j])
                matrix.append(row)
            print()
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col] == 0:
                        print(f'{'':^5}', end = '')  # замена 0 на пустую клетку
                        empty_cell_row = row # найти координаты пустой ячейки (ряд)
                        empty_cell_column = col # найти координаты пустой ячейки (строка)
                    else:
                        print(f'{matrix[row][col]:^5}', end = '')  # форматирование строки 1 - более
                print()
                print()
            break
        else:
            numbers = generate_numb(n)
            solvability_check = find_inversions(n, numbers)
    
    return matrix, empty_cell_row, empty_cell_column

def update_matrix(matrix, total_moves): 

    print(f'Количество шагов: {total_moves}')
    print()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                empty_cell_row = row # найти координаты пустой ячейки (ряд)
                empty_cell_column = col # найти координаты пустой ячейки (строка)
                print(f'{'':^5}', end = '')  # замена 0 на пустую клетку
            else:
                print(f'{matrix[row][col]:^5}', end = '')  # форматирование строки 1 - более
        print()
        print()
    
    return matrix, empty_cell_row, empty_cell_column

def is_win(matrix, n):
    
    check_win = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                pass
            else:
                check_win.append(matrix[i][j])

    count = 0
    # проверка инверсий
    for r in range(len(check_win)):
        for c in range(r + 1, len(check_win)):
            if check_win[r] < check_win[c]:
                pass
            else:
                count += 1

    # найти позицию 0
    win_zero_position = False
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if matrix[a][b] == 0:
                if a == n - 1 and b == n - 1:
                    win_zero_position = True

    # проверка победы
    if count == 0 and win_zero_position:
        print('Поздравляю вы выйграли игру!')
        return True
    
        
# ввод координатов
def move_digits(matrix, empty_cell_row, empty_cell_column, n): 

    total_moves = 0

    while True:
        try:
            move_number = int(input('Введите число, которое хотите передвинуть на пустую клетку: '))

            if 1 <= move_number < n*n:
                total_moves += 1
                # поиск позиции числа, которое хочу подвинуть на пустую ячейку
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        if matrix[i][j] == move_number:
                            number_cell_row = i
                            number_cell_col = j
            else:
                print('Такого числа на поле нет')
                continue

            # определить можно передвинуть цифру на пустую ячейку или нет (строго по вертикали или горизонтали)
            if abs(empty_cell_row - number_cell_row) == 1 and (empty_cell_column == number_cell_col)\
                or abs(empty_cell_column - number_cell_col) == 1 and (empty_cell_row == number_cell_row):
                # меняем местами ячейки
                clear()
                matrix[empty_cell_row][empty_cell_column], matrix[number_cell_row][number_cell_col] = matrix[number_cell_row][number_cell_col], matrix[empty_cell_row][empty_cell_column]
                matrix, empty_cell_row, empty_cell_column = update_matrix(matrix, total_moves) # обновляю матрицу
                if is_win(matrix, n):
                    break
            else:
                print('Это число нельзя передвинуть. Введите другое число, которое находится рядом с пустой клеткой')
                continue

        except ValueError:
            print(f'Введите число от 1 до {n*n - 1}')
    
    return total_moves