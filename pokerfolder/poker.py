# Work with Python 3.6
import discord
import random
import time
import pokercardsdict as pcd
TOKEN = ''


# guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)


client = discord.Client()


@client.event
async def on_message(message):

    # we do not want the bot to reply to itself
    print(message.content)
    print(message.author)
    if message.author == client.user:
        return

    if message.content.startswith('connor'):
        ListOfMessage = message.content.split(" ")
        try:
            ListOfMessage[1]
        except IndexError:
            msg = 'Hello {0.author.mention}, try connor gay'.format(message)
            await client.send_message(message.channel, msg)
        if ListOfMessage[1] == "react":
            await client.add_reaction(message, '🎉')
        if ListOfMessage[1] == "poker":

            # Initialise poker cards deck.
            PokerCardsDeck = pcd.PokerCards()
            msg = 'Hello {0.author.mention}, We will be playing Poker, Texas Hold Em. Dont know? fuck yourself'.format(
                message)
            await client.send_message(message.channel, msg)

            # msg = await client.wait_for_message(author=message.author, check=doublemention)
            # await client.send_message(message.channel, msg)

            # await client.send_message(Player2, "Your role is {}".format(Player2Role))
            #print(Player1, "Your role is {}".format(Player1Role))
            msg = ":one: :clubs: Lets start. I'll send all of you a messsage with your cards."
            await client.send_message(message.channel, msg)
            ListOfPlayers = [
                # UserID, TotalCash, Cash during the round, Playing/Folded(1/0), Checked(1 = False)
                ["Player1", 300, 0, 1, 1],
                ["Player2", 400, 0, 1, 1]
            ]

            await client.send_message(message.author, "Your cards are {} | {}".format(pcd.RemoveCardsEmoji(PokerCardsDeck), pcd.RemoveCardsEmoji(PokerCardsDeck)))
            print("Cards left:", len(PokerCardsDeck))
            PotMoney = 0

            def CallRaiseFold(msg):
                if msg.content.lower() in ["call", "raise", "fold"]:
                    return True
                else:
                    return False

            def CheckBetFold(msg):
                if msg.content.lower() in ["check", "bet", "fold"]:
                    return True
                else:
                    return False

            for RoundsIter in ["Preflop", "Flop", "Turn", "River"]:
                msg = "Round: {}".format(RoundsIter)
                await client.send_message(message.channel, msg)
                RoundsEnd = False
                HighestBid = 0
                while RoundsEnd == False:
                    for Players in ListOfPlayers:
                        if Players[3] == 0:
                            continue
                        if Players[2] < HighestBid:
                            msg = "{}, Please Call, Raise, or Fold".format(
                                Players[0])
                            await client.send_message(message.channel, msg)
                            msg = await client.wait_for_message(author=message.author, check=CallRaiseFold)
                            msg = msg.content.lower()
                            if msg == "call":
                                Players[2] = HighestBid
                            if msg == "raise":
                                msg = "Raise by how much?"
                                await client.send_message(message.channel, msg)
                                while True:
                                    msg = await client.wait_for_message(author=message.author)
                                    try:
                                        if Players[2] - int(msg.content) - HighestBid >= 0:
                                            Players[2] = HighestBid + \
                                                int(msg.content)
                                            break
                                    except:
                                        pass
                                    await client.send_message(message.channel, "You don't have enough money/Error5")
                            if msg == "fold":
                                await client.send_message(message.channel, "You folded")
                                Players[3] = 0
                                Players[4] = 0
                        if Players[2] == HighestBid:
                            if Players[4] == 1:
                                msg = "{}, Please Check, Bet, or Fold".format(
                                    Players[0])
                                await client.send_message(message.channel, msg)
                                msg = await client.wait_for_message(author=message.author, check=CheckBetFold)
                                msg = msg.content.lower()
                                if msg == "check":
                                    await client.send_message(message.channel, "You checked")
                                    Players[2] = HighestBid
                                if msg == "bet":
                                    msg = "Bet how much?"
                                    await client.send_message(message.channel, msg)
                                    while True:
                                        msg = await client.wait_for_message(author=message.author)

                                        try:
                                            if Players[2] - int(msg.content) - HighestBid >= 0:
                                                Players[2] = HighestBid + \
                                                    int(msg.content)
                                                break
                                        except:
                                            pass
                                        await client.send_message(message.channel, "You don't have enough money/Error5")
                                if msg == "fold":
                                    await client.send_message(message.channel, "You folded")
                                    Players[3] = 0
                                Players[4] = 0
                        # Checks for round end
                        # check for one player left
                    if sum(row[3] for row in ListOfPlayers) == 1:
                        RoundsEnd = True
                        await client.send_message(message.channel, "Game ended, all other players folded")
                    # check for all checked
                    if sum(row[4] for row in ListOfPlayers) == 0:
                        await client.send_message(message.channel, "All Players Checked")
                        # check for highest bid all
                        RoundsEnd = True
                        for x in ListOfPlayers:
                            if x[3] == 1:
                                if x[4] != HighestBid:
                                    RoundsEnd = False

        if ListOfMessage[1] == "secret":
            msg = 'Hello {0.author.mention}, We will be playing Secret Hitler'.format(
                message)
            await client.send_message(message.channel, msg)
            msg = 'Which two will be playing? Send in the format of "@ShibeMaster @Shibemaster"'
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "junan":
            FarmTimer = 0
            while FarmTimer == 0:
                msg = "```junan ure gay```"
                await client.send_message(message.channel, msg)
                time.sleep(5)

        if ListOfMessage[1] == "stop":
            FarmTimer = 1

        if ListOfMessage[1] == "repeat":
            msg = "/tts junan ure gay"
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "mention":
            msg = 'Hello {0.author.mention}, Youre mentioning {1[0].mention}'.format(
                message, message.mentions)
            await client.send_message(message.mentions[0], msg)

        if ListOfMessage[1] == "gay":
            msg = 'Hello {0.author.mention}, im gay'.format(message)
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "pm":
            msg = 'Hello {0.author.mention}, im gay'.format(message)
            await client.send_message(message.author, msg)

        if ListOfMessage[1] == "random":
            testnumber = random.choice([1, 2, 3, 4, 5, 6])
            msg = 'Hello {0.author.mention}, {1}'.format(message, testnumber)
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "investigator":
            InvestigatorChannel = discord.utils.get(
                message.server.channels, name="investigator", type=discord.ChannelType.text)
            await client.send_message(InvestigatorChannel, "Investigator? I barely know her")

        if ListOfMessage[1] == "hello":
            await client.send_message(message.channel, 'Say hello')
            msg = await client.wait_for_message(author=message.author, content='hello')
            await client.send_message(message.channel, 'Hello.')

        ''' THIS CODE AINT WORKING ITS DOUBLE SENDING
        else:
            msg = 'Hello {0.author.mention}, try connor pm'.format(message)
            await client.send_message(message.channel, msg)'''


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
