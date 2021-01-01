import discord
from discord.ext import commands
from core.bot import Bot

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Start bot
    @commands.command()
    async def start(self, ctx):
        if(Bot.state):
            await ctx.send('Il bot è già acceso cazzo rompi i coglioni')
            return
        if(Bot.is_ready()):
            Bot.turn_on()
            await ctx.send('Levelup - discord leveling bot \nIl bot è stato acceso')
        else:
            await ctx.send('Per fare funzionare il bot devi digitare i seguenti comandi (in questo ordine):\n`.add_level max_xp id_ruolo_ricompensa` per aggiungere un livello\n`.add_users` per caricare la lista degli utenti nel bot escludendo dei ruoli (opzionale)')

    #Stop bot
    @commands.command()
    async def stop(self, ctx):
        if not(Bot.state):
            await ctx.send('Il bot è già fermo cazzo rompi i coglioni')
            return
        Bot.turn_off()
        await ctx.send('Il bot è stato fermato')

    #Add new level
    @commands.command()
    async def add_level(self, ctx, max_xp, reward):
        if(Bot.state):
            await ctx.send('Il bot è in funzione, per aggiungere un livello devi prima fermarlo con .stop, testa di cazzo')
            return
        if(Bot.add_level(max_xp, reward)):
            await ctx.send('Livello aggiunto con successo')

    #Remove all levels
    @commands.command()
    async def clear_levels(self, ctx):
        Bot.clear_levels()
        await ctx.send('Livelli eliminati con successo')

    #Get the list of all levels
    @commands.command()
    async def levels(self, ctx):
        await ctx.send(Bot.get_levels())

    #Get the list of all roles
    @commands.command()
    async def roles(self, ctx):
        await ctx.send(Bot.get_roles())

    #Add all users escept bots
    @commands.command()
    async def add_users(self, ctx):
        if(Bot.is_levels_empty()):
            await ctx.send("Devi prima inserire i livelli, faccia di merda")
            return
        Bot.add_users()
        await ctx.send("Tutti gli utenti del server tranne i bot sono stati aggiunti con successo")

    @commands.command()
    async def add_channel(self, ctx, id):
        Bot.add_channels()
        await ctx.send("Tutti i canali da escludere sono stati aggiunti con successo")

    @commands.command()
    async def get_voice_channels(self, ctx):
        await ctx.send(Bot.get_voice_channels())

    @commands.command()
    async def set_comunication_channel(self, ctx, comunication_channel_id):
        Bot.set_comunication_channel_id(comunication_channel_id)
        await ctx.send('Canale di comunicazione principale settato con successo')

def setup(client):
    client.add_cog(Basic(client))