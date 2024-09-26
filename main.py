import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from jishaku import Jishaku
from discord import Embed, Color
from jishaku.help_command import MinimalEmbedPaginatorHelp

load_dotenv()

class Bot(commands.Bot):
    async def is_owner(self, user: discord.User):
        return user.id == 696158716617031711

intents = discord.Intents.all()
bot = Bot(command_prefix=commands.when_mentioned_or("-"), intents=intents, help_command=MinimalEmbedPaginatorHelp())

@bot.event
async def on_ready():
    await bot.load_extension('jishaku')
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await bot.load_extension("cogs." + f[:-3])
            print(f)
    await bot.tree.sync()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = Embed(
            color=Color.blurple(),
            title="",
            description="```\nYou do not have permission to run this command.\n```"
        )
        await ctx.reply(embed=embed)

bot.run(os.getenv("TOKEN"))