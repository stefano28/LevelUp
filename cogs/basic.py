import discord
from discord.ext import commands
from core.bot import Bot

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def start(self, ctx):
        if(Bot.state):
            embed=discord.Embed(title="Levelup", description="levelup è già in funzione", colour = discord.Colour.blue())
            await ctx.send(embed = embed)
            return
        if(Bot.is_ready()):
            Bot.turn_on()
            embed=discord.Embed(title="Levelup", description="levelup ora è in funzione", colour = discord.Colour.blue())
        else:
            embed=discord.Embed(title="Levelup", description="Il bot non può essere avviato\n.help per la lista degli aiuti", colour = discord.Colour.blue())
        
        await ctx.send(embed = embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def stop(self, ctx):
        if not(Bot.state):
            await ctx.send('Il bot è già fermo')
            return
        Bot.turn_off()
        await ctx.send('Il bot è stato fermato')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def add_level(self, ctx, max_xp, reward):
        if(Bot.state):
            await ctx.send('Il bot è in funzione, per aggiungere un livello devi prima fermarlo con .stop')
            return
        await Bot.add_level(max_xp, reward)
        await ctx.send('Livello aggiunto con successo')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clear_levels(self, ctx):
        Bot.clear_levels()
        await ctx.send('Livelli eliminati con successo')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clear_users(self, ctx):
        Bot.clear_users()
        await ctx.send('Utenti eliminati con successo')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def levels(self, ctx):
        await ctx.send(Bot.get_levels())

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def roles(self, ctx):
        await ctx.send(Bot.get_roles())

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def add_users(self, ctx):
        if(Bot.is_levels_empty()):
            await ctx.send("Devi prima inserire i livelli")
            return
        Bot.add_users()
        await ctx.send("Tutti gli utenti del server tranne i bot sono stati aggiunti con successo")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def add_no_xp_channel(self, ctx, id):
        Bot.add_no_xp_channel(id)
        await ctx.send("Tutti i canali da escludere sono stati aggiunti con successo")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def get_voice_channels(self, ctx):
        await ctx.send(Bot.get_voice_channels())

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def get_text_channels(self, ctx):
        await ctx.send(Bot.get_text_channels())

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def set_comunication_channel(self, ctx, comunication_channel_id):
        Bot.set_comunication_channel_id(comunication_channel_id)
        await ctx.send('Canale di comunicazione principale settato con successo')

def setup(client):
    client.add_cog(Basic(client))