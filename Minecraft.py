import discord
from discord.ext import commands
from mcstatus import MinecraftBedrockServer

client = commands.Bot(command_prefix="mc.", intents=discord.Intents.all(), activity=discord.Game(name="mc.help"), status=discord.Status.idle)
stat = {
	"motd":"EditedWorld",
	"players_max":100,
	"version":"1.17.11"
}

@client.event
async def on_ready():
	print(f"""------------------------------
Имя: {client.user.name}
Айди: {client.user.id}
Серверов: {len(client.guilds)}
------------------------------""")

@client.command()
async def status(ctx):
	global stat
	try:
		server = MinecraftBedrockServer.lookup("94.130.53.134:26383")
		st = server.status()
		stat["motd"] = st.motd
		stat["latency"] = st.latency
		stat["version"] = st.version.version
		stat["players_max"] = st.players_max
		await ctx.send(embed=discord. Embed(title="Статус сервера", description=f"""Имя: {stat["motd"]}
Статус: 🟩Онлайн
Пинг: {round(status.latency*1000)}ms
Игроки: {st.players_online}/{stat["players_max"]}
Версия: {stat["version"]}""", color = discord.Color.green()))
	except:
		await ctx.send(embed=discord. Embed(title="Статус сервера", description=f"""Имя: {stat["motd"]}
Статус: 🟥Оффлайн
Пинг: 0ms
Игроки: 0/{stat["players_max"]}
Версия: {stat["version"]}""", color = discord.Color.red()))

client.run("ODg1NDI0MjU3NTk1NzQ4MzUy.YTm1mQ.iJPTkRbcNoGZAwgUbmoIoiUZ6MA")