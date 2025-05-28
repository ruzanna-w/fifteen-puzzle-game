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
    
    solvability_check = count + free_field_position
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
                    if numbers[i * n + j] == 0:
                        empty_position_row = i # найти координаты пустой ячейки (ряд)
                        empty_position_column = j # найти координаты пустой ячейки (строка)
                matrix.append(row)
            print()
            for row in matrix:
                for i in row:
                    if i == 0:
                        i = ''
                        print(f'{i:^5}', end = '')  # замена 0 на пустую клетку
                    else:
                        print(f'{i:^5}', end = '')  # форматирование строки 1 - более
                print()
                print()
            break
        else:
            numbers = generate_numb(n)
            solvability_check = find_inversions(n, numbers)
    
    return matrix, empty_position_row, empty_position_column

# ввод координатов
def move_digits(matrix, empty_position_row, empty_position_column):

    while True:
        move_number = int(input('напишите число, которое хотите передвинуть на пустую клетку: '))

        # поиск позиции числа, которое хочу подвинуть на пустую ячейку
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                number_to_move = matrix[i][j]
                if number_to_move == move_number:
                    row_num_position = i
                    column_num_position = j
                    break

        # определить можно передвинуть цифру на пустую ячейку или нет (строго по вертикали или горизонтали)
        if abs(empty_position_row - row_num_position) == 1 and (empty_position_column == column_num_position)\
            or abs(empty_position_column - column_num_position) == 1 and (empty_position_row == row_num_position):
            print('Можно передвинуть')
        else:
            print('Это число нельзя передвинуть. Введите другое число')