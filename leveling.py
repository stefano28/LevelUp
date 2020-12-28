
import discord
import settings
import json

def get_users_in_voice_channels(voice_channels):
    active_users = []
    for voice_channel in voice_channels:
        for user in voice_channel.members:
            active_users.append(user)
    return active_users

def increment_xp(active_users):
    f = open('AppData/users.json', 'r')
    json_users = json.load(f)
    f.close()
    for user in active_users:
        for json_user in json_users:
            if(user.id == json_user['id']):
                json_user['xp'] = json_user['xp'] + 1
    f = open('AppData/users.json', 'w')
    json.dump(json_users, f)
    f.close()


def core(guild):
    voice_channels = settings.get_xp_channels(guild)
    active_users = get_users_in_voice_channels(voice_channels)
    increment_xp(active_users)