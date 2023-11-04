import discord
from discord.ext import commands

import config


class OneMoreRoomBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=config.prefix, intents=intents)

    async def on_ready(self):
        print("Bot is ready!")

    async def setup_hook(self) -> None:
        await self.load_extension("one_more_room")


def main():
    bot = OneMoreRoomBot()
    bot.run(config.token)


if __name__ == "__main__":
    main()
