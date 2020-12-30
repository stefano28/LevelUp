from .storage import Storage

class User:

    def add(id, name, xp, max_xp, level):
        if(User.exist(id)):
            return
        users = Storage.read('users.json')
        user = {
            'id': id,
            'name': name,
            'xp': xp,
            'max_xp': max_xp,
            'level': level
        }
        users.append(user)
        Storage.write('users.json', users)

    def exist(id):
        try:
            users = Storage.read('users.json')
        except FileNotFoundError:
            return False

        for user in users:
            if(user['id'] == id):
                return True
        return False

    def increment_xp(id):
        users = Storage.read('users.json')
        for user in users:
            if(user['id'] == id):
                user['xp'] += 1
        Storage.write('users.json', users)

    def get_xp(id):
        users = Storage.read('users.json')
        for user in users:
            if(user['id'] == id):
                return user['xp']
        raise Exception('User not found')

    def get_max_xp(id):
        users = Storage.read('users.json')
        for user in users:
            if(user['id'] == id):
                return user['max_xp']
        raise Exception('User not found')