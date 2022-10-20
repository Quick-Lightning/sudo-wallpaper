import discord


BOT_TOKEN = "MTAzMjY3NjAzMTM1MTUwNTA0Ng.Gh1Tll.oLMdfcInrWcZlk7EpJfNkxlErUaEVXZ51l_bAk" #TOP SECRET DO NOT DISCLOSE

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user and message.attachments:
        for file in message.attachments:
            for ext in ['.jpg','.png','.jpeg']:
                if file.filename.endswith(ext):
                    await message.channel.send("That message contains an image!")

client.run(BOT_TOKEN)