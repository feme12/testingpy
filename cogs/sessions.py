import discord
import json
from discord.ext import commands
from discord import Embed

class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('config.json') as config_file:
            config = json.load(config_file)
        self.config = config
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.add_view(Session_view())

    @commands.hybrid_command(name="session", description="Starts a session.", with_app_command=True)
    async def session(self, ctx: commands.Context):
        embed = Embed(
            title=self.config["Session"]["Vote_embed"]["title"],
            description=self.config["Session"]["Vote_embed"]["description"],
            color=discord.Color.from_rgb(self.config["Session"]["Vote_embed"]["color"]["r"],self.config["Session"]["Vote_embed"]["color"]["g"],self.config["Session"]["Vote_embed"]["color"]["b"])
        )
        view = Session_view()
        view.ctx = ctx
        await ctx.reply(embed=embed, view=view)

class Session_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.votes = []
        with open('config.json') as config_file:
            config = json.load(config_file)
        self.config = config
        
    
    @discord.ui.button(label=f"Vote(0/15)", style=discord.ButtonStyle.gray, custom_id="vote_button")
    async def vote_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = interaction.user.id
        if user_id not in self.votes:
            self.votes.append(user_id)
            embed = Embed(
                title=self.config["Session"]["Vote_button_response_embed"]["added"]["title"],
                description=self.config["Session"]["Vote_button_response_embed"]["added"]["description"],
                color=discord.Color.from_rgb(self.config["Session"]["Vote_button_response_embed"]["added"]["color"]["r"],self.config["Session"]["Vote_button_response_embed"]["added"]["color"]["g"],self.config["Session"]["Vote_button_response_embed"]["added"]["color"]["b"])
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            if user_id in self.votes:
                self.votes.remove(user_id)
                embed = Embed(
                    title=self.config["Session"]["Vote_button_response_embed"]["removed"]["title"],
                    description=self.config["Session"]["Vote_button_response_embed"]["removed"]["description"],
                    color=discord.Color.from_rgb(self.config["Session"]["Vote_button_response_embed"]["removed"]["color"]["r"],self.config["Session"]["Vote_button_response_embed"]["removed"]["color"]["g"],self.config["Session"]["Vote_button_response_embed"]["removed"]["color"]["b"])
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="View Votes", style=discord.ButtonStyle.gray, custom_id="vote_view_button")
    async def vote_view_button(self, interaction: discord.Interaction, button: discord.Button):
        message = "\n".join(f"<@{user}>" for user in self.votes)
        embed = Embed(
            title=self.config["Session"]["Votes_view_embed"]["title"],
            description=f"{self.config["Session"]["Votes_view_embed"]["description"]}\n{message}",
            color=discord.Color.from_rgb(self.config["Session"]["Votes_view_embed"]["color"]["r"],self.config["Session"]["Votes_view_embed"]["color"]["g"],self.config["Session"]["Votes_view_embed"]["color"]["b"])
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Session(bot))