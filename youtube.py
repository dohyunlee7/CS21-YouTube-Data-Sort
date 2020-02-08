"""
Dohyun Lee
April 10th, 2019
A program that analyzes YouTube data using sorting algorithms.
"""
from ytchannel import *
def main():
    print("Welcome to my YouTube Channel Program!")
    ytLst = readData()
    k = int(input("How many top channels do you want to see? "))
    while k < 1:
        k = int(input("Invalid input. How many top channels do you want to see? "))
    print()
    uploads(k,ytLst)
    print()
    subs(k,ytLst)
    print()
    views(k,ytLst)

def readData():
    """
    purpose: reads the file data and imports the data to our sort program
    parameters: none
    returns: lst -- a list of the YouTube data
    """
    file = input("Enter the name of the YouTube data file: ")
    while len(file) == 0:
        file = input("Please enter the name of the YouTube data file: ")
    myfile = open(file, "r")
    lst = []
    i = 0
    for line in myfile:
        if i != 0:
            txt = line.strip().split(",")
            ch = Channel(txt[0], int(txt[1]), int(txt[2]), int(txt[3]))
            lst.append(ch)
        i = i + 1
    myfile.close()
    return lst

def uploads(k,ytLst):
    """
    purpose: sorts the top 'k' channels by their uploads in descending order
    parameters: k -- size of list, ytLst -- list of data
    returns: none
    """
    for num in range(len(ytLst)-1,0,-1):
        for i in range(num):
            if ytLst[i].getUploads() < ytLst[i+1].getUploads():
                temp = ytLst[i]
                ytLst[i] = ytLst[i+1]
                ytLst[i+1] = temp
    print("Top %d channels by number of uploads:" % (k))
    if k >= len(ytLst):
        print("The list is out of range")
    else:
        print("Channel                      Uploads")
        for x in range(k):
            print("%-25s    %5d" % (ytLst[x].getName(),ytLst[x].getUploads()))

def subs(k,ytLst):
    """
    purpose: sorts the top 'k' subscribed channels and # of subscribers in descending order
    parameters: k -- size of list, ytLst -- list of data
    returns: none
    """
    for num in range(len(ytLst)-1,0,-1):
        for i in range(num):
            if ytLst[i].getSubscribers() < ytLst[i+1].getSubscribers():
                temp = ytLst[i]
                ytLst[i] = ytLst[i+1]
                ytLst[i+1] = temp
    print("Top %d channels by number of subscribers:" % (k))
    if k >= len(ytLst):
        print("The list is out of range")
    else:
        print("Channel                      Subscribers")
        for x in range(k):
            print("%-25s    %5d" % (ytLst[x].getName(),ytLst[x].getSubscribers()))

def views(k,ytLst):
    """
    purpose: sorts the top 'k' viewed channels and their views in descending order
    parameters: k -- size of list, ytLst -- list of data
    returns: none
    """
    for num in range(len(ytLst)-1,0,-1):
        for i in range(num):
            if ytLst[i].getViews() < ytLst[i+1].getViews():
                temp = ytLst[i]
                ytLst[i] = ytLst[i+1]
                ytLst[i+1] = temp
    print("Top %d channels by number of views:" %(k))
    if k >= len(ytLst):
        print("The list is out of range")
    else:
        print("Channel                      Views")
        for x in range(k):
            print("%-25s    %5d" % (ytLst[x].getName(),ytLst[x].getViews()))
main()
