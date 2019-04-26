from TextFiles import *
import time
import json

global lol

percents = []
uts = []

goodwords = ["good", "nice", "hilarious", "funny", "amazing","love","fine","super","superb","duper","love","XD", "cool", "hehe","ultimate","radical", "neat","lol","lmao","like","liked"]
badwords = ["bad","crap","worst","stupid","retarted","fine","shit"]

y = 0

def logic(number):

    good = 0
    bad = 0
    x = 0
    tval = 0
    percentage = 0

    while x != 20:
        global subject
        subject = text[number]
        subject = subject.lower()
        #subject = subject.strip([","])

        if goodwords[x].lower() in subject:
            good = good + 1
            #print("yes")
        else:
            tval = tval + 1
        #time.sleep(0.5)
        x = x + 1

    x = 0

    while x != 6:
        #sprint(str(x))
        if badwords[x].lower() in subject:
            bad = bad + 1
        #    print("yes")
        else:
            tval = tval + 1
        #time.sleep(0.5)
        x = x + 1


    tval = good + bad
    #print(str(tval))
    if tval == 0:
        print("Sentiment can't be detected for the comment: '" + text[number] + "'")
        uts.append(1)

    else:
        percentage = good/tval * 100


    #print(str(percentage) + "%")
    percents.append(percentage)

num = len(text)
y = num - 1
while y != -1:

    logic(y)
    y = y - 1

print("\nFinal sentiment around the product being assesed = " + str(round(sum(percents)/len(percents), 1)) + "%")
#print(str(sum(uts)))
#print(str(len(text)))

print(str(round(((len(text) - sum(uts))/len(text))*100, 1)) + "% of the comments were analysed")


time.sleep(10000)
