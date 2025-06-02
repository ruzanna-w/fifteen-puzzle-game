import json

def save_game(user_name, n, total_moves, matrix, empty_cell_row, empty_cell_column):
    
    game_state = {
        'user_name': user_name,
        'field_size': n,
        'total_moves': total_moves,
        'matrix': matrix,
        'empty_cell_position': [empty_cell_row, empty_cell_column]
    }

    with open('save.json', 'w') as save:
        json.dump(game_state, save, indent=4)


def load_game():
    try:
        with open('save.json', 'r') as save:
            game_data = json.load(save)
            user_name = game_data['user_name']
            field_size = game_data['field_size']
            total_moves = game_data['total_moves']
            matrix = game_data['matrix']
            empty_cell_position = game_data['empty_cell_position']
            return user_name, field_size, total_moves, matrix, empty_cell_position
    except FileNotFoundError:
        print('Нет сохраненной игры')