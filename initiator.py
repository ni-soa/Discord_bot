import discord, os
import discord.ext.commands 
import asyncio
from PM_token import TOKEN
import Channel_define

client = discord.Client()


#起動時に動作する処理
@client.event
async def on_ready():
  print('--------------------------------------')
  print('ログインしました')
  print('--------------------------------------')


#メッセージ受信時に動作する処理 
@client.event
async def on_message(message):
  if message.author.bot:
    return

  #greeting
  if message.content.startswith('!Hello') or message.content.startswith("!Hi"):
    await message.reply('Hello!', mention_author=True)

# change icon
  if message.content == "Change icon":
    attachment = message.attachments[0]
    await attachment.save(f'New_icon{os.path.splitext(attachment.url)[1]}')
    with open (f'New_icon{os.path.splitext(attachment.url)[1]}', 'rb') as f:
      icon = f.read()
    
    await message.reply('Are you sure to save this change ?  !yes to save change')

    def msg_check(msg):
      return msg.author == message.author and msg.content == '!yes'

    try:
      await client.wait_for('message', check = msg_check, timeout = 7.0)

    except asyncio.exceptions.TimeoutError:
      await message.channel.send('Change unsaved')
    else:
      await guild.edit(icon = icon)
      await message.channel.send("Icon is successfully changed.")
      print('Change saved')
      print('--------------------------------------')
  
  
  if message.content == "test":
    channel = discord.utils.get(guild.text_channels, name = "status")
    await channel.send('Hi')
    


#online status表示
@client.event
async def on_member_update(before, after):
  if str(before.status) == "online":
    if str(after.status) == "offline":
      channel = discord.utils.get(discord.Guild.text_channels, name = "status")
      await channel.send("{} has gone {}.".format(after.name,after.status))

    if str(after.status) == "offline":
      print("{} has gone {}.".format(after.name,after.status))


client.run(TOKEN)

