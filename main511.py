import os

import discord

import random
import time
import re, asyncio

from discord.ext import commands, tasks
from itertools import cycle
from discord import Activity, ActivityType, Member
from discord.utils import get
import requests
from random import choice
from discord.ext.commands import Bot, Greedy

PREFIX = "c_"
Client = commands.Bot(command_prefix = PREFIX)

@Client.event
async def on_ready():
    print('---------loaded-----------')
    # -------код вывода всех серверов пользователя-------
    # async for guild in Client.fetch_guilds(limit=150):
    #     print(guild.name)
    stream = discord.Streaming(
        name="С Котом В l_help",
        url="https://www.twitch.tv/leykoder", 
    )
    await Client.change_presence(activity=stream)

@Client.remove_command('help')

@Client.command()
async def help(ctx):
    emb1 = discord.Embed(title="Информация о командах", color=random.randint(1, 16777216))
    emb1.add_field(name = f"`{PREFIX}rainbowrole` : ", value="Запускает изменение цвета роли || Starts changing the color of the role", inline=False)
    await ctx.send(embed = emb1)

serverid = 521678450818547714
colours = ['#EB5757', '#EB6157', '#EB6A57', '#EB7457', '#EB7E57', '#EB8857', '#EB9257', '#EB9C57', '#EBA657', '#EBB057', '#EBBA57', '#EBC357', '#EBCD57', '#EBD757', '#EBE157', '#EBEB57', '#E1EB57', '#D7EB57', '#CDEB57', '#C3EB57', '#BAEB57', '#B0EB57', '#A6EB57', '#9CEB57', '#92EB57', '#88EB57', '#7EEB57', '#74EB57', '#6AEB57', '#61EB57', '#57EB57', '#57EB61', '#57EB6A', '#57EB74', '#57EB7E', '#57EB88', '#57EB92', '#57EB9C', '#57EBA6', '#57EBB0', '#57EBBA', '#57EBC3', '#57EBCD', '#57EBD7', '#57EBE1', '#57EBEB', '#57E1EB', '#57D7EB', '#57CDEB', '#57C3EB', '#57BAEB', '#57B0EB', '#57A6EB', '#579CEB', '#5792EB', '#5788EB', '#577EEB', '#5774EB', '#576AEB', '#5761EB', '#5757EB', '#6157EB', '#6A57EB', '#7457EB', '#7E57EB', '#8857EB', '#9257EB', '#9C57EB', '#A657EB', '#B057EB', '#BA57EB', '#C357EB', '#CD57EB', '#D757EB', '#E157EB', '#EB57EB', '#EB57E1', '#EB57D7', '#EB57CD', '#EB57C3', '#EB57BA', '#EB57B0', '#EB57A6', '#EB579C', '#EB5792', '#EB5788', '#EB577E', '#EB5774', '#EB576A', '#EB5761']
rainbowrolename = "Rainbow"
delay = 10

@Client.command()
@commands.is_owner()
async def rainbowrole(role):
    for role in Client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            while not Client.is_closed():
                for element in colours:
                    element = element.replace('#','')
                    col = int(f"{element}" , 16)
                    try:
                        await role.edit(color=col)
                    except Exception:
                        print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                        pass
                    await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await Client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        Client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        Client.loop.create_task(rainbowrole(rainbowrolename))   

token = os.environ.get('BOT_TOKEN')

Client.run(str(token))
