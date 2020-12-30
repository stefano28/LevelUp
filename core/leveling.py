
import discord
import core.settings as settings
from models.user import User
import json

def get_users_in_voice_channels(voice_channels):
    active_users = []
    for voice_channel in voice_channels:
        for user in voice_channel.members:
            active_users.append(user)
    return active_users

def increment_xp(active_users):
    for user in active_users:
        User.increment_xp(user.id)
        #check_level(user.id)

def check_level(user_id):
    if(User.get_xp(user_id) < User.get_max_xp(user_id)):
        return
    
    f = open('AppData/levels.json', 'r')
    levels = json.load(f)
    f.close()
    if(user['level'] < len(levels)):
        user['level'] += 1
        for level in levels:
            if(level['id'] == user['level']):
                user['max_xp'] = level['max_xp']
        print("Level Up!!!")
    return user

def core(guild):
    voice_channels = settings.get_xp_channels(guild)
    active_users = get_users_in_voice_channels(voice_channels)
    increment_xp(active_users)