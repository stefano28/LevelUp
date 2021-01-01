
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
        User.increment_level(user_id)
        level_number = User.get_level(user_id)
        level_max_xp = Level.get_max_xp(level_number)
        User.set_max_xp(user_id, level_max_xp)
        await edit_user_role(user_id)
        await levelup_notification(user_id)

async def edit_user_role(user_id):
    level_id = User.get_level(user_id)
    role_id = Level.get_reward(level_id)
    await Bot.apply_user_role(user_id, role_id)

async def levelup_notification(user_id):
        name = User.get_name(user_id)
        level = User.get_level(user_id)
        await Bot.send_message(Setting.get_comunication_channel_id(), '@' + name + ' hai raggiunto il livello ' + str(level))

async def core(guild):
    voice_channels = guild.voice_channels
    active_users = get_users_in_voice_channels(voice_channels)
    await increment_xp(active_users)