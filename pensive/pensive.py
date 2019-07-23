import discord
from redbot.core import commands
from typing import Optional


class Pensive(commands.Cog):
    """My First Cog"""

    @commands.command()
    async def support(self, ctx):
        """Support Server"""
        await ctx.send("https://discord.gg/xGEMMmy")

    @commands.command()
    async def say(self, ctx, *, msg: str):
        """Make the bot repeat things"""
        await ctx.author.send(msg)

    @commands.command(hidden=True)
    async def silentsay(self, ctx, *, msg: str):
        """
           Makes the Bot repeat things silently
        """
        # https://github.com/TrustyJAID/Trusty-cogs/blob/master/trustybot/trustybot.py#L56
        if ctx.channel.permissions_for(ctx.guild).manage_messages:
            await ctx.message.delete()
        await ctx.send(msg)