import discord
import json
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="ping", description="The latency of the bot.", with_app_command=True)
    async def ping(self, ctx: commands.Context):
        latency=round(self.bot.latency, 1)

        await ctx.reply(f"My ping is {latency}ms")



async def setup(bot):
    await bot.add_cog(Misc(bot))