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
count = 0;
m = 0;
mt = 0;
#xtime = str(dt.now())

def func_test():
    time.sleep(0.1)
    time.sleep(0.1)

@bot.event
@asyncio.coroutine
async def on_ready():
    global count;
    global xtime;
    xtime = str(dt.now())
    await bot.change_presence(game=discord.Game(name='$help for help'))
    print(xtime + ": " + "Bot is now online. Enjoy!");
    print(xtime + ": " + str(dt.now()));
    print(xtime + ": " + str(bot.user));

@bot.event
@asyncio.coroutine
async def on_message(message):
    # filer = open("roaster.txt", "r");
    global xtime
    xtime = str(dt.now())
    global count;

    if message.content.startswith("$about"):
        await bot.send_message(message.channel, "PadmeBot (aka ThinkingBot/FlamePrincessBot). Copyright Emperor Kek");
        print(xtime + ": " + str(message.author.id) + " requested for " + "$about");

    if message.content.startswith("$freshprinceofromania"):
        await bot.send_message(message.channel, "https://pastebin.com/PWFfcbZ2");
        print(xtime + ": " + str(message.author.id) + " requested for " + "$freshprinceofromania");

    if message.content.startswith('$aesthetics'):
        await bot.send_message(message.channel, random.choice(open('roaster.txt').readlines()));
        print(xtime + ": " + str(message.author.id) + " requested for " + "$aesthetics")

    if message.content.startswith('$submit'):
        await bot.send_message(message.channel, "This feature is currently under development. Checkback later!");
        print(xtime + ": " + str(message.author.id) + " tried to submit an aesthetic OC but forgot that OC submission is currently not possible at this time");

    if message.content.startswith('$mindtrick'):
        if message.author.id == "213869966003273728":
            str_content = message.content[len('$mindtrick'):].strip();
            await bot.send_message(message.channel, str_content);
            print(xtime + ": " + "$mindtrick request sent!")
            str_content = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$mindtrick but was not granted access due to ID not matching");

    if message.content.startswith("$daisy") or message.content.startswith("$streetfucking"):
        await bot.send_message(message.channel, "https://pastebin.com/AcsS5MjD <=== BEST STORY 2017");
        print(xtime + ": " + str(message.author.id) + " requested for " + "My Dream");

    if dt.now().minute == 0:
        if count == 0:
            count = 1
            await bot.send_message(discord.Object(id = "275686777560236044"), "Hourly Unix Time report: " + str(int(time.time())));
            #ftime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")
            #await bot.send_message(discord.Object(id = "302185287545782273"), "```css\nBONG BONG BOT: RELOADED\n\nIt's another hour, niggers. Here are the fucking times in some cities around the world\n\nManila:\n" + ftime + "\n```")
            #print("This fag asked for bong bong: " + str(message.author.id))
            print(xtime + ": " + "Hourly Unix Time report sent!");

        else:
            count = 1;

    if dt.now().minute == 1:
        count = 0;

    if message.content.startswith("$unixtime"):
        await bot.send_message(message.channel, "Current Unix Time: " + str(int(time.time())));
        print(xtime + ": " + str(message.author.id) + " requested for current Unix Time.")

    if message.content.startswith("$ping"):
        await bot.send_message(message.channel, "Pong!. Also, I can't tell the time it took to ping you back.");
        print(xtime + ": " + str(message.author.id) + " requested for $ping.")

    if message.content.startswith("$r"):
        if message.author.id == "213869966003273728":
            str_contento = message.content[len('$r'):].strip();
            str_contente = "t!rep " + str_contento
            await bot.send_message(message.channel, str_contente);
            print(xtime + ": " + "$r request sent!")
            str_contento = "";
            str_contente = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$r but was not granted access due to ID not matching");

    if message.content.startswith("$d"):
        if message.author.id == "213869966003273728":
            str_contenta = message.content[len('$d'):].strip();
            str_contentb = "t!daily " + str_contenta;
            await bot.send_message(message.channel, str_contentb);
            print(xtime + ": " + "$d request sent!")
            str_contenta = "";
            str_contentb = "";

        else:
            await bot.send_message(message.channel, "You're not my master!");
            print(xtime + ": " + str(message.author.id) + " requested for " + "$d but was not granted access due to ID not matching" );

    if message.content.startswith("$bongtest"):
        mtime = time.strftime("%A, %B %d, %Y %I:%M:%S %p")
        #rtime = dt.strptime(mtime, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        await bot.send_message(message.channel, "```css\nBONG BONG BOT: RELOADED\n\nIt's another hour, niggers. Here are the fucking times in some cities around the world\n\nManila:\n" + mtime + "\n```")
        print(xtime + ": " + "This fag asked for bong bong: " + str(message.author.id))

    if message.content.startswith("$irand"):
        irand = random.randint(0, 2147483647)
        await bot.send_message(message.channel, str(irand))
        print(xtime + ": " + str(message.author.id) + " generated a random number using irand")

    if message.content.startswith("$help"):
        await bot.send_message(message.channel, open('help.txt').read());
        print(xtime + ": " + str(message.author.id) + " requested for " + "$help")

    if message.content.startswith("$nrand"):
        xrand =  message.content[len('$nrand'):].strip();
        #xrand = random.randint(0, 2147483647)
        #await bot.send_message(message.channel, str(xrand))
        #print(xtime + ": " + str(message.author.id) + " generated a random number")

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

    if message.content.startswith("$ebook") or message.content.startswith("$book"):
        await bot.send_message(message.channel, random.choice(open('books.txt').readlines()));
        print(xtime + ": " + "$ebook requested by " + message.author.id)

    #if "lol" in message.content:
        #global mt
        #global m

        # mt = dt.now().minute
        # m = 1
        #await bot.add_reaction(message, '😂')
        #print(xtime + ": " + "Emoji shitpost requested by " + message.author.id)
        # print(str(message.author.id) + " requested for big guy")

        #if m == 0:
            #mt = dt.now().minute
            #m = 1
            #await bot.send_message(message.channel, "4u");
            #print(str(message.author.id) + " requested for big guy")

    #if dt.now().minute == mt + 2:
        #m = 0

    #if message.content.startswith("$sesocuck"):
        #await bot.send_message(message.channel, "https://youtu.be/c6S8cgAoaNM");
        #print(str(message.author) + " requested for $sesocuck")

    #if message.content.find('big guy'):
        #global m
        #global mt

        #if m == 0:
            #m = 1
            #mt = dt.now().minute
            #await bot.send_message(discord.Object(id="298735319694704640"), str(dt.now()));

        #else:
            #m = 1

    #if dt.now().minute == mt + 2:
        #m = 0;

def main():
    global xtime
    xtime = str(dt.now())
    email = "";
    password = "";
    token = "";
    bot_start = "u" #input("Start bot as?(u/t): ");

    if bot_start == "u":
        #email = input(xtime + ": " + "Enter email: ");
        #password = input(xtime + ": " + "Enter password: ");
        email = "georgesorsisafaggot@muslim.com";
        password = "H9$/jH!KRrLZ?'3,";
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