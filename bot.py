from logging import getLogger

import discord
from discord.ext import commands

import config

logger = getLogger("discord")


class OneMoreRoomBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix=config.prefix, intents=intents)

    async def on_ready(self):
        logger.info("Bot is ready!")

    async def setup_hook(self) -> None:
        await self.load_extension("one_more_room")


def main():
    bot = OneMoreRoomBot()
    bot.run(config.token)


if __name__ == "__main__":
    main()
