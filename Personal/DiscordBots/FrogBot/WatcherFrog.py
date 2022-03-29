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
import requests
import bs4
import time
from selenium import webdriver 
from selenium .webdriver.chrome.options import Options
from fake_useragent import UserAgent
from datetime import datetime


ua = UserAgent()

opts = Options()
opts.add_argument("user-agent="+ua.random)
driver = webdriver.Chrome(options=opts)


gamblingAccounts = {}

TOKEN = 'x'

DailyChatLog = []
DailyChatLogLength = 0

CommandNameList = ['gambleCoin', 'gambleBalance', 'gambleGift', 'pointMute']

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(intents=intents, command_prefix = '/')
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
        with open('GamblingAccounts.txt', 'r') as f:
            for line in f:
                (holder, bal) = line.split('=')
                bal = bal.strip()
                gamblingAccounts.update({holder : bal})
            f.close()
        await client.get_channel(882033829177597982).send(f'Accounts Found')
    else:
        await client.get_channel(882033829177597982).send(f'No Accounts Found') 
        with open('GamblingAccounts.txt', 'w') as f:
            for members in memberList:
                f.write(members.name + '=' + '1000')
                f.write('\n')
                gamblingAccounts.update({members.name: "1000"})
            f.close()
        
    await track()
        
    
        
        
        
        
    
    #for i in CommandNameList:
        #registerGuildCommand(i)
        
    
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
    bal = gamblingAccounts[asker]
    embed=discord.Embed(title="User Balance!", description="**{0}** has **{1}**points!    ".format(asker, bal), color=0xff00f6)
    await ctx.send(embed=embed)
            
            
@client.command()
async def gambleCoin(ctx, args1): #check first then rewrite?
    bettor = ctx.author.name
    bet = int(args1)
    if validUserTransaction(bettor, bet):
        outcomeEvent = random.randint(0,1)
        if outcomeEvent == 1:
            newBal = int(gamblingAccounts[bettor]) + bet
            gamblingAccounts[bettor] = str(newBal)
            embed=discord.Embed(title="Coin Flip!", description="**{0}** flipped a coin betting **{1}**  points and **won**! \n Their new balance is: **{2}** ".format(bettor, str(bet), newBal), color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            newBal = int(gamblingAccounts[bettor]) - bet
            gamblingAccounts[bettor] = str(newBal)
            embed=discord.Embed(title="Coin Flip!", description="**{0}** flipped a coin betting **{1}**  points but **lost**! \n Their new balance is: **{2}** ".format(bettor, str(bet), newBal), color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Coin Flip!", description="**{0}** Tried flipping a coin and betting **{1}**  points but they lacked the points, they would have **won**! \n Their balance is: **{2}** ".format(bettor, str(bet), gamblingAccounts[bettor]), color=0xff00f6)
        await ctx.send(embed=embed)
    await rewrite()
        
@client.command()
async def gambleGift(ctx, gift, reciever):
    gifter = ctx.author.name
    giftAmt = int(gift)
    (validTransaction, validReciever) = validUserTransfer(gifter, int(gift), reciever)
    if validTransaction and validReciever:
        gamblingAccounts[gifter] = str(int(gamblingAccounts[gifter])-giftAmt)
        gamblingAccounts[reciever] = str(int(gamblingAccounts[reciever])+giftAmt)
        embed=discord.Embed(title="Points Sent!", description="**{0}** sent **{1}** **{2}** points! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
    elif not validTransaction:
        embed=discord.Embed(title="Gift Failure!", description="**{0}** tried to send **{1}** **{2}** points but was too broke! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
    elif not validReciever:
        embed=discord.Embed(title="Gift Failure!", description="**{0}** tried to send **{1}** **{2}** points but they dont exist! ".format(gifter, reciever, gift), color=0xff00f6)
        await ctx.send(embed=embed)
    await rewrite()
        
####### 
#
#Point Spending
#
#######

@client.command()
async def pointMute(ctx, member: discord.Member):
    buyer = ctx.author.name
    rewrite = ''
    (validTransaction, validReciever) = validUserTransfer(buyer, 1000, member.name)
    if validTransaction and validReciever:
        await member.edit(mute = True)
        newBal = int(gamblingAccounts[buyer]) - 1000
        gamblingAccounts[buyer] = str(newBal)
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
    #retValue = bal>=amt ???
    retValue = False
    bal = int(gamblingAccounts[user])
    if bal >= amt:
        retValue = True
    return retValue
    
#@desc: Validates user transaction request when another party is involved
#@param: str, int, str
#@return: list of two booleans 
def validUserTransfer(user, amt, tar):
    retValue = [validUserTransaction(user,amt), False]
    for i in gamblingAccounts:
        if i == tar:
            retValue[1] = True
    return retValue
    
#@desc: updates text file storing accounts
#@param: none
#@return: void
async def rewrite():
    rewrite = ''
    with open('GamblingAccounts.txt', 'w') as f:
        for i in gamblingAccounts:
            bal = gamblingAccounts[i]
            rewrite = rewrite + i+'='+bal+'\n'
        f.write(rewrite)
        f.close()
            
    
async def track():
    while True:
        driver.get("https://www.adafruit.com/product/4295")
        html = driver.page_source
        scrape = bs4.BeautifulSoup(html,"html.parser")
    
        itemInStore = scrape.find_all("span",{"class":"meta_pid_box_status"})
        inStock = []
        
    
        for product in itemInStore:
            if("Out of stock" not in product.text):
                inStock.append(product.find_parent("a")['href'])
            
        baseUrl = "https://www.adafruit.com"
        if inStock  == []:
            print('['+str(datetime.now())+']'+" Track Pass: [No Stock]")
            #await client.get_channel(882033829177597982).send(f'No RPIs on Adafruit')
        else:
            for part in inStock:
                whole = baseUrl + part
                await client.get_channel(882033829177597982).send(whole)
            print('['+str(datetime.now())+']'+" Track Pass: [ALERT INSTOCK]")
        await asyncio.sleep(15)
    
 
    
#@desc: register the command
#@param: str
#@return: void
#def registerGuildCommand(commandName):
#    url = "https://discord.com/api/v8/applications/<app_id>/guilds/<guild_id>/commands"
#    json = {"name": commandName, "type": 2}
#    headers = {"Authorization": "Bot TOKEN"}
#    r = requests.post(url, headers=headers, json=json)
#    print(r)
    



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
