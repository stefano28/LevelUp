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

    def add_channel(id):
        Channel.add(voice_channel.id)

    def add_level(max_xp, reward):
        return Level.add(max_xp, reward)

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

    def get_roles():
        roles = Bot.guild.roles
        text = ''
        for role in roles:
            text += role.name + ' ' + str(role.id) + '\n'
        return text

    def get_voice_channels():
        voice_channels = Bot.guild.voice_channels
        text = ''
        for voice_channel in voice_channels:
            text += voice_channel.name + ' ' + str(voice_channel.id) + '\n'
        return text

    def set_comunication_channel_id(comunication_channel_id):
        Setting.set_comunication_channel_id(comunication_channel_id)

    async def send_message(channel_id, msg):
        channel = Bot.client.get_channel(channel_id)
        print(msg)
        #await channel.send_message(msg)