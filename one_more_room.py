import discord
from discord.ext import commands

import config
from bot import OneMoreRoomBot


class OneMoreRoom(commands.Cog):
    def __init__(self, bot: OneMoreRoomBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: discord.Member,
        before: discord.VoiceState,
        after: discord.VoiceState,
    ):
        try:
            if (
                before.channel
                and isinstance(before.channel, discord.VoiceChannel)
                and before.channel.id not in config.ignored_channels
                and not before.channel.members
            ):
                await before.channel.delete()

            if (
                after.channel
                and isinstance(after.channel, discord.VoiceChannel)
                and after.channel.id not in config.ignored_channels
                and len(after.channel.members) == 1
            ):
                await after.channel.clone()
        except discord.Forbidden:
            pass


async def setup(bot: OneMoreRoomBot):
    await bot.add_cog(OneMoreRoom(bot))
