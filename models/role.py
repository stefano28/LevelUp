import json
from .storage import Storage

class Role:

    def add(id, name):
        roles = Storage.read('roles.json')
        role = {
            'id': id,
            'name': name
        }
        roles.append(role)
        Storage.write('roles.json', roles)