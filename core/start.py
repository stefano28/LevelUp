from models.user import User
from models.level import Level
from models.role import Role

class Start():
    
    state = False

    def is_ready():
        try:
            f = open('AppData/levels.json', 'r')
        except FileNotFoundError:
            return False
        return state

    def turn_on():
        state = True

    def turn_off():
        state = False

    def boot(guild):
        Start.manage_roles_file(guild.roles)
        Start.manage_users_file(guild.members)

    def manage_users_file(members):
        for user in members:
            User.add(user.id, user.name, 0, 5, 1)
        
    def manage_roles_file(roles):
        for role in roles:
            Role.add(role.id, role.name)

    def add_level(id, max_xp, reward):
        Level.add(id, max_xp, reward)

    def ask_levels():
        return 0