import discord
import random
from discord.ext import commands,tasks
from random import choice
import os

client = commands.Bot(command_prefix = '^')

@client.event
async def on_ready():
    changeStatus.start()
    print('Ready na!')

status=['Nanonood nanaman siguro ng hentai si lyndon','insert madrama na quote','sardinas nga lamang po ang ulam','tara kain tayo','drink your water today']

@tasks.loop(minutes=5)
async def changeStatus():
    await client.change_presence(activity=discord.Game(choice(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def ping(ctx):
    await ctx.send(f'Yow! ang ping discord ay {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["Oo ata.",
                "Malay mo pwede.",
                "Oo naman for sure!.",
                "Yes na yes!!!.",
                "Sige pwede ka umasa.",
                "Kung ako tatanungin pwede.",
                "Siguro.",
                "Ata?.",
                "Oo.",
                "Parang oo.",
                "Di ako sure try mo uli mamaya.",
                "Busy ako wag ngayon.",
                "Wag nalang baka masaktan ka.",
                "Wala ako sa mood.",
                "Sure ka na ba jan? Isipin mo mabuti tas tanong mo ko uli.",
                "Wag ka na umasa.",
                "Hindi.",
                "Hindi daw sabi ni Lord.",
                "Kahit 20 times mo ako tanungin nyan, hindi talaga.",
                "Parang hindi."
                "Tangina mo wag mo ko tanungin."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.listen()
async def on_message(message):
    if message.author==client.user:
        return
    if 'tite' in message.content:
         await message.channel.send("tanginang to napaka bastos")
    if '@here' in message.content:
         await message.channel.send("oops walang kasama 💔 ")
    if 'gago' in message.content:
         await message.channel.send("gago ka rin tangina mo")
    if 'lyndon' in message.content:
         await message.channel.send("wag mo hanapin yan nanonood ng hentai")
    if 'barcy' in message.content:
         await message.channel.send("bat hinahanap yung babaero")
    if str(message.author)=="shinobi#2467":
        await message.add_reaction('🚩')
    if str(message.author)=="Lyndawg#9218":
         await message.add_reaction("🍆")
    if str(message.author)=="𝚁𝚊𝚣𝚣#1558":
        await message.add_reaction("🙏")
        await message.add_reaction("👨‍💻")
    if str(message.author)=="MuJacko#4846":
        await message.add_reaction("🎮")
        await message.add_reaction("💢")
    if str(message.author)=="Lucy#6289":
        await message.add_reaction("💦")
        await message.add_reaction("💨")
    

client.run('ODQzMDgwNTQyMDA0OTY5NTAy.YJ-p8A.OJAKWlO1e4qcppymjQ-yWZ1FLv0')