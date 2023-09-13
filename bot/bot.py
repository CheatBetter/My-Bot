"""

MIT License

Copyright (c) 2023 CheatBetter

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

"""Main bot class, holds the actual functions for the bot
"""

import discord
from discord.ext.commands import Bot
from discord import Intents
from bot.constants import config
from bot.utils import logger
from colorama import Fore, Style
from glob import glob
from datetime import datetime



class DiscordBot(Bot):
    def __init__(self, version: str) -> None:
        super().__init__(command_prefix=config.COMMANDPRE, intents=Intents.all(), application_id=1150558352468873326)
        self.READY = False
        self.VERSION = version
        self.LOGGER = logger.Logger(name=config.BOTNAME, time=True, color=Fore.GREEN, style=Style.BRIGHT, t_color=Fore.CYAN, t_style=Style.BRIGHT, version=self.VERSION, dev_mode=True)

    async def load_extensions(self):
        COGS = [path.split("\\")[-1][:-3] for path in glob("./bot/extensions/*.py")]
        for cog in COGS:
            await self.load_extension(f"bot.extensions.{cog}")
            self.LOGGER.info(f"Successfully loaded {cog}")

    async def setup_hook(self) -> None:
        self.LOGGER.debug("Loading extensions...")
        await self.load_extensions()
        await self.tree.sync(guild=discord.Object(id=1150551992272420999))


    async def start_bot(self):
        self.LOGGER.debug("Running bot...")
        self.tree.copy_global_to(guild=discord.Object(id=1150551992272420999))
        await self.start(token=config.TOKEN, reconnect=True)

    async def on_connect(self):
        self.LOGGER.info(f"{self.user.display_name} has connected")

    async def on_ready(self):
        if not self.READY:
            self.LOGGER.info(f"{self.user.name} is ready for usage")
            self.READY = True
            if config.SDOUT == "True":
                channel = self.get_channel(int(config.SDID))
                await channel.send(f"{config.SDMSG}")
        else:
            self.LOGGER.warn("Bot has reconnected")

bot = DiscordBot("0.0.1")