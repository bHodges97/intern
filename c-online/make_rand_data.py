import os
import csv
from random import *

header = ["UserID","Task","Event","Data"]

def rand_time():
    return str(round(normalvariate(300,20)))

def makerow():
    event_list = ["Compile Success","Compile Fail","Solution Correct","Solution Incorrect"]

    userID = randrange(200)
    task = str(randrange(1,8)) + "-" + str(randrange(1,8)) + "-" + str(randrange(1,108))
    event = choices(event_list,weights= [10,90,5,45])[0]
    data = ""
    if event == event_list[0]:
        if random() > 0.2:
            data = rand_time()
        else:
            data = 0#time out
    else:
        data= rand_time()

    row = [userID, task, event, data]
    return row


with open('test.csv',  'w') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(header)
    for i in range(100000):
        writer.writerow(makerow())
