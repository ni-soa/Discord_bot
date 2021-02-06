import discord
client = discord.Client()

@client.event
async def on_message(message):
  if message.content == "Member status":
    Status_channel = message.channel
    print(Status_channel)