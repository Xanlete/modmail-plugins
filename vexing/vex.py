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


class Vex(Cog):
    """
    Replies with a witty remark. Give it a try if you think you're strong enough to take it.
    """

    vex = [
        "Your useless self has nothing that would justify expending my precious time on the likes of you"
    ]


    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        # self.db = bot.plugin_db.get_partition(self)

    @commands.command(name="aki", aliases=["cat"])
    async def _aki(self, ctx):
        """
        Replies with a witty remark. Give it a try if you think you're strong enough to take it.
        """
        embed = discord.Embed(
            title="vex", color=0000000
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Vex(bot))
