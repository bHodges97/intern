import os
import csv
from random import *

header = ["UserID","Topic","Task","Event","Data"]

def rand_time():
    return str(round(normalvariate(300,20)))

def makerow(userID,topic,task):
    event_list = ["Compile Success","Compile Fail","Solution Correct","Solution Incorrect"]
    event = choices(event_list,weights= [10,90,5,45])[0]
    data = ""
    if event == event_list[0]:
        if random() > 0.2:
            data = rand_time()
        else:
            data = 0#time out
    else:
        data= rand_time()

    row = [userID, topic, task, event, data]
    return row


with open('test.csv',  'w') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(header)

    #fake 200 users
    users = set()
    while len(users) < 200:
        users.add(randrange(10000))
    for user in users:
        for i in range(randrange(12)):
            tasks = {randrange(108) for i in range(randrange(10))}
            for task in tasks:
                row = makerow(user,task%7,task)
                writer.writerow(row)
