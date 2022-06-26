import logging
from enum import Enum
from random import randint, choice
import discord
from discord.ext import commands
from core import checks
import box
import json
import string
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")


class emoji(Cog):
    """
    Where tf did I mess up?
    """

    image = [
        "https://cdn.discordapp.com/emojis/949633562146136094.webp?size=44&quality=lossless"

    ]

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        # self.db = bot.plugin_db.get_partition(self)

    @commands.command(name="yuri", aliases=["gaytime"])
    async def _gaytime(self, ctx):
        """
        Where did I mess up
        """
        embed = discord.Embed(color=15383739)
        embed.set_image(url=choice(self.image))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(emoji(bot))
