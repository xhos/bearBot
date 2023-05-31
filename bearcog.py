import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import random
from bear import GUILD_ID

now = datetime.now()
time_now = now.strftime("%H:%M:%S %d.%m.%Y")

class Bear(commands.Cog):
    def __init__(self, bear : commands.Bot):
        self.bear = bear

    @app_commands.command(name="bear", description="bear")
    async def bear(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "**bear:**", color= 0x964B00)
        embed.set_image(url=f"https://source.unsplash.com/random/?bear&{random.randint(0,1000)}")
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bear : commands.Bot):
    await bear.add_cog(Bear(bear), guilds = [discord.Object(id = GUILD_ID)])
    print(f'{__name__} loaded')