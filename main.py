from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# --- Mantener el bot activo en Replit ---
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def keep_alive():
    Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8080}).start()

# --- Configuración del bot ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# IDs de los usuarios permitidos y del servidor
GUILD_ID = 1335418414671597668  # Reemplaza esto con el ID de tu servidor
ALLOWED_IDS = [1175609298508857409, 1071835969180925973]  # Owner y Creator

# Crear instancia del bot
bot = commands.Bot(command_prefix="/", intents=intents)

# Evento al iniciar el bot
@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))  # Sincroniza los comandos slash
    print(f"✅ Bot is ready! Logged in as {bot.user}")

# Comando /post
@bot.tree.command(name="post", description="Publish SSU", guild=discord.Object(id=GUILD_ID))
async def post(interaction: discord.Interaction):
    if interaction.user.id not in ALLOWED_IDS:
        await interaction.response.send_message("❌ You do not have permission to use this command.", ephemeral=True)
        return

    embed = discord.Embed(
        title="🌟 New SSU Posted!",
        description="Feel free to join the server!",
        color=discord.Color.blue()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1389070678090715156/1389073423854080031/Michigan_is_better_with_you.jpg")
    embed.add_field(name="Version", value="1.8", inline=False)
    embed.set_footer(text="Posted by Dominoes 500 / Theo")

    await interaction.response.send_message(embed=embed)

# --- Ejecutar el bot ---
keep_alive()
bot.run(os.getenv("TOKEN"))