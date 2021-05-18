import asyncio
import discord
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import bot
import random 
import pickle
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import requests

os.chdir(r'\root\bot')

client = commands.Bot(command_prefix = '+')
client.remove_command('help')

#bot = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('ImNotMagik Bitch'))
    print("Bot Online")
    
@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users  = json.load(f)

    await update_data(users, members)

    with open('users.json', 'w') as f:
        json.dump(users, f)
        
    role = discord.utils.get(member.sever.role, name='Customers')
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)

async def update_date(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['exerience'] = 0
        user[user.id]['levlel'] = 1 

async def add_experience(users, user, exp):
    user[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experince = users[user.id]['experience']
    level_start = users[user.id]['level']
    level_end = int(experience ** (1/4))

    if level_start < level_end:
        await client.send.message(channel, '{} has leveled  up to level {)'.format(user.mention, level_end))
        user[user.id]['lelvel'] = level_end

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.")

@client.command(pass_context=True)
async def help():
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
        )

    embed.set_author(name ='Help')
    embed.added_field(name='+ping', value='Reutnrn Pong', inline=False)

    await client.send_message(author)
    await client.send_message(channel)
@client.command()
async def choose(ctx):
   random_lines = random.choice(open("Movie_List.txt").readlines())
   await ctx.send(random_lines)

@client.command()
async def loop(ctx):
    while True:
        await ctx.send("Chef_Kev#0317")

@client.command()
async def sin(ctx):
    await ctx.send("confess your sins my son")

@client.command()
async def confess(ctx):
    await ctx.send("Your sins are forgiven, go in peace my child")

@client.command(pass_context=True)
async def snap(ctx, amount=None):
    if amount is None:
        await ctx.channel.purge(limit=5)
    elif amount == "all":
        await ctx.channel.purge()
        await ctx.send('https://tenor.com/view/thanos-avengers-infinity-war-mind-stone-last-stone-infinity-gauntlet-gif-15735729')
        await ctx.send('https://tenor.com/view/thanos-this-does-put-smile-on-my-face-but-this-does-put-smile-on-my-face-smile-on-my-face-thanos-smile-on-my-face-gif-16933884')
    else:
        await ctx.channel.purge(limit=int(amount))

@client.command()
async def wipe(ctx, amount=0):
    await ctx.channel.purge(limit=amount)

'''@snap.error()
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Enter correct amount of messages to delete.")
        '''

@client.command()
async def quote(ctx):
    random_lines = random.choice(open("quote.txt").readlines())
    await ctx.send(random_lines)

@client.command()
@commands.has_any_role("OG")
async def ban(ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
       await ctx.channel.send("You cannot ban yourself")
       return
    if reason == None:
        reason = ""
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} is banned!")

@client.command()
async def unabn(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned  {user.mention}')
            return 

@client.command()
async def soccer(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')

@client.command()
async def yum(ctx):
    url = "https://www.reddit.com/r/food/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img", attrs={"alt":"Post image"})
    number = 0
    for image in images:
        print(image["src"])
        image_src = image["src"]
        urllib.request.urlretrieve(image_src, str(number))
        number += 1
        break
    path="/root/bot"
    files=os.listdir(path)
    d=random.choice(files)
    await ctx.send(os.startfile(d))




       
client.run("Nzc1NDg1OTAzNjEwMzE0ODM0.X6nBhw.QP7wu4FvXXq9ddoZDcwkuvwMxSM")