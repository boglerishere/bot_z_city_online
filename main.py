
import a2s
from discord.ext import commands

bot = commands.Bot(command_prefix='>', self_bot=True)

list_servers = [
    ('5.42.211.48',24215),
    ('5.42.211.48', 24217),
    ('194.147.90.131', 24215),
    ('194.147.90.131', 24217)
]
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_message(message):
    print(message.content)
    if message.content == '!status' and message.channel.id == 1271789595909951492:
        text = 'Бот создан > thebogler если что то не работает пишите ему'
        for server in list_servers:
            try:
                adres = a2s.info(server, timeout=2)
                text += f'''```fix
IP: {server[0]}:{server[1]}
-=-=-=-=-=-=-=-=-=-=-=-=-=-
NAME: {adres.server_name}
MAP: {adres.map_name}
-=-=-=-=-=-=-=-=-=-=-=-=-=-
PLAYER COUNT: {adres.player_count}/{adres.max_players}```'''

            except:
                print('Сервер с IP', server,'Не доступен')



        await message.channel.send(text+"\nБот не работает в <#1271789595909951488> из за того что один человек начал спамить, и бот начал засорять чат\nКак смогу напишу систему для антиспама")


bot.run('123123')