import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

class Bear(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
        )

    async def setup_hook(self):

        await self.load_extension('bearcog')
        try:
            synced = await self.tree.sync(guild=discord.Object(id=690297491513409570))
            print(f"Synced {len(synced)} bear commands")
            print('Bearing in...')

        except Exception:
            print("Unable to sync bear commands!")

    async def close(self):
        await super().close()

    async def on_ready(self):
        print(f'Beared in as {self.user}')
        print(f'Beartency is {round(self.latency * 1000)} ms')

bear = Bear()

async def start():
    async with bear:
        await bear.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(start())