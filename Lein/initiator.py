import discord, os
import asyncio
from PM_token import TOKEN

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
  #greerings
  if message.author.bot:
    return
  if message.content.startswith('/hello') or message.content.startswith("/hi"):
    await message.reply('Hello!', mention_author=True)

# change icon
  if message.content == "change icon":
    guild = message.guild
    attachment = message.attachments[0]
    await attachment.save(f'New_icon{os.path.splitext(attachment.url)[1]}')
    with open (f'New_icon{os.path.splitext(attachment.url)[1]}', 'rb') as f:
      icon = f.read()
    
    await message.reply('Are you sure to save this change ?  /yes to save change')

    def msg_check(msg):
      return msg.author == message.author and msg.content == '/yes'

    try:
      await client. wait_for('message', check = msg_check, timeout = 7.0)

    except asyncio.exceptions.TimeoutError:
      await message.channel.send('Change unsaved')
    else:
      await guild.edit(icon = icon)
      await message.channel.send("Icon is successfully changed.")
      print('Change saved')
      print('--------------------------------------')







client.run(TOKEN)

