import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('does this shit work'):
        await message.channel.send('yes')

client.run('MTI2MDIwNjY2ODQwMzE3OTUzMg.G5M72N.vP7gEdLhOgKn3Rm1bIfangEa_qLLKSDMRDt7ac')
