from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

botToken = os.environ.get("bot-token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print("Connected!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name="foo")
async def foo(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(arg)


bot.run(botToken)
