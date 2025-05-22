import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    for name in levelnames:
        if name in str(message.content).lower() and len(message.content) < len(name)*5:
            await message.reply(levelnames[name], mention_author=True)

client.run('bot_token_here')
