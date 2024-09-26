import discord
from discord import app_commands
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="test", description="This is a test command.", with_app_command=True)
    async def test(self, ctx: commands.Context):
        """Testing"""
        await ctx.reply("This is a test hybrid command.")

async def setup(bot):
    await bot.add_cog(Test(bot))