import discord
import asyncio

client = discord.Client()
member = discord.Member
user = discord.User
server = discord.Server
game = discord.game
lastedit = "June 12, 2016"
ver = "build 0.04 0x001 - Styrofoam"
prefix = "*"
owner = "SporadicToast"
ownerid = 169064821382316032
clid = 191088734345625600

@client.event
async def on_ready():
    print('Client software ready!')
    print('Bot         {} | {}'.format(client.user.name, client.user.id))
    print('Owner       {} | {}'.format(owner, ownerid))
    print('')
    print('Current command prefix is > {} <'.format(prefix))
    print("{}'s version is {}|{}".format(client.user.name, ver, lastedit))
    print("===============LOGGING===============")
@client.event
async def on_message(message):
    ban = [169066265858539521]
    userid = message.author.id
    if int(userid) in ban:
        if message.content.startswith('{}'.format(prefix)):        
            print('[Security] Banned user attempted to command - {}|{}.'.format(message.author, message.author.id))
    else:
        if message.content.startswith('{}'.format(prefix)):
            print('Command recieved - {}|{} - {}'.format(message.author, message.author.id, message.content))
        if message.content.startswith('{}messagecount'.format(prefix)):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        elif message.content.startswith('{}sleep'.format(prefix)):
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')

        elif message.content.startswith('{}help'.format(prefix)):
            await client.send_message(message.channel, 'Hello! I am {} - ID {}'.format(client.user.name, client.user.id))

        elif message.content.startswith('{}msgdata'.format(prefix)):
            await client.send_message(message.channel, 'Understood, the one who sent that message was {}, it contained {}, message id is {}'.format(message.author, message.content, message.id))
        
        elif "this bot sucks" in message.content:
            await client.send_message(message.channel, ":c")     
        
        elif message.content.startswith('{}info'.format(prefix)):
            await client.send_message(message.channel, "Konnichiwa! \nI am **{}**, or ***Yukinon***! \nI was written in Python 3.5 by {} as pretty much to kill time. \nI lack alot of features, but I hope we can work together".format(client.user.name, owner))
            dumpmsg =  "Statistics Dump: \n{} | {} : prefix.type; {} : system.version; {} ".format(client.user.name, client.user.id, prefix, ver)
            librarybuild =  "\n\n= Library Build ============ \nmessagecount, sleep, help, msgdata, authkey, authkey2, userinfo, troll1, troll2, format"
            infomsg = "```" + dumpmsg + librarybuild + "```"
            await client.send_message(message.channel, infomsg)
        elif message.content.startswith('{}authkey1'.format(prefix)):
            await client.send_message(message.channel, "Checking if user {0.author.mention} has proper authentication...".format(message))
            print('[Authentication] - Authorization request from {}/{} - {} | {} : {}'.format(message.server, message.channel, message.author, message.author.id, message.content))
            a = message.author.id
            b = ownerid 

            if int(a) == int(b):
                    print('[Authentication] - Authorization hereby granted for {} from {}/{}'.format(message.author, message.server, message.channel))
                    await client.send_message(message.channel, '{0.author.mention} is an authorized user. Creating oauth2 ID and mailing it.'.format(message))
                    oauth = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0x00218800".format(clid)
                    await client.send_message(message.channel, 'OAuth2 message sent!')
                    await client.send_message(message.author, 'Authentication key for {} | {} - {} : {}'.format(client.user.name, client.user.id, ver, oauth))
            else:
                    print('[AuthFailure] - Authorization failed for {}|{} from {}/{} : {}'.format(message.author, message.author.id, message.server, message.channel, message.content))    
        
        elif message.content.startswith('{}authkey2'.format(prefix)):
            await client.send_message(message.channel, "Checking if user {0.author.mention} has proper authentication...".format(message))
            print('[Authentication] - Authorization request from {}/{} - {} | {} : {}'.format(message.server, message.channel, message.author, message.author.id, message.content))
            a = message.author.id
            b = ownerid 
            c = 191089034733289472
            if int(a) == int(b):
                    print('[Authentication] - Authorization hereby granted for {} from {}/{}'.format(message.author, message.server, message.channel))
                    await client.send_message(message.channel, '{0.author.mention} is an authorized user. Creating oauth2 ID and mailing it.'.format(message))
                    oauth = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0x00218800".format(c)
                    await client.send_message(message.channel, 'OAuth2 message sent!')
                    await client.send_message(message.author, 'Authentication key for {} | {} - {} : {}'.format("Miyazuki", "???", "v1.9.5c", oauth))
            else:
                    print('[AuthFailure] - Authorization failed for {}|{} from {}/{} : {}'.format(message.author, message.author.id, message.server, message.channel, message.content))           
        elif message.content.startswith('{}userinfo'.format(prefix)):
            print("Hi")
        elif message.content.startswith('{}ulol-ba-si-gian?'.format(prefix)):
            await client.send_message(message.channel, 'Yep! Sobrang ulol po ni Gian, {0.author.mention}.'.format(message))
        elif "marc" in message.content.lower():
            await client.send_message(message.channel, 'My master has been called! :D')    
        elif "thunder" in message.content.lower():
            await client.send_message(message.channel, '***PUTANGINA GUYS KUMIKIDLAT***')  
        elif "dat boi" in message.content.lower():
            await client.send_message(message.channel, 'oh shit ***whaddup***')  
        elif "boi" in message.content.lower():
            await client.send_message(message.channel, 'oh shit ***whaddup***')                                  
        elif "*tsk" in message.content:
            await client.send_message(message.channel, 'tsk')            
        elif message.content.startswith('{}format'.format(prefix)):
            send = ""
            send += "```"
            send += "====== Formatting 101 ====== \n `content` - format one line code, triple for code block \n *italics* - Italicizes text \n **bold** - Bolds text \n ***bold-italics*** - Bold Italicizes test \n __underline__ - Underlines text \n ~~strikethrough~~ - Strikes through text"
            send += "```"   
            await client.send_message(message.author, send)     
        elif message.content.startswith('{}codefilipino'.format(prefix)):
            await client.send_message(message.channel, '{0.author.mention}, Google Classroom password for **Filipino** is `cnca3u`'.format(message))
client.run('MTkxMDk0MjcxODI5MzQ0MjU2.Cj1Uqg.noo9wZF0i9HCyfE03ZEaWneJ7w0')
os.system("title Running Yukino - ver {}".format(ver))