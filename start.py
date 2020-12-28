import json

def manage_users_file(members):
    f = open('AppData/users.json', 'w+')
    users = []
    for member in members:
        user = {
            'id': member.id,
            'name': member.name,
            'xp': 0,
            'level': 0
        }
        users.append(user)
    f.write(json.dumps(users))
    f.close()