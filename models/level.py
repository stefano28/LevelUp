from .storage import Storage

class Level:

    def add(max_xp, reward):
        if(Level.is_empty()):
            levels = []
            last_id = 0
        else:
            levels = Storage.read('levels.json')
            last_id = levels[len(levels) - 1]['id']
        level = {
            'id': last_id + 1,
            'max_xp': int(max_xp),
            'reward': int(reward)
        }
        levels.append(level)
        Storage.write('levels.json', levels)
        return True

    def exist(id):
        try:
            levels = Storage.read('levels.json')
        except FileNotFoundError:
            return False
        for level in levels:
            if(level['id'] == int(id)):
                return True
        return False

    def get_all():
        levels = Storage.read('levels.json')
        return levels

    def get_reward(id):
        levels = Storage.read('levels.json')
        for level in levels:
            if(level['id'] == id):
                return level['reward']

    def get_max_xp(id):
        levels = Storage.read('levels.json')
        for level in levels:
            if(level['id'] == id):
                return level['max_xp']

    def get_max_level_number():
        levels = Storage.read('levels.json')
        return len(levels)

    def clear():
        levels = []
        Storage.write('levels.json', levels)

    def is_empty():
        levels = Storage.read('levels.json')
        return len(levels) < 1