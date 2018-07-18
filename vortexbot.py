import discord
import asyncio
import time

client = discord.Client()

# Function: checkrole()

def checkrole(user):
    for role in user.roles:
        if role.name == "Vortex team" or role.name == "LORD NERDS":
            return True
    return False

@client.event
async def on_ready():
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("Eingeloggt als:")
    print(client.user.name)
    print(client.user.id)
    print("-=-=-=-=-=-=-=-=-=-=-")

    # Changing the playing status
    await client.change_presence(game=discord.Game(name="Vortex.gg"))


@client.event
async def on_message(message):

    # Command: !trial, !trail, !free

    # if message.content.startswith("!trial ") or message.content == "!trial" or message.content.startswith("!trail ") or message.content == "!trail" or message.content.startswith("!free ") or message.content == "!free":
    #
    #     embed = discord.Embed(title="Is there a free trial?", description="The developers are working really hard on Vortex, because they want you to have te best experience. But they also want and need to get paid for their hard work. That's why it's not possible to offer a free or trial version of Vortex.\n\nIf you want to make sure, that Vortex is lag-free with your internet connection, make sure, that you have done the ping test: <http://vortex.gg/ping>\n\nIf you still don't trust Vortex, just watch some youtube videos and listen to other peoples opinion about this service! :)\n\n*Note that there is also a `!refund` if you are not happy with Vortex!*", color=0x0884ff)
    #     embed.set_author(
    #         name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")
    #
    #     if len(message.mentions) != 0:
    #         embed.set_footer(
    #             text="The person who was tagged can delete this message by clicking the reaction below!")
    #         msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
    #         await client.add_reaction(msg, "❌")
    #
    #     else:
    #         msg = await client.send_message(message.channel, embed=embed)
    #         i = 40
    #         while i >= 0:
    #             timer = str(i)
    #             embed.set_footer(
    #                 text="This message gets deleted automatically in " + timer + " seconds.")
    #             await client.edit_message(msg, embed=embed)
    #             i = i - 2
    #             await asyncio.sleep(2.0)
    #         await client.delete_message(msg)
    #
    #     await client.delete_message(message)

    # Command: !wait, !queue

    if message.content.startswith("!wait ") or message.content == "!wait" or message.content.startswith("!queue ") or message.content == "!queue":

        embed = discord.Embed(title="Why do I have to wait in a queue?", description="If too many people want to use Vortex in the same country, Vortex will automatically create new servers. But unfortunately this takes a while, and that's why you get put into a queue.\n\nJust relax or chat with us on this discord server, until it's time for you to have the best cloud gaming experience you ever had!", color=0x0884ff)
        embed.set_author(
            name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")

        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !support

    if message.content.startswith("!support ") or message.content == "!support":

        embed = discord.Embed(title="Support", description="If you have any support related issues feel free to write an email to contact@vortex.gg or use this link: <https://vortexgg.zendesk.com/hc/en-us/requests/new>\n\nDon't forget to include your Vortex account email (if your issue is payment related, also some payment details) and your mobile/device model that you are using.", color=0x0884ff)
        embed.set_author(
            name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")

        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !ping, !performance

    if message.content.startswith("!ping ") or message.content == "!ping" or message.content.startswith("!performance ") or message.content == "!performance":

        embed = discord.Embed(title="Ping / Performance Test",
                              description="To make sure, that Vortex works lag-free with your internet-connection, make sure, you have done the ping-test:\n\n<https://vortex.gg/ping>", color=0xF89256)
        embed.set_author(
            name="Vortex", icon_url="https://cdn.discordapp.com/emojis/446638333402152960.png?v=1")
        # embed.set_thumbnail(url="https://i.imgur.com/59Fw0Ub.png")
        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !rules

    if message.content.startswith("!rules ") or message.content == "!rules":

        embed = discord.Embed(title="Rules", description="1. English only. We can try translate you by google, but it is in good manners that you try to use english.\n2. Any kind of vulgar behaviour, harassment or another bad behaviour will result in warning or even ban.\n3. Please do not provide here any vulnerable data like account or password.\n4. **Do not ask for:** trial/test account, free account, free money, free gift cards\n5. Vortex is paid service, and won't be available in any kind of free access.\n\n(See #rules for more information)", color=0x0884ff)
        embed.set_author(
            name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")

        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !refund

    # if message.content.startswith("!refund ") or message.content == "!refund":
    #
    #     embed = discord.Embed(title="Refund", description="If you are not happy with Vortex you can ask for a refund (To do that, contact the support `!support`). Note, that this is only possible if you have less than 15 minutes of playtime.", color=0x0884ff)
    #     embed.set_author(
    #         name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")
    #
    #     if len(message.mentions) != 0:
    #         embed.set_footer(
    #             text="The person who was tagged can delete this message by clicking the reaction below!")
    #         msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
    #         await client.add_reaction(msg, "❌")
    #
    #     else:
    #         msg = await client.send_message(message.channel, embed=embed)
    #         i = 40
    #         while i >= 0:
    #             timer = str(i)
    #             embed.set_footer(
    #                 text="This message gets deleted automatically in " + timer + " seconds.")
    #             await client.edit_message(msg, embed=embed)
    #             i = i - 2
    #             await asyncio.sleep(2.0)
    #         await client.delete_message(msg)
    #
    #     await client.delete_message(message)

    # Command: !steam

    if message.content.startswith("!steam ") or message.content == "!steam":

        embed = discord.Embed(title="Steam", description="In order to play Steam licensed games you need to link your Steam account. To do that you must create a Steam community profile and make your games list visible for us (public).\nHere are the steps explained in details:\n\nStep 1: Create Steam community profile.\nStep 2: Go to your profile and choose privacy settings.\nStep 3: Change games list visibilty to public.\n\nWarning: We are not storing your Steam games list, ownership is checked every time you want to play a game so keep that privacy settings on public level as long as you are using Vortex.", color=0x0884ff)
        embed.set_author(
            name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")

        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !status <Status>

    if message.content == "!status online" or message.content == "!status offline" or message.content == "!status fixing" or message.content == "!status down" or message.content == "!status fix" or message.content == "!status ddos":
        if checkrole(message.author):

            if message.content == "!status online":
                await client.delete_message(message)
                embed = discord.Embed(
                    title="Vortex is online!", description="Vortex is back online and should work fine!", color=0x2DB451)
                embed.set_author(
                    name="Vortex Status", icon_url="https://i.imgur.com/UiJWZD2.png")
                await client.send_message(message.channel, embed=embed)

            if message.content == "!status offline" or message.content == "!status down":
                await client.delete_message(message)
                embed = discord.Embed(title="Investigating downtime!",
                                      description="Vortex is currently offline and not working. We don't know why yet and have to wait for an offical announcement from the Vortex team!\n\nKeep calm and have a chat with us! :)", color=0xC8001C)
                embed.set_author(
                    name="Vortex Status", icon_url="https://i.imgur.com/igOBuZp.png")
                await client.send_message(message.channel, embed=embed)

            if message.content == "!status fixing" or message.content == "!status fix":
                await client.delete_message(message)
                embed = discord.Embed(
                    title="Downtime Update", description="The team is currently working on the issue and Vortex will be back online as soon as possible!", color=0xFF9536)
                embed.set_author(
                    name="Vortex Status", icon_url="https://i.imgur.com/0G47MrY.png")
                await client.send_message(message.channel, embed=embed)

            if message.content == "!status ddos":
                await client.delete_message(message)
                embed = discord.Embed(
                    title="Downtime Update: DDoS-Attack", description="Vortex is currently undergoing a DDoS-attack. The only thing we can do is to wait.", color=0xFF9536)
                embed.set_author(
                    name="Vortex Status", icon_url="https://i.imgur.com/0G47MrY.png")
                await client.send_message(message.channel, embed=embed)

            await client.delete_message(message)
        else:
            embed = discord.Embed(
                title="Error", description="You do not have the permission to do that!\n", color=0xf31d11)

            msg = await client.send_message(message.channel, embed=embed)
            i = 10
            while i >= 0:
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)
            await client.delete_message(message)

    # Command: !maintenance <Game>

    if message.content.startswith("!maintenance "):
        if checkrole(message.author):

            if message.content == "!maintenance fortnite":
                await client.delete_message(message)
                embed = discord.Embed(
                    title="Game Maintenance", description="We are currently installing the new Fortnite update on our machines. The game will be available as soon as possible. Please bear with us!", color=0x35A3E0)
                embed.set_author(
                    name="Fortnite", icon_url="https://cdn.discordapp.com/app-assets/432980957394370572/443127594037018634.png")
                await client.send_message(message.channel, embed=embed)

            await client.delete_message(message)
        else:
            embed = discord.Embed(
                title="Error", description="You do not have the permission to do that!\n", color=0xf31d11)

            msg = await client.send_message(message.channel, embed=embed)
            i = 10
            while i >= 0:
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)
            await client.delete_message(message)

    # Command: !language, !lang

    if message.content.startswith("!language ") or message.content == "!language" or message.content.startswith("!lang ") or message.content == "!lang":

        embed = discord.Embed(
            title="Languages", description="If you need help in a certain language, check if your language is listed down below and ask those persons to help you.\n\n:flag_gb: **Otherwise try to use English!**\n\n.\n", color=0x0884ff)
        embed.add_field(name=":flag_de:",
                        value="<@219389750111502348>", inline=True)
        embed.add_field(name=":flag_gr:",
                        value="<@364515552737230848>", inline=True)
        embed.add_field(name=":flag_hr:",
                        value="<@351820668620242946>", inline=True)
        embed.add_field(name=":flag_al:",
                        value="<@364515552737230848>", inline=True)
        embed.add_field(name=":flag_bg:",
                        value="<@351820668620242946>", inline=True)
        embed.add_field(name=":flag_pl:",
                        value="<@446575267670917120>", inline=True)
        embed.set_author(
            name="Information", icon_url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/141/information-source_2139.png")

        if len(message.mentions) != 0:
            embed.set_footer(
                text="The person who was tagged can delete this message by clicking the reaction below!")
            msg = await client.send_message(message.channel, "<@" + message.raw_mentions[0] + "> :arrow_down:", embed=embed)
            await client.add_reaction(msg, "❌")

        else:
            msg = await client.send_message(message.channel, embed=embed)
            i = 40
            while i >= 0:
                timer = str(i)
                embed.set_footer(
                    text="This message gets deleted automatically in " + timer + " seconds.")
                await client.edit_message(msg, embed=embed)
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !clear

    if message.content.startswith("!clear"):
        if checkrole(message.author):
            try:
                val = int(message.content[6:])
            except ValueError:
                embed = discord.Embed(
                    title="Error", description="Usuage: !clear [number of messages]\n", color=0xf31d11)
                msg = await client.send_message(message.channel, embed=embed)
                return

            mgs = []
            number = int(message.content[6:]) + 1

            if number > 51:
                embed = discord.Embed(
                    title="Error", description="You cannot delete more than 50 messages at one time!\n", color=0xf31d11)
                msg = await client.send_message(message.channel, embed=embed)
                return

            async for x in client.logs_from(message.channel, limit=number):
                mgs.append(x)
            await client.delete_messages(mgs)

        else:
            embed = discord.Embed(
                title="Error", description="You do not have the permission to do that!\n", color=0xf31d11)
            msg = await client.send_message(message.channel, embed=embed)
            i = 10
            while i >= 0:
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)
            await client.delete_message(message)

    # Command: !uclear

    if message.content.startswith("!uclear"):
        if checkrole(message.author):

            rlen = len(message.raw_mentions[0]) + 12

            try:
                val = int(message.content[rlen:])
            except ValueError:
                embed = discord.Embed(
                    title="Error", description="Usuage: !uclear (@username) (number of messages to check)\n", color=0xf31d11)
                msg = await client.send_message(message.channel, embed=embed)
                return

            mgs = []
            number = int(message.content[rlen:]) + 1

            if number > 100:
                embed = discord.Embed(
                    title="Error", description="You cannot check more than 99 messages!\n", color=0xf31d11)
                msg = await client.send_message(message.channel, embed=embed)
                return

            async for x in client.logs_from(message.channel, limit=number):
                if x.author.id == message.raw_mentions[0]:
                    mgs.append(x)
            await client.delete_messages(mgs)

        else:
            embed = discord.Embed(
                title="Error", description="You do not have the permission to do that!\n", color=0xf31d11)
            msg = await client.send_message(message.channel, embed=embed)
            i = 10
            while i >= 0:
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)
            await client.delete_message(message)

    # Command: !patreon, !donate

    if message.content == "!patreon" or message.content == "!donate":
        embed = discord.Embed(
            title="Support me!", description="Hey! I'm just a 15 year old student and it costs me a lot of money to pay the server on which my stuff is running, for example this bot. Because it's really hard for me to pay the server fees of 40$ monthly, I would really appreciate it, if you consider helping me out by donating some money. It would help me a lot! \n\nhttps://www.patreon.com/CrazyEasy", color=0xffffff)
        embed.set_author(
            name="EASY", icon_url="https://i.imgur.com/Vb6y3jT.png")
        await client.send_message(message.channel, embed=embed)

    # Command: !bot, !about, !help

    if message.content.startswith("!about") or message.content.startswith("!bot") or message.content.startswith("!help"):

        embed = discord.Embed(
            title="About", description="Hi! I was created with Python by <@219389750111502348> and I'm here to help!\n", color=0x242424)
        embed.set_author(
            name="VortexBot", icon_url="https://i.imgur.com/yI1dXBA.png")
        embed.add_field(
            name="Commands", value="~~!trial [@username], !free [@username]~~\n!queue [@username], !wait [@username]\n!rules [@username]\n!support [@username]\n!steam [@username]\n!ping [@username], !performance [@username]\n!language [@username], !lang [@username]\n~~!refund [@username]~~\n!donate, !patreon\n!help, !about, !bot", inline=False)
        embed.add_field(
            name="Admin only:", value="!clear (number of messages)\n!uclear (@username) (number of messages to check)\n!status online\n!status offline, !status down\n!status fixing, !status fix\n!status ddos\n!maintenance (fortnite)", inline=False)

        msg = await client.send_message(message.channel, embed=embed)
        i = 30
        while i >= 0:
            timer = str(i)
            embed.set_footer(
                text="This message gets deleted automatically in " + timer + " seconds.")
            await client.edit_message(msg, embed=embed)
            i = i - 2
            await asyncio.sleep(2.0)
        await client.delete_message(msg)

        await client.delete_message(message)

    # Command: !reload

    if message.content == "!reload" or message.content == "!rl":
        if message.author.id == "219389750111502348":
            await client.add_reaction(message, "✅")
            await client.logout()
        else:
            embed = discord.Embed(
                title="Error", description="You do not have the permission to do that!\n", color=0xf31d11)

            msg = await client.send_message(message.channel, embed=embed)
            i = 10
            while i >= 0:
                i = i - 2
                await asyncio.sleep(2.0)
            await client.delete_message(msg)
            await client.delete_message(message)

    # Asking for a free account or trial

    keywords = [["free", 3], ["trial", 3], ["can", 1], ["cant", -10], ["dont", -10],
                ["i", 1], ["have", 1], ["trail", 3], ["get", 1], ["pls", 2], ["please", 2],
                ["need", 1], ["don't ", -10], ["can't ", -10], ["not", -10], ["give", 2],
                ["account", 1], ["stop", -10], ["give account", 3], ["test", 2], ["acc", 1],
                ["no paid", 3], ["wont", -10], ["won't", -10]]

    if message.content.count(" ") > 12:
        flagpoints = -10
    elif message.content.count(" ") > 16:
        flagpoints = -100
    else:
        flagpoints = 0

    for i in range(len(keywords)):
        if keywords[i][0] in message.content.lower():
            flagpoints = flagpoints + keywords[i][1]
    # print(flagpoints)

    if flagpoints > 7:
        embed = discord.Embed(
            title="Do not ask for a free account or trial! (You won't get one)", description="<@" + message.author.id + "> Please check out the rules: `!rules`", color=0xf31d11)
        embed.set_footer(
            text="This answer was automatically created because of certain keywords in you message. (" + str(flagpoints) + ")")
        msg = await client.send_message(message.channel, embed=embed)

@client.event
async def on_reaction_add(reaction, user):

    # Deleting messages by reaction

    if reaction.emoji == "❌" and user.id == reaction.message.raw_mentions[0] and reaction.message.author.id == "463396754369544202":
        await client.delete_message(reaction.message)


client.run("xxxx")
