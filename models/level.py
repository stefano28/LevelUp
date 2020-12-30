from .storage import Storage

class Level:

    def add(id, max_xp, reward):
        if(Level.exist(id)):
            return
        levels = Storage.read('levels.json')
        level = {
            'id': id,
            'max_xp': name,
            'reward': xp
        }
        levels.append(level)
        Storage.write('levels.json', levels)

    def exist(id):
        try:
            users = Storage.read('levels.json')
        except FileNotFoundError:
            return False

        for level in levels:
            if(level['id'] == id):
                return True
        return False