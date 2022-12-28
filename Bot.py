import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random

bot = commands.Bot(command_prefix="?", intents = nextcord.Intents.all())

# Variables
welcome_channel = 1057463315414138911
log_channel = 1057460149532508200
stats_channel = 1057474766505771188
guild_id = 1050489982680322218

# Run code
@bot.event
async def on_ready():
    print('The bot has sucuessfully logged in: {0.user}'.format(bot))
    await bot.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.playing, name = "Bloxstore Shopping"))
    await update_membercount()

# Events
@bot.event
async def on_member_join(user):
    await bot.get_channel(welcome_channel).send(f":tada: Please welcome {user.name} to Bloxstore Shopping!\n\nWe hope to see you around!")
    await update_membercount()

@bot.event
async def on_message_edit(before, after):
    embed = nextcord.Embed(title=f"{before.author.mention} has edited their message!")
    embed.add_field(name="Before", value=before.content, inline=False)
    embed.add_field(name="After", value=after.content, inline=False)
    await sendembed_log(embed)

@bot.event
async def on_message_delete(message):
    embed = nextcord.Embed(title=f"{message.author.mention} has deleted their message!")
    embed.add_field(name="Value", value=message.content, inline=False)
    await sendembed_log(embed)

# Functions
async def send_log(reason):
    await bot.get_channel(log_channel).send(reason)

async def sendembed_log(embed):
    await bot.get_channel(log_channel).send(embed=embed)

async def update_membercount():
    await bot.get_channel(stats_channel).edit(name=f"Members: {bot.get_guild(guild_id).member_count}")

# Commands
@bot.slash_command(name="d20", description="Rolls a d20")
async def roll(interaction : Interaction, cheat : bool):
    roll = random.randint(1, 20)
    if cheat == True:
        return await interaction.response.send_message("Trying to cheat are you?")
    if roll == 20:
        await interaction.response.send_message("Woo! 🎉 You rolled 20!")
    else:
        await interaction.response.send_message(f"oof you were {20 - roll} away from rolling a d20! You rolled {roll}.")
@bot.slash_command(name="joke", description="Tells the user a random joke")
async def joke(interaction : Interaction):
    num = random.randint(1, 10)
    is_special = random.randint(1, 100)
    todays_joke = ""
    
    # Special message
    if is_special == 100:
        return await interaction.response.send_message(f"🎉 Wooo! {interaction.user.mention} is special and get's to pick the joke of the day! Message Shining with the joke you want.")

    # Jokes  
    if num == 1:
        await interaction.response.send_message("Here's the joke:\nI don't have one. :joy:")
    if num == 2:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 3:
        if todays_joke == "":            
            await interaction.response.send_message("Here's the joke of the day:\nhttps://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        else:
            await interaction.response.send_message("Here's the joke:\n{todays_joke}")
    if num == 4:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 5:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 6:
        if todays_joke == "":            
            await interaction.response.send_message("Here's the joke:\nhttps://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        else:
            await interaction.response.send_message("Here's the joke of the day:\n{todays_joke}")
    if num == 7:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 8:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 9:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
    if num == 10:
        await interaction.response.send_message("Here's the joke:\n[Your suggestion here]")
@bot.slash_command(name="devlogs", description="Devlogs Command")
async def devlogs(interaction : Interaction):
    await interaction.response.send_message("**Latest Devlog**\nNothing, Sorry.")
@bot.slash_command(name="promote", description="Promote Command")
async def promote(interaction : Interaction, name : str):
    await send_log(f"**{interaction.user.mention} has promoted {name}!**") 
    await interaction.response.send_message(f"Sucuessfully promoted {name}", ephemeral=True)
@bot.slash_command(name="demote", description="Demote Command")
async def demote(interaction : Interaction, name : str):
    await send_log(f"**{interaction.user.mention} has demoted {name}!**") 
    await interaction.response.send_message(f"Sucuessfully demoted {name}", ephemeral=True)
@bot.slash_command(name="hello", description="Says Hello")
async def hello(interaction : Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")
@bot.slash_command(name="refresh", description="Refreshes all commands")
async def refresh(interaction : Interaction):
    if interaction.user.id == 950091757952057385:
        await interaction.response.send_message(f"Refreshing all commands! (Comming Soon Does Not Do Anything)", ephemeral=True)
        return
    await interaction.response.send_message(f"You must be whitelisted to run this command!", ephemeral=True)
@bot.slash_command(name="shutdown", description="Stops the bot")
async def shutdown(interaction : Interaction):
    if interaction.user.id == 950091757952057385:
        await interaction.response.send_message(f"Shutting down Bloxstore Shopping Bot!", ephemeral=True)
        bot.close()
        return
    await interaction.response.send_message(f"You must be whitelisted to run this command!", ephemeral=True)
@bot.slash_command(name="ping", description="The bots ping")
async def ping(interaction : Interaction):
    await interaction.response.send_message(f"🏓Pong\nBloxstore Bot's ping is\n{round(bot.latency * 1000)} ms", ephemeral=True)
@bot.slash_command(name="whoareyou", description="Tells you who I am")
async def whoareyou(interaction : Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} My name is Bloxstore Bot and I love to shop!")

bot.run('Sorry lol')
