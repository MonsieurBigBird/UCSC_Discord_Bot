
import discord
import botToken
import random

maxOakesLength = 5

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global maxOakesLength
    if message.author == client.user:
        return

    if message.content.startswith('!setMaxOakes '):
        maxOakes = message.content.split("!setMaxOakes ", 1)[1]
        if(maxOakes.isdigit()):
            if(int(maxOakes) < 0 or int(maxOakes) > 500):
                await message.channel.send("Number of OAKES spammed must be between 1 and 500")
            else:
                outputString = "Max number of OAKES that can be spammed is currently " + maxOakes
                await message.channel.send(outputString)
                maxOakesLength = int(maxOakes)
        else:
            await message.channel.send('That is not a valid input')

    if message.content.startswith('!getMaxOakes'):
        outputString = "Max number of OAKES that can be spammed is currently " + str(maxOakesLength)
        await message.channel.send(outputString)

    if 'oakes' in message.content:
        oakesString = "OAKES"
        for i in range(random.randint(1, maxOakesLength)):
            oakesString = oakesString + " OAKES"
        await message.channel.send(oakesString)

client.run(botToken.token)
