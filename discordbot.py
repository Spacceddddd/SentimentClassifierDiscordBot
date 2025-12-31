
import discord
from discord.ext import commands
import random


from transformers import pipeline

choices = [
    'How do you feel about Osama Bin Laden',
    'Do you think nuclear weapons should be banned and why?', 
    'Like taxes? why or why not',
    'Should artificial intelligence be regulated by governments?',
    'What is the most important issue facing society today?',
    'Do you believe in free speech without limits?',
    'Should wealth be redistributed more equally?',
    'Is climate change humanity\'s biggest challenge?',
    'What role should social media play in politics?',
    'Do you think universal basic income is a good idea?',
    'Should healthcare be free for everyone?',
    'Is education too expensive?',
    'What do you think about cancel culture?',
    'Should privacy or security be prioritized more?'
]
# This classifies sentiment
sentiment = pipeline("sentiment-analysis")
result = sentiment("I hate this policy")


class Client(commands.Bot):#Client is the name of your robot, discord.client is giving your robot the capabilities of a standard discord bot
    pending_question = False
    async def on_ready(self):
        #called whenever the bot turns on
        print(f"Logged on as {self.user}!") #name of the bot
        try:
          guild = discord.Object(id=1453225509327605922)
          synced = await self.tree.sync(guild=guild)
          #syncing our guild object/decleopment server with our code to discord
          print(f"Synced {len(synced)} commands to guild : {guild.id}")
        except Exception as e:
          print(f"Problem syncing commands with guild {guild.id}: {e}")


    async def on_message(self,message):
      if message.author == self.user: #stops the bot from self replying
        return
      if message.content.startswith('hello'):
          await message.channel.send(f'Hi there {message.author}')#wait for discord to send your message
      if message.content.lower() == 'ask me a question':
        carr =random.choice(choices)
        await message.channel.send(f"{carr}")
        self.pending_question =True
      elif self.pending_question == True:
        resulta = sentiment(message.content)
        await message.channel.send(f"Your results\n{resulta}")

      content = message.content
      #author = message.author.name
      channel = message.channel.name


      """if message.content.startswith('ask me a question'):
        carr = random.choice(choices)
        await message.channel.send(f"{carr}")
          async def on_message(self,message):
            if message.author == self.user: #stops the bot from self replying
              return
            result = sentiment(message.content)
            await message.channel.send(f"{result}")"""





    async def on_reaction_add(self, reaction, user):
      await reaction.message.channel.send(f'You reacted')
    async def on_message_edit(self,before, after):
      if before.author or after.author == self.user:
        return
      else:
        await before.channel.send(f"{before.author} edited from '{before.content}'  to '{after.content}'")
    async def on_message_delete(self,message):
      await message.channel.send(f"{message.author} deleted the message {message.content}")

#1453225509327605922

GUILD_ID= discord.Object(id=1453225509327605922)

intents = discord.Intents.default()
intents.message_content = True  #allowing it to act
client = Client(command_prefix="!",intents=intents)#command prefix were the commands used by discord before but they're pushing slash commands, the code wouldnt work if you dont include the prefixes tho
#intents for running our bot by passing in our permissiones
@client.tree.command(name="yello",description="Say hello!",guild=GUILD_ID)#client refers to the object before
async def sayHello(interaction: discord.Interaction):
  #wherever this interaction was, respond to this interaction by sending a message
  await interaction.response.send_message("Hi there!")

@client.tree.command(name="mirror",description="Mirrors your message!",guild=GUILD_ID)#client refers to the object before
async def mirrorp(interaction: discord.Interaction,printer: str):
  #wherever this interaction was, respond to this interaction by sending a message
  await interaction.response.send_message(f"{printer}")

@client.tree.command(name="embed",description="Embed Demo!",guild=GUILD_ID)#client refers to the object before
async def embedded(interaction: discord.Interaction):
  embed = discord.Embed(title="I AM A TITLE", description='JESUS LOVES YOU', url='https://www.bible.com/bible/111/ROM.16.NIV',color = discord.Color.teal())
  embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHgqFl381WvzC646QnaMK6dVlLdtg1lkq3aw&s')
  embed.add_field(name='Why?',value="", inline=False)
  embed.add_field(name='Reason 1', value='Because he died for you',inline=False)#inline means can other fields be on the same ling
  embed.add_field(name='Reason 2', value="He formed you and He's the reason you're alive", inline=False)
  embed.set_footer(text='Do you believe?')
  embed.set_author(name=interaction.user.name, url = 'https://www.youtube.com/@YHWHislawd' )
  await interaction.response.send_message(embed=embed)


#class is for displaying the button and other stuff


class Viewbuttoner(discord.ui.View):
  @discord.ui.button(label = 'REDAHH', style=discord.ButtonStyle.danger, emoji='🥀')
  async def button_callback(self,button,interaction):#callbackforwhenthebuttonisclicked
    await button.response.send_message(f"{button.user.name}!, how dare you awaken me!!!!")

  @discord.ui.button(label = 'GREENAHH', style=discord.ButtonStyle.primary, emoji='😊')
  async def button_callback(self,button,interaction):#callbackforwhenthebuttonisclicked
    await button.response.send_message(f"{button.user.name}! , WAKE UP TO REALITY!!!!")


  #BUTTONS







@client.tree.command(name="button",description="Embed Demo!",guild=GUILD_ID)
async def mybuttoner(interaction: discord.Interaction):
  await interaction.response.send_message(view=Viewbuttoner())





client.run('DISCORDBOTTOKEN')
