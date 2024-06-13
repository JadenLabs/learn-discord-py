# First we are going to import the discord library with Client and Intents
#       Client is the class that handles discord-related functions
#       Intents is a class helps to tell discord what your bot will do
from discord import Client, Intents

# Create the client with all intents
#       Using all intents for simplicity at the moment
client = Client(intents=Intents.all())

# Just trying to run client.run() naively
# It will throw an error because there isn't a token
client.run()
# ! TypeError:
# !     Client.run() missing 1 required positional argument: 'token'
