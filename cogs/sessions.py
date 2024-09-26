import discord
from discord.ext import commands


class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    

class Session_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.votes = []
    
    @discord.ui.button(
        label="Vote", style=discord.ButtonStyle.gray, custom_id="vote_button" 
    )
    async def vote_button(self, button:discord.ui.Button, interaction: discord.Interaction):
        if not self.votes[interaction.user.id]:
            self.votes.insert(-1, interaction.user.id)
            await interaction.response("")




async def setup(bot):
    await bot.add_cog(bot)