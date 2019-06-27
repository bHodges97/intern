import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

#data = np.genfromtxt('test.csv', delimiter=',')

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python analyse.py UserID Topic Task Event Data")
        exit()


    userID,topic,task,event,data = sys.argv[1:]
    fieldNames = ["UserId","Topic","Task","Event","Data"]

    with open('test.csv',  'r') as csvfile:
        reader = csv.reader(csvfile)
        corrects = filter(lambda x:x[3] == 'Solution Correct' and x[2] == task, reader)
        times = np.fromiter((x[4] for x in corrects),dtype = int)

        fig1,ax1 = plt.subplots()
        ax1.boxplot(times)
        ax1.set_ylabel("Time taken(s)")
        ax1.set_xlabel("Task")
        ax1.xaxis.set_ticklabels([task])
        #for spine in ax1.spines.values():
            #spine.set_visible(False)
        plt.savefig("test.png")

        mean = np.mean(times)
