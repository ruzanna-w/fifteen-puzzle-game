import random, time
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

def update_matrix(matrix): 
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
    
# ввод координатов
def move_digits(matrix, empty_cell_row, empty_cell_column): 

    while True:
        move_number = int(input('напишите число, которое хотите передвинуть на пустую клетку: '))

        # поиск позиции числа, которое хочу подвинуть на пустую ячейку
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == move_number:
                    number_cell_row = i
                    number_cell_col = j
                    break

        # определить можно передвинуть цифру на пустую ячейку или нет (строго по вертикали или горизонтали)
        if abs(empty_cell_row - number_cell_row) == 1 and (empty_cell_column == number_cell_col)\
            or abs(empty_cell_column - number_cell_col) == 1 and (empty_cell_row == number_cell_row):
            # меняем местами ячейки
            matrix[empty_cell_row][empty_cell_column], matrix[number_cell_row][number_cell_col] = matrix[number_cell_row][number_cell_col], matrix[empty_cell_row][empty_cell_column]
            matrix, empty_cell_row, empty_cell_column = update_matrix(matrix) # обновляю матрицу
        else:
            print('Это число нельзя передвинуть. Введите другое число, которое находится рядом с пустой клеткой')