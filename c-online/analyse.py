import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv




#data = np.genfromtxt('test.csv', delimiter=',')



if len(sys.argv) == 1:
    print("Usage: python analyse.py UserID Task Event Data")
    exit()


userID,task,event,data = sys.argv[1:]

with open('test.csv',  'r') as csvfile:
    reader = csv.reader(csvfile)
    corrects = filter(lambda x:x[2] == "Solution Correct" and x[1] == task, reader)
    times = np.fromiter((x[3] for x in corrects),dtype = int)

    fig1,ax1 = plt.subplots()
    ax1.boxplot(times)
    plt.savefig("test.png")

    mean = np.mean(times)
