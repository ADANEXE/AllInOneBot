import discord
import os
import asyncio
import logging
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# 1. Setup Logging & Environment
logging.basicConfig(level=logging.INFO)
load_dotenv()

class OtakuProductions(commands.Bot):
    def __init__(self):
        # Setting up all intents for full "All-in-One" functionality
        intents = discord.Intents.all()
        
        super().__init__(
            command_prefix="!", 
            intents=intents,
            help_command=None # We will make a custom one later
        )
        
        # Database & Config
        self.mongo_uri = os.getenv("MONGO_URI")
        self.adan_id = int(os.getenv("ADAN_ID")) # Your ID from .env
        self.db = None

    async def setup_hook(self):
        """This runs before the bot starts—perfect for DB and Cogs."""
        # Connect to MongoDB
        client = AsyncIOMotorClient(self.mongo_uri)
        self.db = client["otaku_productions_db"]
        print("✅ Connected to MongoDB Atlas")

        # Automatically Load all Cogs from the /cogs folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"📦 Loaded Cog: {filename}")
                except Exception as e:
                    print(f"❌ Failed to load Cog {filename}: {e}")

    async def on_ready(self):
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Logged in as: {self.user.name}")
        print(f"Bot ID: {self.user.id}")
        print(f"Owner ID: {self.adan_id}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Syncing Slash Commands (Tree)
        try:
            synced = await self.tree.sync()
            print(f"🔄 Synced {len(synced)} Slash Commands globally.")
        except Exception as e:
            print(f"⚠️ Slash Sync Error: {e}")

        # Set Status
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name="Otaku Productions | !plan"
            )
        )

# --- EXECUTION ---
bot = OtakuProductions()

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ ERROR: BOT_TOKEN not found in environment variables!")
    else:
        bot.run(token)
