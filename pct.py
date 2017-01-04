import discord
import json

# Commands #
from commands.peacoat import pug

config = json.loads(open('config.json').read())  # Load Configs
DISCORD_TOKEN = config["discord_token"]
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):

    if message.content.startswith('!help') or message.content.startswith('!pug'):
        await client.send_message(message.channel, "I'm Peacoat, Destroyer of Pugs!\n"
                                                   "Use: !peacoat <name> <server>\n"
                                                   "Example: !pug Peacoat Sargeras")

    if message.content.startswith('!peacoat'):
        await pug(client, message)

client.run(DISCORD_TOKEN)
