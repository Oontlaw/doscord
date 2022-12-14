from discord.ext import commands
from discord import Intents

intents = Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')
    await ctx.send(f"Client Latency: `{round(bot.latency * 1000)}ms`")

bot.run('TOKEN_HERE')
