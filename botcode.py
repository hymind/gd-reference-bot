import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.lower()
    with open('levelnames.json') as f:
        levelnames = json.load(f)
        for name in levelnames:
            if name == 'what' or name == 'how':
                if msg != name:
                    return
            if name + ' ' in msg or name + 's ' in msg or msg.endswith(name):
                if len(msg) < len(name*20):
                    await message.reply(levelnames[name], mention_author=True)
        await bot.process_commands(message)
        return

@bot.hybrid_command()
async def submit(ctx, name: str, img: str):
    try:
        if not (img.startswith('https://') or img.startswith('http://')):
            await ctx.send("Image must be a link!")
            return
        elif not (img.endswith(('.jpg', '.png'))):
            await ctx.send("Invalid file type!")
            return
        elif not (name == name.lower()):
            await ctx.send("Name must be all lowercase!")
            return
        with open('levelnames.json', 'r') as f:
            levelnames = json.load(f)
            levelnames[name]=img
        with open('levelnames.json', 'w') as f:
            json.dump(levelnames, f, indent=4)
        await ctx.send("Added to database successfully!")
    except Exception as e:
        await ctx.send(f"An error has occurred: {e}")

bot.run('token_here')
