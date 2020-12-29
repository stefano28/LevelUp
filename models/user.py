from .storage import Storage

class User:

    def add(id, name, xp, max_xp, level):
        if(User.exist(id)):
            return
        user = {
            'id': id,
            'name': name,
            'xp': xp,
            'max_xp': max_xp,
            'level': level
        }
        Storage.write('users.json', user)

    def exist(id):
        try:
            users = Storage.read('users.json')
        except FileNotFoundError:
            return False

        for user in users:
            if(user['id'] == id):
                return True
        return False

    def remove(id):
        return

    def get_max_xp(id):
        users = Storage.read('users.json')
        for user in users:
            if(user['id'] == id):
                return user['max_xp']
        raise Exception('User not found')