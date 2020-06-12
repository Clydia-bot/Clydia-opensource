import asyncio
from discord.ext import commands
import discord
print("Lancement du bot")
# discord.py module import


# ajouter un composant de discord.py


# créer une nouvelle instance de notre bot
# client = discord.Client()
client = commands.Bot(command_prefix='c?', help=None)
client.remove_command('help')

## ---- BOT configuration ---- ##

# on ready :
@client.event
async def on_ready():
    activity = discord.Game(name="Regarde c?help", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot has log in.')


# command error
@client.event
async def on_command_error(ctx, error):
    # print(ctx.command.name + " command was invoked incorrectly")
    print(error)
    await ctx.channel.send("Oups, il y a une erreur dans la commande :/ Voici l'erreur : {}".format(error))

#  Help command
@client.command(name='help', help='Show this message')
async def help(ctx):
    embed = discord.Embed(
        title="Help Menu", description="Liste des commandes", color=discord.Color.dark_red())
    embed.set_author(name="Clydia")
    embed.add_field(name="https://documentation.clydia.online/#/?id=%f0%9f%92%ac-commandes-",
                    value="Cliquer sur le lien pour voir l'aide", inline=True)
    await ctx.send(embed=embed)

## ---- Général ---- ##

# say hello
@client.command(name='hello', aliases=['bonjour', 'salut', 'coucou'], help='Just say Hello')
async def hello(ctx):
    await ctx.channel.send("Salut toi ça va ?")


# clear command

@client.command(name='clear', help='Clear X message from channel')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    amount = int(number)
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send("Tu as clean {}".format(number) + " messages")
    await asyncio.sleep(3)
    amount = int(1)
    await ctx.channel.purge(limit=amount)

# info command
@client.command(name='info', help='Donne une petite biographie de Clydia')
async def info(ctx):
    embed = discord.Embed(title="Biographie", color=discord.Color.dark_red())
    embed.add_field(name="Allez c'est parti",
                    value="J'ai été crée par @_l0u1$_#4317. Après plus de 100 lignes de codes, me voilà enfin. Et l'aventure n'est pas encore terminé", inline=False)
    embed.set_footer(text="@Clydia #9501")
    await ctx.send(embed=embed)

# say command
@client.command(name='say', help='Dire un message à votre place')
@commands.has_permissions(send_messages=True, manage_messages=True)
async def say(ctx, channel:discord.TextChannel, *, message):
    #Embed making
    embed = discord.Embed(title="Message", color=discord.Color.dark_red())
    embed.add_field(name="Nouveau message de {}".format(ctx.message.author), value="{}".format(message))
    embed.set_footer(text="{}".format(ctx.message.author))

    await channel.send(embed=embed)

## ---- Modération ---- ##

# ban
@client.command(name='ban', help='Bannir qql')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author == member:
        await ctx.channel.send("Tu ne peux pas te bannir toi meme ")

    else:
        await member.ban(reason=reason)
        await member.send("Tu as été ban du serveur par {}".format(ctx.message.author))

# deban
@client.command(name='unban', aliases=['debannir', 'débann'], help='deban qql')
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)

# kick
@client.command(name='kick', help="Expulser quelqu'un")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author == member:
        await ctx.channel.send("Tu ne peux pas t'expulser toi meme ")
    else:
        await member.kick(reason=reason)
        await member.send("Tu as été expulsé du serveur par {}".format(ctx.message.author))


## ---- Autres ---- ##
# Ping command
@client.command(name='ping', help='Know latency')
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency} ms')






# connecter au serveur
client.run('TOKENHERE')
