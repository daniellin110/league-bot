import config
import discord
from discord.ext import commands
import extract_result
import post_result

TOKEN = config.TOKEN
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def update(ctx, *, link):
    result = extract_result.extract_result(link)
    if result == []:
        await ctx.send('Invalid game link.')
    else:
        if post_result.post_result(result[0], result[1], result[2]) == -1:
            await ctx.send(result[0] + ' (white) vs. ' + result[1] + ' (black) is not a match in the current round.')
        else:
            msg = result[0] + ' vs ' + result[1] + ' has been recorded as a ' 
            if(result[2] == 'Draw'):
                msg = msg + 'Draw.'
            else:
                msg = msg + 'Win for ' + result[3] + '.'
            await ctx.send(msg)
bot.run(TOKEN)