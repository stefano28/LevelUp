from models.user import User

def manage_users_file(members):
    for member in members:
        User.add(member.id, member.name, 0, 5, 1)