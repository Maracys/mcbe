import discord, asyncio, datetime
from discord.ext import commands
from mcstatus import MinecraftBedrockServer

client = commands.Bot(command_prefix="mc.", intents=discord.Intents.all(), activity=discord.Game(name="mc.info"), status=discord.Status.idle)
client.remove_command("help")

inter = {}

status = {
	"ip":"94.130.53.134",
	"port":"26383",
	"name":"EditedWorld",
	"version":"1.17.11",
	"online":False,
	"latency":0,
	"players_max":100,
	"players_online":0,
	"types":{True:"🟩Онлайн", False:"🟥Оффлайн"}
}

server = MinecraftBedrockServer(f"{status['ip']}:{status['port']}")

async def get_status():
	global status, server
	try:
		st = server.lookup(f"{status['ip']}:{status['port']}").status()
		status["name"] = st.motd
		status["version"] = st.version.version
		status["players_max"] = st.players_max
		status["players_online"] = st.players_online
		status["latency"] = st.latency
		status["online"] = True
	except:
		status["players_online"] = 0
		status["latency"] = 0
		status["online"] = False

@client.event
async def on_ready():
	print(f"""------------------------------
Имя: {client.user.name}
Айди: {client.user.id}
Серверов: {len(client.guilds)}
------------------------------""")
	while True:
		await get_status()
		msg = await client.fetch_channel(885850390099271720)
		msg = await msg.fetch_message(885850580336119838)
		await msg.edit(embed=discord. Embed(title="Статус сервера", description=f"""Статус: {status["types"][status["online"]]}
Пинг: {round(status["latency"]*1000)}ms
Игроки: {status["players_online"]}/{status["players_max"]}""", timestamp=datetime.datetime.utcnow(), color = discord.Color.green()))
		await asyncio.sleep(60)
		
@client.command()
async def info(ctx):
	await get_status()
	emb=discord. Embed(title="Информация сервера", description=f"""Имя: {status["name"]}
Айпи: {status["ip"]}
Порт: {status["port"]}
Тип: Bedrock Edition
[Скачать {status["version"]}](https://disk.yandex.ru/d/GQepjV0oxVOzrg)
Статус: {client.command_prefix}stat""", color = discord.Color.green())
	await ctx.send(embed=emb)

client.run("ODg1NDI0MjU3NTk1NzQ4MzUy.YTm1mQ.iJPTkRbcNoGZAwgUbmoIoiUZ6MA")