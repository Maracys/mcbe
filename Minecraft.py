import discord
from discord.ext import commands
from mcstatus import MinecraftBedrockServer

client = commands.Bot(command_prefix="mc.", intents=discord.Intents.all(), activity=discord.Game(name="mc.help"), status=discord.Status.idle)

@client.event
async def on_ready():
	print(f"""------------------------------
Имя: {client.user.name}
Айди: {client.user.id}
Серверов: {len(client.guilds)}
------------------------------""")

@client.command()
async def status(ctx):
	server = MinecraftBedrockServer.lookup("94.130.53.134:26383")
	status = server.status()
	await ctx.send(embed=discord. Embed(title="Статус сервера", description=f"""Имя: {status.motd}
Пинг: {round(status.latency*1000)}ms
Игроки: {status.players_online}/{status.players_max}
Версия: {status.version.version}""", color = discord.Color.green()))

client.run("ODg1NDI0MjU3NTk1NzQ4MzUy.YTm1mQ.iJPTkRbcNoGZAwgUbmoIoiUZ6MA")