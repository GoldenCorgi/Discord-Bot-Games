# Work with Python 3.6
import discord
import random
import time

TOKEN = ''





client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('connor'):
        ListOfMessage = message.content.split(" ")
        try:
            ListOfMessage[1]
        except IndexError:
            msg = 'Hello {0.author.mention}, try connor gay'.format(message)
            await client.send_message(message.channel, msg)
        if ListOfMessage[1] == "inhuman":
            # Player Variables
            #Player1 = ""
            Player2 = ""
            # List Variables
            ListOfPeacefulRobot = ["You may not mention any people other than strangers or enemies","You may not discuss anything that happened before you woke up this morning","You may not express opinions and only state observable facts","You may only mention objects that you can see from where you are sitting","Once the investigator mention a specific person/place/thing you may not mention that thing","Once you have mentioned an animal vegetable or mineral you may not mention examples of other two types of things for the rest of the round","you may not say the words 'think' 'thought' 'feel' or 'felt'","You must describe emotions only using physical description (crying or sweating palms NOT sad or nervous)","You may only describe good consequences and must take credit for them"]
            ListOfViolentRobot = ["Mention an animal in response to 3 different questions","Make an animal noise","Interrupt the investigator 3 times to add detail to a description","Continue to describe something until interrupted","Describe 3 verbal disagreements you have had","Insult the investigator 2 times","Explain where you got the idea for 3 things you have made up","Guess the inspiration for 2 of the investigators question","Mention the same imagined thing in response to 4 questions","Mention 3 imaginery locations","Give 1-word answers to 3 questions. Do not elaborate until asked","Describe how 3 things seem unfair to you","For 2 times say what you think should have happened instead","Blame someone else for something 3 times huh hongyao","Blame yourself for something 3 times huh junan","Describe dealing with 3 different tragedies the same way","Refer to the same friend or family member 4 times"]
            ListOfInterrogationQuestion = ["Share a plan for some time in the next seven days","Describe a project or task they worked on recently","Share a conversation they had recently or expect to have"]
            ListOfSecondaryInterrogation = ["Guess what another person might have thought","Describe something they enjoyed or expect to enjoy","Describe a challenge they recently faced"]
            ListOfPenaltyCard = ["Apologize","Swear","Snap your fingers","Clap loudly","Mispronounce a word","hum three notes","say three consecutive words beginngin with the same letter","say two consecutive rhyming words","remain silent for ten seconds","interrupt the investigator","say your last name","fail to complete a sentence","repeat a question word for word","begin a new sentence with the last word spoken"]
            ListOfSuspectPersonality = ["Compulsive liar","Friends with the president","Cult Leader","Imprisoned for life","Professional Actor","Professional Criminal","Famous Kpop Star","Famous Olympics Champion","Very old","On life support","Dishonorably discharged from the military"]
            
            SuspectPersonality = random.choice(ListOfSuspectPersonality)

            msg = 'Hello {0.author.mention}, We will be playing Inhuman Conditions, rules at https://robots.management/'.format(message)
            await client.send_message(message.channel, msg)
            msg = 'Which two will be playing? Send in the format of "@ShibeMaster @Shibemaster"'
            await client.send_message(message.channel, msg)

            def doublemention(msg):
                if len(msg.mentions) == 1:
               # if len(msg.mentions) == 2:
                    return msg.mentions
            
            msg = await client.wait_for_message(author=message.author, check=doublemention)
            # Player1 = msg.mentions[1]
            Player2 = msg.mentions[0]
            msg = "The players for this game will be {}. Please check your direct message for your roles".format(msg.content)
            await client.send_message(message.channel, msg)
           # print(Player1)
            print(Player2)
            #Player1Role = "Investigator"
            Player2Role = random.choice(["Human","Peaceful Robot","Violent Robot"])
            #await client.send_message(Player1, "Your role is {}".format(Player1Role))
            await client.send_message(Player2, "Your role is {}".format(Player2Role))
            #print(Player1, "Your role is {}".format(Player1Role))
            print(Player2, "Your role is {}".format(Player2Role))    
            msg = "Roles has been sent. Please proceed to the channels for your specific role. Robot/Human, please proceed to Suspect. Investigators, please proceed to Investigator"
            await client.send_message(message.channel, msg)

            InvestigatorChannel = discord.utils.get(message.server.channels, name="investigator", type=discord.ChannelType.text)
            SuspectChannel = discord.utils.get(message.server.channels, name="suspect", type=discord.ChannelType.text)
            await client.send_message(InvestigatorChannel, "Investigator? I barely know her.")
            await client.send_message(InvestigatorChannel, "Ensure  all  human  Suspects  are  properly  identified  as  HUMAN and ensure  all  robot  Suspects  are  identified  as  ROBOT  and  safely detained")
            await client.send_message(InvestigatorChannel, "There are two types of robots, Peaceful and Violent. Peaceful will try to pretend to be human, whereas Violent robots have to complete 2 out of 3 of their tasks to be a deviant and kill you. Prevent this at all cost.")
            await client.send_message(InvestigatorChannel, "Choose one out of the three following penalty cards to discard. E.g. reply with '2' to remove 2")
            #to do - list of penalty cards https://stackoverflow.com/questions/1262955/how-do-i-pick-2-random-items-from-a-python-set
            PenaltyList3 = random.sample(ListOfPenaltyCard, 3)
            # PenaltyList3 = ["test1","test2","test3"]
            await client.send_message(InvestigatorChannel, "```1. {}\n2. {}\n3. {}```".format(PenaltyList3[0],PenaltyList3[1],PenaltyList3[2]))
            while len(PenaltyList3) == 3:
                msg = await client.wait_for_message(channel=InvestigatorChannel)
                if msg.content == "1":
                    PenaltyList3 = [PenaltyList3[1],PenaltyList3[2]]
                if msg.content == "2":
                    PenaltyList3 = [PenaltyList3[0],PenaltyList3[2]]
                if msg.content == "3":
                    PenaltyList3 = [PenaltyList3[0],PenaltyList3[1]]
            await client.send_message(InvestigatorChannel, "The suspect will now choose his penalty card. Please wait.")
            await client.send_message(SuspectChannel, "Choose your penalty card INMATE. We do not like deviants. E.g. reply with '2' to choose 2")
            await client.send_message(SuspectChannel, "```1. {}\n2. {}```".format(PenaltyList3[0],PenaltyList3[1]))
            PenaltyCard = ""
            while PenaltyCard == "":
                msg = await client.wait_for_message()
                if msg.content == "1":
                    PenaltyCard = [PenaltyList3[0]]
                if msg.content == "2":
                    PenaltyCard = [PenaltyList3[1]]
            await client.send_message(InvestigatorChannel, "The Penalty is ```{}```".format(PenaltyCard[0]))
            await client.send_message(SuspectChannel, "The Penalty is ```{}```".format(PenaltyCard[0]))
            if Player2Role == "Peaceful Robot":
                await client.send_message(SuspectChannel, "Peaceful Robot, your restriction is {}.".format(random.choice(ListOfPeacefulRobot)))
            if Player2Role == "Violent Robot":
                await client.send_message(SuspectChannel, "Violent Robot, your criterias are ```1. {}\n2. {}\n3. Perform the penalty twice```".format(random.choice(ListOfViolentRobot),random.choice(ListOfViolentRobot)))
                await client.send_message(SuspectChannel, "You only need to complete 2 out of the 3 criterias, then kill la kill")
            if Player2Role == "Human":
                await client.send_message(SuspectChannel, "You're human as human can get, god damn deviants and their donkey nonsense. Do whatever you can to convince the investigator youre human.")
            await client.send_message(InvestigatorChannel, "***The suspect is ```{}```***".format(SuspectPersonality))
            await client.send_message(SuspectChannel, "***You are ```{}```***".format(SuspectPersonality))
            await client.send_message(InvestigatorChannel, "The interrogation starts now for 5 minutes. You may question the suspect any question you want, but you must at least fulfill the 2 question given.")
            await client.send_message(SuspectChannel, "The interrogation starts now for 5 minutes. Survive.")

            await client.send_message(InvestigatorChannel, "Type 'qn' to get the next question. \nType 'robot' to jail the suspect, if they are human you lose. \nType 'human' to release the suspect.")
            await client.send_message(SuspectChannel, "Type 'kill' to kill the investigator once you completed your tasks. \nType 'rerollp' to reroll your criterias for peaceful robots\nType 'rerollv' to reroll your criterias for violent robots\nType 'rerollrole' to reroll your role")
            gametime = 0
            while gametime == 0:
                msg = await client.wait_for_message()
                if msg.content == "kill":
                    gametime = gametime + 1
                if msg.content == "robot":
                    gametime = gametime + 1
                if msg.content == "human":
                    gametime = gametime + 1
                if msg.content == "qn":
                    await client.send_message(InvestigatorChannel, "Inquisitor, your next question is '**{}**'\nSecondary question is '**{}**'.".format(random.choice(ListOfInterrogationQuestion),random.choice(ListOfSecondaryInterrogation)))
                if msg.content == "rerollp":
                    await client.send_message(SuspectChannel, "Peaceful Robot, your restriction is **{}**.".format(random.choice(ListOfPeacefulRobot)))
                if msg.content == "rerollv":
                    await client.send_message(SuspectChannel, "Violent Robot, your criterias are ```1. {}\n2. {}\n3. Perform the penalty twice```".format(random.choice(ListOfViolentRobot),random.choice(ListOfViolentRobot)))
                if msg.content == "rerollrole":
                    SuspectPersonality = random.choice(ListOfSuspectPersonality)
                    await client.send_message(InvestigatorChannel, "***The suspect is ```{}```***".format(SuspectPersonality))
                    await client.send_message(SuspectChannel, "***You are ```{}```***".format(SuspectPersonality))
            await client.send_message(InvestigatorChannel, "The game ended! {} is {}.".format(Player2, Player2Role))
            await client.send_message(SuspectChannel, "The game ended! {} is {}.".format(Player2, Player2Role))         

        if ListOfMessage[1] == "secret":
            msg = 'Hello {0.author.mention}, We will be playing Secret Hitler'.format(message)
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
            msg = 'Hello {0.author.mention}, Youre mentioning {1[0].mention}'.format(message,message.mentions)
            await client.send_message(message.mentions[0], msg)
            

        if ListOfMessage[1] == "gay":
            msg = 'Hello {0.author.mention}, im gay'.format(message)
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "pm":
            msg = 'Hello {0.author.mention}, im gay'.format(message)
            await client.send_message(message.author, msg)

        if ListOfMessage[1] == "random":
            testnumber=random.choice([1,2,3,4,5,6])
            msg = 'Hello {0.author.mention}, {1}'.format(message, testnumber)
            await client.send_message(message.channel, msg)

        if ListOfMessage[1] == "investigator":
            InvestigatorChannel = discord.utils.get(message.server.channels, name="investigator", type=discord.ChannelType.text)
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