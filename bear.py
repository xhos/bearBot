import os
import asyncio
import discord
import aiohttp
from discord.ext import commands
from bearconfig import TOKEN
class Evo(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
        )

    async def setup_hook(self):

        self.session = aiohttp.ClientSession()
        await self.load_extension('bearcog')
        try:
            synced = await self.tree.sync(guild=discord.Object(id=690297491513409570))
            print(f"Synced {len(synced)} slash commands")
            print('Logging in...')

        except Exception:
            print("Unable to sync slash commands!")

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print("""
            bear
        """)
        print(f'Logged in as {self.user}')
        print(f'Latency is {round(self.latency * 1000)} ms')

evo = Evo()

async def start():
    async with evo:
        await evo.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(start())