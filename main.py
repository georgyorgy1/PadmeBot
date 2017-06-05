#This bot is still in alpha/testing stages.
import discord
import asyncio
import random
import os
from datetime import datetime as dt
import time

bot = discord.Client();
global strtime
global count
global m
global mt
global xtime
global master
count = 0;
m = 0;
mt = 0;
master = ["213869966003273728", "174671055544123392"] #your Discord ID here. This can be a list if you want
master_chan = "321228116796112897" #Master channel here for the hourly shitposting
#xtime = str(dt.now())


booksList = {
    "CSharp-Book-2016-Rob-Miles-82.pdf": "http://www.robmiles.com/s/CSharp-Book-2016-Rob-Miles-82.pdf",
    "Inside-The-Third-Reich.txt": "https://archive.org/details/Inside_the_Third_Reich_Albert_Speer",
    "tutorial.pdf": "http://www.cplusplus.com/files/tutorial.pdf",
    "Luthereng.pdf": "http://vho.org/aaargh/fran/livres9/Luthereng.pdf",
    "mein-kampf.txt": "https://archive.org/details/meinkampf035176mbp",
    "Us-military-GermanPhraseBooken194365P..pdf": "https://archive.org/details/GermanPhraseBook_987",
    "DanzigIsGerman.pdf": "https://archive.org/details/DanzigIsGerman",
    "culture-of-critique.pdf": "https://document.li/u4Ng",
    "": "https://cdn.discordapp.com/attachments/302185287545782273/321222411422924800/Suicide_of_a_Superpower_-_Patrick_J._Buchanan.epub"
}


async def unixReport():
    global count
    while True:
        if dt.now().minute == 0: #if you want to add channels, then add more await bot.send_message stuff. Idk
            if count == 0:
                count = 1
                await bot.send_message(discord.Object(id = master_chan), "Hourly Unix Time report: " + str(int(time.time())));
                #ftime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")
                #await bot.send_message(discord.Object(id = master_chan), "```css\nBONG BONG BOT: RELOADED\n\nIt's another hour, niggers. Here are the fucking times in some cities around the world\n\nManila:\n" + ftime + "\n```")
                print(xtime + ": " + "Hourly Unix Time report sent!");

        elif dt.now().minute == 1:
            count = 0;

        await asyncio.sleep(1)

@bot.event
@asyncio.coroutine
async def on_ready():
    global count;
    global xtime;
    xtime = str(dt.now())
    await bot.change_presence(game=discord.Game(name='$help for help'))
    asyncio.get_event_loop().create_task(unixReport())
    print(xtime + ": " + "Bot is now online. Enjoy!");
    print(xtime + ": " + str(dt.now()));
    print(xtime + ": " + str(bot.user));

@bot.event
@asyncio.coroutine
async def on_message(message):
    global xtime;
    global master;
    xtime = str(dt.now())

    if message.content.startswith("$about"):
        await bot.send_message(message.channel, "PadmeBot (aka ThinkingBot/FlamePrincessBot). Copyright Emperor Kek");
        print(xtime + ": " + str(message.author.id) + " requested for " + "$about");

    elif message.content.startswith("$freshprinceofromania"):
        await bot.send_message(message.channel, "https://pastebin.com/PWFfcbZ2");
        print(xtime + ": " + str(message.author.id) + " requested for " + "$freshprinceofromania");

    elif message.content.startswith('$aesthetics'):
        await bot.send_message(message.channel, random.choice(open('roaster.txt').readlines()));
        print(xtime + ": " + str(message.author.id) + " requested for " + "$aesthetics")

    elif message.content.startswith('$submit'):
        await bot.send_message(message.channel, "This feature is currently under development. Checkback later!");
        print(xtime + ": " + str(message.author.id) + " tried to submit an aesthetic OC but forgot that OC submission is currently not possible at this time");

    elif message.content.startswith('$mindtrick'):
        if message.author.id in master:
            str_content = message.content[len('$mindtrick'):].strip();
            await bot.send_message(message.channel, str_content);
            print(xtime + ": " + "$mindtrick request sent!")
            str_content = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$mindtrick but was not granted access due to ID not matching");

    elif message.content.startswith("$daisy") or message.content.startswith("$streetfucking"):
        await bot.send_message(message.channel, "https://pastebin.com/AcsS5MjD <=== BEST STORY 2017");
        print(xtime + ": " + str(message.author.id) + " requested for " + "My Dream");

    elif message.content.startswith("$unixtime"):
        await bot.send_message(message.channel, "Current Unix Time: " + str(int(time.time())));
        print(xtime + ": " + str(message.author.id) + " requested for current Unix Time.")

    elif message.content.startswith("$ping"):
        await bot.send_message(message.channel, "Pong!. Also, I can't tell the time it took to ping you back.");
        print(xtime + ": " + str(message.author.id) + " requested for $ping.")

    elif message.content.startswith("$r"):
        if message.author.id in master:
            str_contento = message.content[len('$r'):].strip();
            str_contente = "t!rep " + str_contento
            await bot.send_message(message.channel, str_contente);
            print(xtime + ": " + "$r request sent!")
            str_contento = "";
            str_contente = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$r but was not granted access due to ID not matching");

    elif message.content.startswith("$d"):
        if message.author.id in master:
            str_contenta = message.content[len('$d'):].strip();
            str_contentb = "t!daily " + str_contenta;
            await bot.send_message(message.channel, str_contentb);
            print(xtime + ": " + "$d request sent!")
            str_contenta = "";
            str_contentb = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$d but was not granted access due to ID not matching" );

    elif message.content.startswith("$bongtest"):
        mtime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")
        await bot.send_message(message.channel, "```css\nBONG BONG BOT: RELOADED\n\nIt's another hour, niggers. Here are the fucking times in some cities around the world\n\nManila:\n" + mtime + "\n```")
        print(xtime + ": " + "This fag asked for bong bong: " + str(message.author.id))

    elif message.content.startswith("$irand"):
        irand = random.randint(0, 2147483647)
        await bot.send_message(message.channel, str(irand))
        print(xtime + ": " + str(message.author.id) + " generated a random number using irand")

    elif message.content.startswith("$help"):
        e = discord.Embed(colour=0x3F6A7F)
        theText = open("help.txt")
        e.title = "Hey there, {}, I'm Padme, the senator from Naboo and wife of the Chosen One.".format(str(message.author)[:-5])
        e.description = theText.read()
        await bot.send_message(message.channel, embed=e);
        theText.close()
        print(xtime + ": " + str(message.author.id) + " requested for " + "$help")

    elif message.content.startswith("$nrand"):
        xrand =  message.content[len('$nrand'):].strip();
        
        if xrand == "":
            await bot.send_message(message.channel, "```\nThe nrand command generates a random number from 0 to your specified range (up to the number you desire). \n\nDo ($nrand <number range>) (without ()) to generate a random number.\n```")
            print(xtime + ": " + str(message.author.id) + " asked for help on nrand")

        else:
            exr = False

            try:
                int(xrand)

                if int(xrand) < 0:
                    await bot.send_message(message.channel, "The number you have entered is a negative number!")
                    print(xtime + ": " + str(message.author.id) + " entered a negative number")
                    exr = False

                elif int(xrand) > 9223372036854775807:
                    await bot.send_message(message.channel, "The number you have entered is too big! (9223372036854775807 is the limit)")
                    exr = False
                    print(xtime + ": " + str(message.author.id) + " entered a negative number")

                else:
                    exr = True

            except ValueError:
                exr = False

            if exr == False:
                await bot.send_message(message.channel, "The number you have entered is not an integer!")
                print(xtime + ": " + str(message.author.id) + " entered a non-integer number")

            else:
                randint = random.randint(0, int(xrand))
                await bot.send_message(message.channel, str(randint))
                print(xtime + ": " + str(message.author.id) + " generated a random number using nrand")

    elif message.content.startswith("$ebook") or message.content.startswith("$book"):
        await bot.send_message(message.channel, random.choice(open('books.txt').readlines()));
        print(xtime + ": " + "$ebook requested by " + message.author.id)
        
    elif message.content.startswith("$sesocuck"):
        await bot.send_message(message.channel, "https://youtu.be/c6S8cgAoaNM");
        print(str(message.author) + " requested for $sesocuck")

    if "lol" in message.content:
        await bot.add_reaction(message, '😂')
        print(xtime + ": " + "Emoji shitpost requested by " + message.author.id)

    if 'big guy' in message.content:
        global m
        global mt

        if m == 0:
            m = 1
            mt = dt.now().minute
            await bot.send_message(discord.Object(id = master_chan), "4u");
            print(str(message.author.id) + " requested for big guy");

        else:
            m = 1

    if dt.now().minute == mt + 2:
        m = 0;

def main():
    global xtime
    xtime = str(dt.now())
    email = "";
    password = "";
    token = "";
    bot_start = "u" #input("Start bot as?(u/t): ");

    if bot_start == "u":
        email = input(xtime + ": " + "Enter email: ");
        password = input(xtime + ": " + "Enter password: ");
        print(xtime + ": " + "Executing startup sequence");
        bot.run(email, password);
        email = "";
        password = "";

    elif bot_start == "t":
        token = input(xtime + ": " + "Enter token: ");
        bot.run(token);
        print(xtime + ": " + "Executing startup sequence");

    else:
        print(xtime + ": " + "Invalid. Shutting down.....");
        quit();

main();
