import discord


BOT_TOKEN = "xxx" #TOP SECRET DO NOT DISCLOSE

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
            for ext in ['.jpg', '.png', '.jpeg']:
                if file.filename.endswith(ext):
                    await message.channel.send("That message contains an image!")
                    time.sleep(random.randrange(1, 3))
                    channel1 = client.get_channel(1032676870912753676)
                    channel2 = client.get_channel(1033322865694625905)
                    embed = discord.Embed(title="Would you like to publish this wallpaper?", description="Publishing will send post this wallpaper in other union servers' wallpaper channels. If the image is a wallpaper it is recommended to publish.", color=discord.Colour.blue())
                    embed.set_image(url=message.attachments[0].url)
                    embed.set_footer(text="Note that publishing non wallpaper images or low quality shitpost wallpapers can lead to an infraction.")
                    await channel1.send(embed=embed)
                    await channel2.send(embed=embed)


client.run(BOT_TOKEN)

