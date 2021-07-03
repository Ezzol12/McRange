import random
import socket
import threading
import discord
from discord.ext import commands
import os
import threading
import asyncio
import requests

client= commands.Bot(command_prefix = '.')

print("""


                                                                      
   SSSSSSSSSSSSSSS KKKKKKKKK    KKKKKKKIIIIIIIIIIDDDDDDDDDDDDD        
 SS:::::::::::::::SK:::::::K    K:::::KI::::::::ID::::::::::::DDD     
S:::::SSSSSS::::::SK:::::::K    K:::::KI::::::::ID:::::::::::::::DD   
S:::::S     SSSSSSSK:::::::K   K::::::KII::::::IIDDD:::::DDDDD:::::D  
S:::::S            KK::::::K  K:::::KKK  I::::I    D:::::D    D:::::D 
S:::::S              K:::::K K:::::K     I::::I    D:::::D     D:::::D
 S::::SSSS           K::::::K:::::K      I::::I    D:::::D     D:::::D
  SS::::::SSSSS      K:::::::::::K       I::::I    D:::::D     D:::::D
    SSS::::::::SS    K:::::::::::K       I::::I    D:::::D     D:::::D
       SSSSSS::::S   K::::::K:::::K      I::::I    D:::::D     D:::::D
            S:::::S  K:::::K K:::::K     I::::I    D:::::D     D:::::D
            S:::::SKK::::::K  K:::::KKK  I::::I    D:::::D    D:::::D 
SSSSSSS     S:::::SK:::::::K   K::::::KII::::::IIDDD:::::DDDDD:::::D  
S::::::SSSSSS:::::SK:::::::K    K:::::KI::::::::ID:::::::::::::::DD   
S:::::::::::::::SS K:::::::K    K:::::KI::::::::ID::::::::::::DDD     
 SSSSSSSSSSSSSSS   KKKKKKKKK    KKKKKKKIIIIIIIIIIDDDDDDDDDDDDD        
                                                                      
                                                                      
                                                                      
                       Mcrange crash bot by ae#7990                                               
                                                                    

""")



@client.event
async def on_ready():
    print("bot dziala")

@client.command()
async def aegis(ctx, arg1, arg2):

    embed = discord.Embed(colour = discord.Colour.blue())

    embed.add_field(name='<--> Attack started <-->', value=f'ip: {arg1}', inline=False)
    embed.add_field(name='-------------------', value=f'port: {arg2}', inline=False)
    embed.add_field(name='<--> Attack started <-->', value='⁣', inline=True)
    embed.set_footer(text='Developer your toem#7990')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/854388755463798844/858007596337201152/PicsArt_06-25-03.48.06.png')
    embed.set_image(url='https://cdn.discordapp.com/attachments/854388755463798844/858007598816690196/PicsArt_06-25-03.54.17.jpg')

    await ctx.send(embed=embed)

    def attack():
        os.system(f"your command")

    t1 = threading.Thread(target=attack)
    t1.start()

@client.command()
async def instant(ctx, arg1, arg2):

    embed = discord.Embed(colour = discord.Colour.blue())

    embed.add_field(name='<--> Attack started <-->', value=f'ip: {arg1}', inline=False)
    embed.add_field(name='-------------------', value=f'port: {arg2}', inline=False)
    embed.add_field(name='<--> Attack started <-->', value='⁣', inline=True)
    embed.set_footer(text='Developer your toem#7990')
    embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{arg1}')
    embed.set_image(url='https://cdn.discordapp.com/attachments/854388755463798844/858007598816690196/PicsArt_06-25-03.54.17.jpg')

    await ctx.send(embed=embed)

    def attack():
        os.system(f"your command")

    t1 = threading.Thread(target=attack)
    t1.start()

    await ctx.send(embed=embed)


client.run('token')
