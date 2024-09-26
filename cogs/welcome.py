import discord 
import json
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('config.json') as config_file:
            config = json.load(config_file)
        if config["welcome_channel_id"]:
            guild = member.guild
            channel = guild.get_channel(config["welcome_channel_id"])
            message = f"<:msrp:1258584781868765244> **Welcome to Michigan State Roleplay** {member.mention}! We hope you enjoy your stay here. You are now member `{len([m for m in guild.members if not m.bot])}`"

            await channel.send(message)


async def setup(bot):
    await bot.add_cog(Welcome(bot))