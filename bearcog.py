import discord
from discord import app_commands
from discord.ext import commands
import random
import requests
from bear import GUILD_ID
import yaml

# Load YAML file
with open('bearQuotes.yaml', 'r', encoding="utf8") as file:
    data = yaml.safe_load(file)

quotes = data['quotes']
names = data['names']

class Bear(commands.Cog):
    def __init__(self, bear : commands.Bot):
        self.bear = bear

    @app_commands.command(name="bear", description="bear")
    async def bear(self, interaction: discord.Interaction):
        embed = discord.Embed(title = f"**{random.choice(names)}**", color= 0x964B00)
        response = requests.get(f'https://source.unsplash.com/random/?bear&{random.randint(0,100)}', allow_redirects=False)
        embed.set_image(url=response.url)
        embed.set_footer(text=random.choice(quotes), icon_url=self.bear.user.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bear : commands.Bot):
    await bear.add_cog(Bear(bear), guilds = [discord.Object(id = GUILD_ID)])
    print(f'{__name__} loaded')