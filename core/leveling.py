
import discord
from models.user import User
from models.level import Level
from models.setting import Setting
from models.channel import Channel
from core.bot import Bot
import json

def get_users_in_voice_channels(voice_channels):
    active_users = []
    for voice_channel in voice_channels:
        if not(Channel.exist(voice_channel.id)):
            for user in voice_channel.members:
                active_users.append(user)
    return active_users

async def increment_xp(active_users):
    for user in active_users:
        User.increment_xp(user.id)
        await check_level(user.id)

async def check_level(user_id):
    if(User.get_xp(user_id) < User.get_max_xp(user_id)):
        return
    if(User.get_level(user_id) < Level.get_max_level_number()):
        while(User.get_xp(user_id) > User.get_max_xp(user_id)):
            if(User.get_level(user_id) < Level.get_max_level_number()):
                await levelup_notification(user_id)
                await edit_user_role(user_id)
                User.increment_level(user_id)
                level_number = User.get_level(user_id)
                level_max_xp = Level.get_max_xp(level_number)
                User.set_max_xp(user_id, level_max_xp)
            elif(User.get_level(user_id) == Level.get_max_level_number()):
                await levelup_notification(user_id)
                await edit_user_role(user_id)
                break
    elif(User.get_xp(user_id) == User.get_max_xp(user_id)):
        await levelup_notification(user_id)
        await edit_user_role(user_id)
        
async def edit_user_role(user_id):
    level_id = User.get_level(user_id)
    if level_id > 1:
        role_prev_id = Level.get_reward(level_id - 1)
        user_roles = Bot.get_user_roles(user_id)
        for role in user_roles:
            if(role.id == role_prev_id):
                await Bot.delete_user_role(user_id, role.id)
    role_id = Level.get_reward(level_id)
    await Bot.apply_user_role(user_id, role_id)

async def levelup_notification(user_id):
        name = User.get_name(user_id)
        level = User.get_level(user_id)
        await Bot.send_message(Setting.get_comunication_channel_id(), user_id, ' hai completato il livello ' + str(level) + '!')

async def core(guild):
    voice_channels = guild.voice_channels
    active_users = get_users_in_voice_channels(voice_channels)
    await increment_xp(active_users)