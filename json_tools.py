import json

def save_game(user_name, n, total_moves):
    
    game_state = {
        'user_name': user_name,
        'field_size': n,
        'total_moves': total_moves,
    }

    with open('save.json', 'w') as save:
        json.dump(game_state, save, indent=4)