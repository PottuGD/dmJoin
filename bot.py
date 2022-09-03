# bot.py
import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} on valmiina kayttoon')


@client.event
async def on_member_join(member):

    await member.send(
    f"""Hei {member.name}, Tervetuloa palvelimelle {member.guild.name}! \n
    jos tykkäät Fall Guys pelistä suosittelemme, että liityt \n 
    Tänne: https://discord.gg/EN3KxYytdU \n 
    Täältä löytyy \n 
    > oma klaani \n 
    > Paljon puhekanavia \n 
    > sekä paljon muuta
    """)


client.run(TOKEN)
