import random
import discord
from discord.ext import commands

Cog = getattr(commands, "Cog", object)

logger = logging.getLogger("Modmail")

    @commands.command(name="vexing", aliases=["vex"])
    async def _aki(self, ctx):
        """
        Replies with a witty remark. Give it a try if you think you're strong enough to take it.
        """
    random = ["Your useless self has nothing that would justify expending my precious time on the likes of you", "entry2", "entry3"]
    await ctx.send(f"{random.choice(random)}")


def setup(bot):
    bot.add_cog(Vex(bot))
