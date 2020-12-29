import os
import asyncio
import discord
from dotenv import load_dotenv

import core.start as start
import core.leveling as leveling

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

async def update():
    await client.wait_until_ready()
    await asyncio.sleep(5)
    guild = discord.utils.get(client.guilds, name=GUILD)
    while True:
        leveling.core(guild)
        await asyncio.sleep(1)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    start.manage_users_file(guild.members)

client.loop.create_task(update())
client.run(TOKEN)
