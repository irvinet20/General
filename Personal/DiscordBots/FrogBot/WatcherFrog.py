import os
import os.path
import time
import random
import discord
from discord import *
import random
import asyncio
import datetime
from discord.ext import commands

TOKEN = 'x'

DailyChatLog = []
DailyChatLogLength = 0

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(intents=intents, command_prefix = '.')
FrogBot = Client()


#general = client.get_channel(846357507454140441)
#serverIndex = client.guilds.index(846357507454140438)
#homeIndex = server.channels.index(846357507454140441)

#######
#
#Startup
#
#######
@client.event
async def on_ready():
    print('test {0.user}'.format(client))
    guild = client.get_guild(846357507454140438)
    memberList = guild.members
    memberNameList = []
    for i in memberList:
        memberNameList.append(i.name)
    
    if os.path.exists('GamblingAccounts.txt'):
        await client.get_channel(882033829177597982).send(f'Accounts Found')
        #with open('GamblingAccounts', 'r') as f:
        #    for name in memberNameList:
        #        if name not in f: #error with substring names
        #            with open('GamblingAccounts', 'a') as e:
        #                e.write(name + '=' + '1000')
        #                e.write('\n')
                    
    else:
        await client.get_channel(882033829177597982).send(f'No Accounts Found') 
        with open('GamblingAccounts.txt', 'w') as f:
            for members in memberList:
                f.write(members.name + '=' + '1000')
                f.write('\n')
        f.close()
    
########
#
#Events
#
#######

@client.event    
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
        
    DailyChatLog.append(f'{username}: {user_message} ({channel})')
        
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        return

    await client.process_commands(message)
    return
    
#######
#
#General
#
#######

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@client.command()
async def chatLog(ctx):
    for i in DailyChatLog:
        await ctx.send(i)
        
@client.command()
async def magicBall(ctx, args):
    check = random.randint(1,2)
    if '?' not in args:
        await ctx.send('correct formart is -> "question?"')
        return
    elif check == 1:
        await ctx.send(args+' yes')
    else:
        await ctx.send(args+' no')
        
@client.command()
async def roll(ctx, args1, args2):
    if int(args1) > int(args2):
        await ctx.send('please put the smaller number first')
        return
    retValue = random.randint(int(args1), int(args2))
    await ctx.send(retValue)
    
#######
#
#Gambling
#
#######

@client.command()
async def gambleBalance(ctx):
    asker = ctx.author.name
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == asker:
                embed=discord.Embed(title="User Balance!", description="**{0}** has **{1}**points!    ".format(asker, bal), color=0xff00f6)
                await ctx.send(embed=embed)
    f.close()
            
            
@client.command()
async def gambleCoin(ctx, args1): #check first then rewrite?
    bettor = ctx.author.name
    bet = int(args1)
    rewrite = ''
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == bettor:
                if int(bal) >= bet:
                    outcomeEvent = random.randint(0,1)
                    if outcomeEvent == 1:
                        newBal = str(int(bal)+bet)
                        line = line.replace(bal, newBal)
                        rewrite = rewrite+line+'\n'
                        embed=discord.Embed(title="Coin Flip!", description="**{0}** flipped a coin betting **{1}**  points and **won**! \n Their new balance is: **{2}** ".format(bettor, str(bet), newBal), color=0xff00f6)
                        await ctx.send(embed=embed)
                    else:
                        newBal = str(int(bal)-bet)
                        line = line.replace(bal, newBal)
                        rewrite = rewrite+line+'\n'
                        embed=discord.Embed(title="Coin Flip!", description="**{0}** flipped a coin betting **{1}**  points but **lost**! \n Their new balance is: **{2}** ".format(bettor, str(bet), newBal), color=0xff00f6)
                        await ctx.send(embed=embed)
                else:
                    rewrite = rewrite+line
                    embed=discord.Embed(title="Coin Flip!", description="**{0}** Tried flipping a coin and betting **{1}**  points but they lacked the points, they would have **won**! \n Their balance is: **{2}** ".format(bettor, str(bet), bal), color=0xff00f6)
                    await ctx.send(embed=embed)
            else:
                rewrite = rewrite+line
    f.close()
    with open('GamblingAccounts.txt', 'w') as f:
        f.write(rewrite)
        f.close()
        
@client.command()
async def gambleGift(ctx, gift, reciever):
    gifter = ctx.author.name
    giftAmt = int(gift)
    rewrite = ''
    (validTransaction, validReciever) = validUserTransaction(gifter, int(gift), reciever)
    if validTransaction and validReciever:
        with open('GamblingAccounts.txt', 'r') as f:
            for line in f:
                (holder, bal) = line.split('=')
                if holder == gifter:
                    newBal = str(int(bal)-giftAmt)
                    line = line.replace(bal, newBal)
                    rewrite = rewrite+line+'\n'
                elif holder == reciever:
                    newBal = str(int(bal)+giftAmt)
                    line = line.replace(bal, newBal)
                    rewrite = rewrite+line+'\n'
                else:
                    rewrite = rewrite+line
            f.close()
        with open('GamblingAccounts.txt', 'w') as f:
            f.write(rewrite)
            f.close()
        embed=discord.Embed(title="Points Sent!", description="**{0}** sent **{1}** **{2}** points! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
    elif not validTransaction:
        embed=discord.Embed(title="Gift Failure!", description="**{0}** tried to send **{1}** **{2}** points but was too broke! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
    elif not validReciever:
        embed=discord.Embed(title="Gift Failure!", description="**{0}** tried to send **{1}** **{2}** points but they dont exist! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
        
####### 
#
#Point Spending
#
#######

@client.command()
async def pointMute(ctx, member: discord.Member):
    buyer = ctx.author.name
    rewrite = ''
    (validTransaction, validReciever) = validUserTransaction(buyer, 1000, member.name)
    if validTransaction and validReciever:
        await member.edit(mute = True)
        with open('GamblingAccounts.txt', 'r') as f:
            for line in f:
                (holder, bal) = line.split('=')
                if holder == buyer:
                    newBal = str(int(bal)-1000)
                    line = line.replace(bal, newBal)
                    rewrite = rewrite+line+'\n'
                else:
                    rewrite = rewrite+line
            f.close()
        with open('GamblingAccounts.txt', 'w') as f:
            f.write(rewrite)
            f.close()
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**! for 15s \n New Balance: **{2}**".format(member, ctx.message.author, newBal), color=0xff00f6)
        await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await member.edit(mute = False)
    else:
        embed=discord.Embed(title="User Mute Attempt!", description="**{0}** tried to mute **{1}** for 15s but was too broke!".format(ctx.message.author, member), color=0xff00f6)
        await ctx.send(embed=embed)
    
    
#######
#
#Internals
#
#######

#@desc: Validates user transaction request when another party is involved
#@param: str, int
#@return: returns boolean
def validUserTransaction(user, amt):
    retValue = False
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == use:
                if int(bal) >= amt:
                    retValue = True
        f.close()
    return retValue
    
#@desc: Validates user transaction request when another party is involved
#@param: str, int, str
#@return: list of two booleans 
def validUserTransaction(user, amt, tar):
    retValue = [False, False]
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == user:
                if int(bal) >= amt:
                    retValue[0] = True
            elif holder == tar:
                retValue[1] = True
        f.close()
    return retValue




#@client.event
#async def on_connect():
#    if os.path.exists('GamblingAccounts'):
#        await client.get_channel(882033829177597982).send(f'Accounts Found')
#    else:
#        await client.get_channel(882033829177597982).send(f'No Accounts Found') 
#        with open('GamblingAccounts', 'w') as f:
#            f.write('test')   


    
#@client.event
#async def on_connect():
#    await client.get_channel(846357507454140441).send(f'Watching')

    

    
#@client.event
#async def on_disconnect():
#    await client.get_channel(846357507454140441).send(f'Dipping')
#    
client.run(TOKEN)
