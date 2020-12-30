import discord
from discord.ext import commands
from core.start import Start

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self, ctx):
        if(Start.state):
            await ctx.send('Il bot è già acceso cazzo rompi i coglioni')
            return
        if(Start.is_ready()):
            Start.turn_on
            await ctx.send('Levelup - discord leveling bot \nIl bot è stato acceso')
        else:
            await ctx.send('Non hai definito nessun livello \nPer definirlo usa: \n .add_level numero_livello max_xp ruolo_ricompensa')

    @commands.command()
    async def add_level(self, ctx, id, max_xp, reward):
        if(Start.state):
            await ctx.send('Il bot è in funzione, per aggiungere un livello devi prima fermarlo con .stop, testa di cazzo')
            return
        Start.add_level(id, max_xp, reward)
        await ctx.send('Livello numero '.format(id) +'aggiunto')

def setup(client):
    client.add_cog(Basic(client))