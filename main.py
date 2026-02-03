import discord
import os
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
ADAN_ID = 1130020581367099462  # <--- REPLACE WITH YOUR ACTUAL DISCORD ID

class OtakuBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)
        self.db_client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.db_client["otaku_productions"]
        self.owner_id = ADAN_ID

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        print(f"Logged in as {self.user}")

bot = OtakuBot()
bot.run(TOKEN)
  
