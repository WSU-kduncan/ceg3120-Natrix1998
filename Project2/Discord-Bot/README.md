# My First Bot
## Setup
To get access to the Discord API for your bot, you need to access the discord developer portal first. <br>
Then, create an application and a bot. <br>
Copy the authorization token for the bot and save it to a .env file in the same folder as the python code for the bot.<br>
Make sure you install python3, discord.py, and python-dotenv. <br>
In the bot's code, use "TOKEN = os.getenv('DISCORD_TOKEN')" to pull the token into the bot.<br>
At the end of your python code, use "bot.run(TOKEN)" to interact with Discord's API and connect your bot to your server.
## Usage
Type !uncle to get a random quote from uncle Iroh.<br>
Type !turmoil to get a random quote from prince Zuko.<br>
## Research
To run the bot 24/7, you could host it on a virtual private server (VPS).<br>
If you wanted to keep it local and always active, you could utilize a raspberry pi. Pi's can run Linux and Python pretty easily, and they do not use much power. 