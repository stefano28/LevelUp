import json

def manage_users_file(members):
    try:
        f = open('AppData/users.json', 'x')
    except FileExistsError:
        return
    users = []
    for member in members:
        user = {
            'id': member.id,
            'name': member.name,
            'xp': 0,
            'max_xp': 5,
            'level': 1
        }
        users.append(user)
    f.write(json.dumps(users, indent=4))
    f.close()