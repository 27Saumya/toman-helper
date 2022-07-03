import discord
from discord.ext import commands

class TomanBot(commands.Bot):
    """Subclass of `commands.Bot` (This will be our Toman Helper Bot)"""

    def __init__(self):

        super().__init__(
            command_prefix=get_prefix,
            intents=intents,
            case_insensitive=True,
            strip_after_prefix=True,
        )

    async def on_ready(self):
        """Print a message when the bot is ready"""
        print("Toman Helper Bot is online")


bot = TomanBot()

bot.run("TOKEN")
