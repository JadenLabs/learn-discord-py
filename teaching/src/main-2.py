# Import os to access environment variables
import os

# Import print from rich for cli colors
from rich import print
from discord import Client, Intents

# Import load_dotenv from dotenv
from dotenv import load_dotenv

# Parse the .env file and then load all the
#       variables as environment variables.
load_dotenv()

# Get the TOKEN and put it into a variable
TOKEN = os.environ.get("TOKEN", None)
# Add some error handling just in case the TOKEN doesn't exist
if TOKEN is None:
    print("[red]ERROR[/]: Token not found in `.env`")
    exit(1)

client = Client(intents=Intents.all())


# Create an event handler for the on_ready event
@client.event
async def on_ready():
    # The brackets around some of the words are used for
    #       the rich console formatting
    print(f"[green]SUCCESS[/] Logged in as [blue]{client.user.name}[/]")


# Run the client, but using a token this time
client.run(TOKEN)
