import os
import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix = "/")

@bot.command(name="text2emoji")
async def text2emoji(ctx, *, text):
    try:
        data = requests.get(f"https://nodejs-beta.yash0221.repl.co/{text}")
        await ctx.send(data.content.decode("utf-8"))

    except Exception as e:
        embedVar = discord.Embed(title="💀 error", description=e, color=0xADD8E6)
        await ctx.send(embed=embedVar)
       
bot.run(os.environ["Token"])

        
