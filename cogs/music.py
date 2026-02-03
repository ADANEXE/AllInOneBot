import discord
from discord.ext import commands
import yt_dlp
import asyncio

YTDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True', 'quiet': True}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_premium(self, user_id):
        user = await self.bot.db.premium.find_one({"_id": user_id})
        return user and user.get("is_premium", False)

    @commands.command()
    async def play(self, ctx, *, search):
        if not ctx.author.voice:
            return await ctx.send("Join a voice channel first!")
        
        vc = ctx.voice_client or await ctx.author.voice.channel.connect()
        
        with yt_dlp.YoutubeDL(YTDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
            url = info['url']
            title = info['title']
        
        vc.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
        await ctx.send(f"🎵 Now playing: **{title}**")

    @commands.command()
    async def volume(self, ctx, vol: int):
        if not await self.is_premium(ctx.author.id):
            return await ctx.send("❌ Volume control is an **Otaku Productions Premium** feature!")
        ctx.voice_client.source.volume = vol / 100
        await ctx.send(f"🔊 Volume set to {vol}%")

async def setup(bot):
    await bot.add_cog(Music(bot))
  
