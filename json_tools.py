import json
import os

def save_game(user_name, n, total_moves, matrix, empty_cell_row, empty_cell_column, game_status):
    
    game_state = {
        'user_name': user_name,
        'field_size': n,
        'total_moves': total_moves,
        'matrix': matrix,
        'empty_cell_position': [empty_cell_row, empty_cell_column],
        'game_status': game_status
    }

    with open('save.json', 'w') as save:
        json.dump(game_state, save, indent=4, ensure_ascii=False)


def load_game():
    try:
        with open('save.json', 'r') as save:
            game_data = json.load(save)
            user_name = game_data['user_name']
            field_size = game_data['field_size']
            total_moves = game_data['total_moves']
            matrix = game_data['matrix']
            empty_cell_position = game_data['empty_cell_position']
            game_status = game_data['game_status']
            return user_name, field_size, total_moves, matrix, empty_cell_position, game_status
    except FileNotFoundError:
        print('Нет сохраненной игры')

def delete_game():
    try:
        with open('save.json') as victory:
            game = json.load(victory)

        if game['game_status'] == 'Победа':
            os.remove('save.json')
        else:
            print('Игра ещё не завершена')

    except FileNotFoundError:
        print('Файл сохранения не найден')
