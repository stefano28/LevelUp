from models.user import User
from models.level import Level
from models.setting import Setting
from models.channel import Channel
import discord

class Bot():
    
    state = False

    def set_guild(guild):
        Bot.guild = guild

    def set_client(client):
        Bot.client = client

    def is_ready():
        try:
            f = open('AppData/levels.json', 'r')
        except FileNotFoundError:
            return False
        if(Level.is_empty()):
            return False
        return True

    def turn_on():
        Bot.state = True

    def turn_off():
        Bot.state = False

    def add_users():
        members = Bot.guild.members
        for member in members:
            if not(member.bot):
                User.add(member.id, member.name, 0, Level.get_max_xp(1), 1)

    def add_no_xp_channel(id):
        Channel.add(int(id))

    def get_max_xp(id):
        return User.get_max_xp(id)

    async def add_level(max_xp, reward):
        Level.add(max_xp, reward)

    def get_levels():
        if(Level.is_empty()):
            return 'No levels'
        levels = Level.get_all()
        text = ''
        for level in levels:
            text += 'lvl: ' + str(level['id']) + '   to: ' + str(level['max_xp']) + ' xp' + '   reward: ' + str(level['reward']) + '\n'
        return text
    
    def is_levels_empty():
        return Level.is_empty()

    def clear_levels():
        Level.clear()

    def clear_users():
        User.clear()

    def get_roles():
        roles = Bot.guild.roles
        text = ''
        for role in roles:
            text += role.name + ' ' + str(role.id) + '\n'
        return text

    def get_user_roles(id):
        user = Bot.guild.get_member(id)
        return user.roles

    def get_voice_channels():
        voice_channels = Bot.guild.voice_channels
        text = ''
        for voice_channel in voice_channels:
            text += voice_channel.name + ' ' + str(voice_channel.id) + '\n'
        return text

    def get_text_channels():
        text_channels = Bot.guild.text_channels
        text = ''
        for text_channel in text_channels:
            text += text_channel.name + ' ' + str(text_channel.id) + '\n'
        return text

    def set_comunication_channel_id(comunication_channel_id):
        Setting.set_comunication_channel_id(comunication_channel_id)

    async def send_message(channel_id, user_id, msg):
        member = Bot.guild.get_member(user_id)
        channel = Bot.guild.get_channel(channel_id)
        await channel.send(member.mention + msg)

    async def apply_user_role(user_id, role_id):
        role = Bot.guild.get_role(role_id)
        member = Bot.guild.get_member(user_id)
        await member.add_roles(role)

    async def delete_user_role(user_id, role_id):
        role = Bot.guild.get_role(role_id)
        member = Bot.guild.get_member(user_id)
        await member.remove_roles(role)

    async def get_rank(user_id):
        rank = str(User.get_xp(user_id))
        return rank

    async def get_level(user_id):
        level = str(User.get_level(user_id))
        return level

    def get_reward(level):
        return Level.get_reward(level)

    def get_role_name(role_id):
        role = Bot.guild.get_role(role_id)
        return role.name

    def get_max_level_number():
        return Level.get_max_level_number()

    async def get_top():
        users = User.get_all()
        top_users_id = []
        i = 0
        for user in users:
            i += 1
            top_users_id.append(Bot.guild.get_member(user['id']))
            if(i > 5):
                return top_users_id
        return top_users_id