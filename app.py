import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

from core.bot import Bot
import core.leveling as leveling

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

refresh_rate = 1

client= commands.Bot(command_prefix='.', intents=intents, help_command=None)

cogs = ['cogs.basic', 'cogs.user']

async def update():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    guild = discord.utils.get(client.guilds, name=GUILD)
    while True:
        if(Bot.state):
            await leveling.core(guild)
        await asyncio.sleep(refresh_rate)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    Bot.set_guild(guild)
    Bot.set_client(client)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    Bot.add_users()

@client.event
async def on_client_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Non hai i permessi necessari per eseguire questo comando")
     
for cog in cogs:
    client.load_extension(cog)

client.loop.create_task(update())
client.run(TOKEN)