import os

from rich import print
from discord import Intents, Interaction  # Import the Interaction class for typing

# Import commands from ext, commands will let us structure
#       our bot in a better way later down the road
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN", None)
if TOKEN is None:
    print("[red]ERROR[/]: Token not found in `.env`")
    exit(1)

# Replace Client with Bot and set a command prefix
#       The command prefix doesn't really matter
#       as we will be using slash commands instead
bot = commands.Bot(command_prefix="t.", intents=Intents.all())
# Set the bot tree to a variable
tree = bot.tree


# Create your first discord.py command using tree.command
#       Set the name and description
@tree.command(name="ping", description="Ping the bot!")
# Make an async function that takes an interaction as an argument
#       The ctx variable is also often named interaction, but it's
#       personal preference, set it to pineapple if you really want
async def ping(ctx: Interaction):
    # Respond to the interaction by sending a message
    await ctx.response.send_message("Pong!")


@bot.event
async def on_ready():
    print(f"[green]SUCCESS[/] Logged in as [blue]{bot.user.name}[/]")
    # Sync the tree so your command is registered with discord!
    synced = await tree.sync()
    # Log how many commands were synced because why not
    print(f"{len(synced)} commands synced.")


bot.run(TOKEN)
