"""
MIT License
Copyright (c) 2022-Present 27Saumya
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands
import asyncpg


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
