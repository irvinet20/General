import os
import os.path
import time
import random
import discord
from discord import *
import random
from discord.ext import commands

TOKEN = 'x'

cmdList = ['exclude ()', '.killBot', '.chatLog', '.test (arg)', '.magicBall ("arg?")',
           '.roll (smallerNum LargerNum)', '.squaredCircle', '.Brunswick', '.Jake', '.Meez',
           '.Jared', '.Lauman', '.Lawson', '.Sandman', '.helpList', 'x']
           
gmbList = ['exclude ()', '.gambleCoin (bet)']


LawsonVote = 0
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
                await ctx.send(bal)
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
                if bal >= args1:
                    outcomeEvent = random.randint(0,1)
                    if outcomeEvent == 1:
                        newBal = str(int(bal)+bet)
                        line = line.replace(bal, newBal)
                        rewrite = rewrite+line+'\n'
                        await ctx.send("winner, new balance "+newBal)
                    else:
                        newBal = str(int(bal)-bet)
                        line = line.replace(bal, newBal)
                        rewrite = rewrite+line+'\n'
                        await ctx.send("loser, new balace "+newBal)
                else:
                    rewrite = rewrite+line
                    await ctx.send("Not enough points")
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
    (validTransaction, validReciever) = validUserTransaction(ctx, int(gift), reciever)
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
        await ctx.send('Sent')
    elif not validTransaction:
        await ctx.send('not enough points'+str(validTransaction)+str(validReciever))
    elif not validReciever:
        await ctx.send('not a valid recipient')
        
####### 
#
#Point Spending
#
#######

@client.command()
async def pointTimeout(ctx, buyer, target):
    return true
    
    
#######
#
#Internals
#
#######

#@param str, int
def validUserTransaction(user, amt):
    retValue = False
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == user:
                if int(bal) >= amt:
                    retValue = True
        f.close()
    return retValue

#@param str, int, str
def validUserTransaction(user, amt, tar):
    retValue = [False, False]
    with open('GamblingAccounts.txt', 'r') as f:
        for line in f:
            (holder, bal) = line.split('=')
            if holder == user:
                if int(bal) >= amt:
                    retValue[0] = True
            elif holder == tar:
                retValue[1] == True
        f.close()
    return retValue



#######
#
#Jokes
#
#######  

@client.command()
async def squaredCircle(ctx):
    await ctx.send('A mythical object that is of a plane too high for Jake')
    
@client.command()
async def Jake(ctx):
    await ctx.send('Potentially the dumbest user here')

@client.command()
async def Brunswick(ctx):
    await ctx.send('Spying on everyone almost as much as myself')
    
@client.command()
async def Sandman(ctx):
    await ctx.send('I have the [moral highground] [anyone] dont try it')
    
@client.command()
async def Lauman(ctx):
    await ctx.send('You think there would be a command for lauman? thatd be toxic')
    
@client.command()
async def Meez(ctx):
    await ctx.send('Psychopath spiderman wannabe, most likely to go to chernobyl to look for a mutant spider')
    
@client.command()
async def Jared(ctx):
    await ctx.send('A man of many titles: Hometown worker, OW pro, MinMaxer, Rougelike spammer')
    
@client.command()
async def Lawson(ctx):
    await ctx.send('Error: no user. likely cause: deleted acc')
    
@client.command()
async def killBot(ctx):
    choice = random.randint(1,3)
    if choice == 1:
        await ctx.send('Its treason, then')
    elif choice == 2:
        await ctx.send('Im sorry Dave, Im afraid I cant do That')
    elif choice == 3:
        await ctx.send('Nice try chump')

@client.command()
async def helpList(ctx):
    for i in cmdList:
        await ctx.send(i)
    
    
    
    

        
#@client.command()
#async def muteLaw(ctx):
#    global LawsonVote
#    LawsonVote = LawsonVote + 1
#    if LawsonVote == 3:
#        
#        LawsonVote = 0
#        return
#    else:
#        await ctx.send("more votes req.")
        
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
