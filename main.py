import discord
from discord.ext import commands
from discord_slash import SlashCommand
import os
import requests

bot = commands.Bot(command_prefix = "/")
slash = SlashCommand(bot,sync_commands=True)

@slash.slash(description="with this command you can convert text to emoji")
async def text2emoji(ctx, *, text):
    try:
        data = requests.get(f"https://nodejs-beta.yash0221.repl.co/{text}")
        await ctx.send(data.content)
    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xADD8E6)
        await ctx.channel.send(embed=embedVar)
    
bot.run(os.getenv['Token'])
