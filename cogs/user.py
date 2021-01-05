import discord
from discord.ext import commands
from core.bot import Bot

class User(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(
            title="Levelup lista comandi",
            colour = discord.Colour.blue()
        )
        embed.add_field(name=".rank", value="Visualizza il tuo punteggio e livello", inline=False)
        embed.add_field(name=".top", value="Visualizza la classifica del server", inline=False)
        embed.add_field(name=".help", value="Lista dei comandi", inline=False)
        if ctx.message.author.guild_permissions.administrator:
            embed.add_field(name=".start", value="Fai partire levelup", inline=False)
            embed.add_field(name=".stop", value="Ferma levelup", inline=False)
            embed.add_field(name=".roles", value="Visualizza il nome e id di tutti i ruoli del server", inline=False)
            embed.add_field(name=".levels", value="Visualizza la lista dei livelli salvati", inline=False)
            embed.add_field(name=".add_level <max_xp> <role_id>", value="Aggiunge il livello fino a max_xp e dà come ricompensa role_id", inline=False)
            embed.add_field(name=".clear_levels", value="Elimina tutti i livelli salvati", inline=False)
            embed.add_field(name=".add_users", value="Salva tutti gli utenti del server", inline=False)
            embed.add_field(name=".clear_users", value="Elimina tutti gli utenti del server", inline=False)
            embed.add_field(name=".get_voice_channels", value="Visualizza il nome e id di tutti i canali vocali del server", inline=False)
            embed.add_field(name=".add_channel <voice_channel_id>", value="Salva il canale no xp del server (AFK)", inline=False)
            embed.add_field(name=".get_text_channels", value="Visualizza il nome e id di tutti i canali testuali del server", inline=False)
            embed.add_field(name=".set_comunication_channel <text_channel_id>", value="Salva il canale delle comunicazioni principali del server", inline=False)
        await ctx.send(embed = embed)

    @commands.command()
    async def top(self, ctx):
        embed=discord.Embed(
            title="Classifica top 5",
            colour = discord.Colour.blue()
        )
        users = await Bot.get_top()
        i = 0
        for user in users:
            i += 1
            embed.add_field(name= str(i) + '. ' + user.name , value= str( await Bot.get_rank(user.id)) + ' XP', inline=False)
        await ctx.send(embed = embed)


    @commands.command()
    async def rank(self, ctx):
        rank = int(await Bot.get_rank(ctx.message.author.id))
        level = int(await Bot.get_level(ctx.message.author.id))
        max_xp = int(Bot.get_max_xp(ctx.message.author.id))
        reward = Bot.get_reward(level)
        reward_name = str(Bot.get_role_name(reward))
        uptime = round(rank * 60,1)
        text_uptime = ''
        if(uptime == 0):
            text_uptime = 'Nessuna attività'
        elif(uptime < 1):
            text_uptime = 'Pochi secondi'
        else:
            if(uptime > 60):
                uptime = round(uptime/60,1)
                if(uptime > 60):
                    uptime = round(uptime/60,1)
                    if(uptime == 1):
                        text_uptime = str(uptime) + " ora"
                    else:
                        text_uptime = str(uptime) + " ore"
                    if(uptime > 24):
                        uptime = round(uptime/24,1)
                        if(uptime == 1):
                            text_uptime = str(uptime) + " giorno"
                        else:
                            text_uptime = str(uptime) + " giorni"
                else:
                    if(uptime == 1):
                        text_uptime = str(uptime) + " minuto"
                    else:
                        text_uptime = str(uptime) + " minuti"
            else:
                if(uptime == 1):
                    text_uptime = str(uptime) + " secondo"
                else:
                    text_uptime = str(uptime) + " secondi"
            
        embed=discord.Embed(
            title=ctx.author.name,
            description= 'Ecco il tuo punteggio',
            colour = discord.Colour.blue()
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="Livello", value=str(level), inline=True)
        embed.add_field(name="Punti", value=str(rank) + ' XP', inline=True)
        embed.add_field(name="Uptime", value=text_uptime , inline=True)
        if not(level == Bot.get_max_level_number() and rank > max_xp):
            embed.add_field(name="Completamento livello", value=str(max_xp) + ' XP' , inline=False)
            embed.add_field(name="Ruolo ricompensa", value=reward_name , inline=False)
        else:
            embed.add_field(name="Tutti i livelli sono completati!", value='Complimenti, goditi il potere' , inline=False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(User(client))